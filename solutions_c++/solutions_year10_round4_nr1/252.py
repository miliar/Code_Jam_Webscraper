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
const bool ENABLE_MULTI_PROCESS = false;
using namespace std;

//=========================================================
// program:
//
int N;
int A[50][50];
int B[1000][1000];

void cp(int x, int y, int K) {
    for (int i=0; i<K; i++) {
        for (int j=0; j<K; j++) {
            B[i][j] = -1;
        }
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            B[i+x][j+y] = A[i][j];
        }
    }
}

bool cmp(int a, int b, int c, int d) {
    return ( (B[a][b] == -1) || (B[c][d] == -1) || (B[a][b] == B[c][d]) );
}

bool isSym(int K) {
    for (int i=0; i<K; i++) {
        for (int j=0; j<K; j++) {
            if( ! cmp(i,j, j,i ) ) {
                return false;
            }
            if( ! cmp(i,j, K-j-1, K-i-1 ) ) {
                return false;
            }

        }
    }
    return true;
    
}


int solve() {
    for (int K=N; K<=3*N+1; K++) {
        for (int i=0; i+N<=K; i++) {
            for (int j=0; j+N<=K; j++) {
                cp(i,j,K);
                if(isSym(K) ) {
                    return K*K-N*N;
                }
            }
        }
    }
    
    assert(false);
    return -1;
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

        cin >> N;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                A[i][j] = -1;
            }
        }

        int r = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<i+1; j++) {
                cin >> A[j][N-i-1+j];
                r++;
            }
        }
        for (int i=1; i<N; i++) {
            for (int j=0; i+j<N; j++) {
                cin >> A[i+j][j];
                r++;
            }           
        }
        //cout<<"Read "<<r<<endl;
        /* read input goes here */
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            int x = solve();
            
            /* output result goes here */
            cout<<"Case #"<<_i<<": "<<x<<endl;            
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
