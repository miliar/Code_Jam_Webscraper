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
int W, L;
int x[1000];
int y[1000];
int r[1000];

pair<int,int> ri[1000];

bool intersect(int px, int py, int i)
{
    for (int j=0; j<i; j++) {
        if ( (x[j] + r[ri[j].second] > px - r[ri[i].second])
            && (y[j] + r[ri[j].second] > py - r[ri[i].second])
        ) {
            return true;
        }
    }
    return false;
}

int gety(int px, int i)
{
    int loy = -1;
    int hiy = L;
    
    while (loy+1 < hiy) {
        int hay = loy + (hiy - loy)/2;
        if (intersect(px,hay,i)) {
            loy = hay;
        } else {
            hiy = hay;
        }
    }
    return hiy;

}

void solve() {
    W *= 2;
    L *= 2;
    for (int i=0; i<N; i++) {
        r[i] *= 2;
    }
    for (int i=0; i<N; i++) {
        ri[i] = make_pair(-r[i],i);
    }
    sort(ri, ri+N);
    x[0] = 0;
    y[0] = 0;
    for (int i=1; i<N; i++) {
        int lox = -1;
        int hix = W;
        int picky;
        while (lox+1 < hix) {
            int hax = lox + (hix - lox)/2;
            int py = gety(hax, i);
            if (intersect(hax, py, i)) {
                lox = hax;
            } else {
                hix = hax;
            }
        }
        int py = gety(hix, i);
        //cout << i<<" "<<hix<<", "<<py<<endl;
        assert(! intersect(hix, py, i) );
        x[i] = hix;
        y[i] = py;
        
    }
    for (int j=0; j<N; j++) {
        for (int i=0; i<N; i++) {
            if (ri[i].second == j) {
                cout << (x[i]/2) << "." << (x[i]%2)*5;
                cout << " ";
                cout << (y[i]/2) << "." << (y[i]%2)*5;
                if (j < N - 1) {
                    cout << " ";
                }

            }
     
        }
    }
    cout << endl;
}

inline void init(){
srand('v'*(int)'e'*'x');
}
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
        cin >> N >> W >> L;
        for (int i=0; i<N; i++) {
            cin >> r[i];
        }
        
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) ) {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            /* output result goes here */
            cout<<"Case #"<<_i<<": ";
            solve();            
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
