#ifdef VX_PRECOMPILED
#include "precomp.h"
typedef mpz_class big;
#else
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
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
// http://gmplib.org/ (uncomment if solution does not use big nums)
#include "gmpxx.h"
#define big mpz_class
#endif

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
typedef long long int64;
#define long int64
const bool ENABLE_MULTI_PROCESS = true;
using namespace std;

//=========================================================
// program:
//
int N;
int d[10001];
int l[10001];
int D;

int maxlen[10002];

bool solve() {
    d[N] = D;
    l[N] = 0;
    for (int i=0; i<=N; i++) {
        maxlen[i] = -1;
    }
    maxlen[0] = d[0];
    for (int i=0; i<N; i++) {
        if (maxlen[i] > -1) {
            for (int j=i+1; j<=N; j++) {
                if (d[j] - d[i] <= maxlen[i]) {
                    maxlen[j] = std::max( maxlen[j], std::min(d[j] - d[i], l[j]) );
                } else {
                    break;
                }
            }
        }
    }
    return (maxlen[N] > -1);
}

inline void init(){}
//=========================================================
// I/O:
//
void run(const char* x)
{
    int r = system(x);
    cerr<<x<<" "<<"("<<r<<")"<<endl;
}
int main(int argc, const char* argv[])
{
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    if ( ( mode == 0 ) && ENABLE_MULTI_PROCESS )
    {
        string inputfile = ".input";
        run("cat > .input");
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
        run(command.c_str());
        assert( freopen(inputfile.c_str(),"r",stdin) );
    }
    
    init();
    int TestCases;
    cin>>TestCases;

    for (int _i=1;_i<=TestCases;_i++) {
        /* read input goes here */
        cin >> N;
        for (int i=0; i<N; i++) {
            cin >> d[i] >> l[i];
        }
        cin >> D;
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) ) {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            bool res = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": "<<(res?"YES": "NO")<<endl;            
        }
        else if(mode!=2) break;
        
        assert(cin);
    }
    if(mode==2) {
        run("echo done > .finished");
    } else if(mode==1) {
        struct stat stFileInfo;
        while( stat(".finished",&stFileInfo)!=0);
        run("cat .tem");
    }
    return 0;
}
