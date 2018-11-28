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

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
const bool ENABLE_MULTI_PROCESS = false;
using namespace std;

//=========================================================
// program:
//
int N;
int C[1000];
const int INF = 2000000000;


int solve() {
    int x= 0;
    for (int i=0; i<N; i++) {
        x ^= C[i];
    }
    if ( x == 0) {
        //return accumulate(C,C+N,0) - *min_element(C,C+N);
        int sum = 0;
        for (int i=0; i<N; i++) {
            sum += C[i];
        }
        return   sum - *min_element(C,C+N);
    } else {
        return -1;
    }
    
}

inline void init(){}
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
        cin >> N;
        for (int i=0; i<N; i++) {
            cin >> C[i];
        }
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            int x = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            if ( x==-1) {
                cout<<"NO";
            } else {
                cout<<x;
            }
            cout<<endl;
            
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
