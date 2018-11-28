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
int C, D;
int P[100];
int V[100];

double solve() {
    D *= 2;
    
    int vendors[100];
    int n = 0;
    for (int i=0; i<C; i++) {
        for (int j=0; j<V[i]; j++) {
            vendors[n++] = P[i]*2;
        }
    }
    int minim = vendors[0];
    for (int i=0; i<n; i++) {
        vendors[i] = vendors[i] - minim + 2000;
    }
    int maxlim = vendors[n-1] + 2002;
    /*cout<<0<<" ";
    for (int i=0; i<n; i++) {
        cout<<vendors[i]<<" ";
    }
    cout<<maxlim<<endl;*/
    
    
    int* dp = new int[maxlim*(n+1)];
    const int INF = 2000000000;
    for (int x = maxlim-1; x >= 0; x--) {
        dp[ x*(n+1) + n ] = 0;
        for (int i = 0; i< n; i++) {
            dp[x*(n+1) + i] = INF;
            if ( x < maxlim-1 ) {
                dp[x*(n+1) + i] = dp[(x+1)*(n+1) + i]; 
            }
            int movecost = abs( vendors[i] - x );
            int nx = x + D;
            if (nx < maxlim) {
                int & res = dp[x*(n+1) + i];
                int cst = std::max(dp[nx*(n+1) + (i+1) ], movecost);
                if ( res > cst ) {
                    res = cst;
                }
            }
        }
    }
    
    //int res = dp[0];
    int res = dp[0*(n+1)+0];
    
    delete[] dp;
    return res * 0.5;
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
        cin >> C >> D;
        for (int i=0; i<C; i++) {
            cin >> P[i] >> V[i];
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            double x = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            cout.precision(18);
            cout<<x<<endl;            
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
