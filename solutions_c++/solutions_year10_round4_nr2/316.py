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
int P;
int M[1024];
int matches[10][1024];

long long mem[11][1024][11];
const int INF = 200000000;

long long rec(int level, int a, int b, int c, int add) {
    long long & res = mem[level][a][add];
    // only one return!
    if( res==-1) {
        if(level == P) {
            //verify:
            bool good = true;
            for (int i=a; i<b; i++) {
                if( M[i]+add < P ) {
                    good = false;
                }
            }
            if( good) {
                res = 0;
            } else {
                res = INF;
            }
            
        } else {
            res = INF;
            //buy this:
            int cut = a+(b-a)/2;
            res = std::min(res, matches[P-level-1][c] + rec(level+1, a,cut, c*2, add+1)+rec(level+1, cut,b, c*2+1, add+1) );
            //don't buy this:
            res = std::min(res, rec(level+1, a,cut, c*2, add)+rec(level+1, cut, b, c*2+1, add) );
        }
        
    }
    return res;
}

long long solve() {
    memset(mem,-1,sizeof(mem));
    return rec(0, 0, 1<<P, 0, 0);
    
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
        cin >> P;
        for (int i=0; i<(1<<P); i++) {
            cin >> M[i];
        }
        int p = P-1;
        for (int i=0; i<P; i++) {
            for (int j=0; j<(1<<p); j++) {
                cin >> matches[i][j];
            }
            p--;
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            int cost = solve();
            
            /* output result goes here */
            cout<<"Case #"<<_i<<": "<<cost<<endl;            
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
