#include<numeric>
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
const bool ENABLE_MULTI_PROCESS = true;
using namespace std;

//=========================================================
// program:
//
int X,S,R,t,N;
int B[1000000], E[1000000], w[1000000];
int L[1000001];
double T[1000001];

double solve() {
    //Always run from the beginning until the time ends.
    double best = 1e100;
    int nowlen = X;
    for (int i=0; i<N; i++) {
        L[i] = (E[i]-B[i]);
        w[i] += S;
        T[i] = L[i]/(double)(w[i]);
        nowlen -= L[i];
    }
    L[N] = nowlen;
    w[N] = S;
    T[N++] = L[N]/(double)(w[N]);
    
    bool modified[N];
    fill(modified, modified+N, false);
    double tt = t;
    while (tt > 0) {
        pair<double, int > pick = make_pair<double,int>(-1.0,-1); 
        for (int i=0; i<N; i++) {
            if (! modified[i]) {
                double ns = w[i] + R - S;
                if ( L[i] / ns <= tt ) {
                    double uset = L[i] / ns;
                    double dec = T[i] - L[i] / ns;
                    pick = std::max(pick, make_pair<double,int>(dec/uset,i) );
                } else {
                    double x = tt * ns;
                    double uset = tt;
                    double dec = T[i] - (tt + (L[i]-x) / w[i] );
                    pick = std::max(pick, make_pair<double,int>(dec/uset,i) );
                }
            }

        }
        if( pick.second == -1) {
            break;
        }
        int i = pick.second;
        double ns = w[i] + R - S;
        modified[i] = true;
        if ( L[i] / ns <= tt ) {
            double uset = L[i] / ns;
            double dec = T[i] - L[i] / ns;
            T[i] -= dec;
            tt -= uset;
        } else {
            double x = tt * ns;
            double uset = tt;
            double dec = T[i] - (tt + (L[i]-x) / w[i] );
            tt -= uset;
            T[i] -= dec;
        }
        
        
    }
    return accumulate(T, T+N, 0.0);
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
        cin >> X >> S >> R >> t >> N;
        for (int i=0; i<N; i++) {
            cin >> B[i] >> E[i] >> w[i];
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            double mint = solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            cout.precision(13);
            cout<<mint<<endl;;            
        }
        else if(mode!=2) break;
        
        assert(cin);
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
