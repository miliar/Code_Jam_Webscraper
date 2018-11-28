#include<string>
#include<iostream>
#include<sstream>
#include<assert.h>
#include<cstdio>
#include<map>
#include<algorithm>
#include<bitset>
#include<cmath>
#include<queue>
#include<functional>
#include<set>
#include<sys/stat.h> 
const bool ENABLE_MULTI_PROCESS = true;
using namespace std;

//=========================================================
// program:
//
int K, D;
long long S[10];

const int MAX_PRIME = 1000000;
int pn;
int primes[MAX_PRIME+1];
bool composite[MAX_PRIME+1];

int digiNum(int x) {
    int s = 0;
    while( x > 0) {
        x /= 10;
        s ++;
    }
    return s;
}

void solve() {
    
    int next = -1;
    for (int p=0; p<pn; p++) {
        int P=primes[p];
        if(digiNum(P)>D) {
            break;
        }
        bool tgood = true;
        for (int i=0; i<K; i++) {
            if( S[i] >= P ) {
                tgood = false;
            }
        }
        if(!tgood) {
            continue;
        }
        for (int A=0; A<P; A++) {
            //for (int B=0; B<P; B++) {
                bool good = true;
                
                int s1 = (S[0]*A) % P;
                int B = 0;
                if( K>=2 ) {
                    B = (S[1] - s1 + P) % P;
                    if( ! ( (S[0]*A + B) % P == S[1] ) ) {
                        cout<<endl<<S[0]<<", "<<S[1]<<", "<<A<<", ! "<<B<<" ; "<<P<<endl;
                    }
                
                    assert( (S[0]*A + B) % P == S[1] );
                    
                } else {
                    cout<<"I don't know."<<endl;
                    return;
                }
                for (int i=2; i<K; i++) {
                    if( (S[i-1]*A + B) % P != S[i] ) {
                        good = false;
                    }
                }
                if(good) {
                    //cout<<"{" << A<<" , "<<B<<"}";
                    int s = (S[K-1]*A + B) % P;
                    if( (next!=-1) && (s!=next) ) {
                        cout<<"I don't know."<<endl;
                        return;
                    } else {
                        next = s;
                    }
                }
            //}

        }
        
    }
    if(next==-1) {
        cout<<"I don't know."<<endl;
    } else {
        cout<<next<<endl;
    }
}

inline void init()
{
    pn = 0;
    fill(composite, composite+MAX_PRIME+1, false);
    for (int i=2; i<=MAX_PRIME; i++) {
        if(!composite[i]) {
            primes[pn++] = i;
            for (int j=i+i; j<=MAX_PRIME; j+=i) {
                composite[j] = true;
            }
        }
    }
}
//=========================================================
// I/O:
//
int main(int argc, const char* argv[])
{
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    if ( ( mode == 0 ) && ENABLE_MULTI_PROCESS )
    {
        string inputfile = ".input";
        system("cat > .input");
        /* I use a dual core CPU, so for long solutions I might use this
         multi-process thing, splitting the input in halves effectively
         halving execution time of slow solutions. But due to overhead it
         increases the time of fast solutions, so it is optional... */
        mode = 1;
        remove(".finished");
        cerr<<"--Multi process mode--"<<endl;
        //string inputfile = argv[2];
        string command = argv[0];
        command += " 2 < "+inputfile+" > .tem &";
        system(command.c_str());
        freopen(inputfile.c_str(),"r",stdin);
    }
    
    init();
    int TestCases;
    cin>>TestCases;

    for (int _i=1;_i<=TestCases;_i++)
    {
        /* read input goes here */
        cin >> D >> K;
        for (int i=0; i<K; i++) {
            cin >> S[i];
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            solve();
            
        }
        else if(mode!=2) break;
    }
    if(mode==2) system("echo done > .finished");
    else if(mode==1)
    {
        struct stat stFileInfo;
        while( stat(".finished",&stFileInfo)!=0);
        system("cat .tem");

    }
    return 0;
}
