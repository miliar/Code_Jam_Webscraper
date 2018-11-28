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
char Games[101][101];

double TeamRank[100];

bool   WP_done[101][101];
double WP[101][101];

double teamWP(int x, int y) {
    if ( ! WP_done[x][y+1] ) {
        WP_done[x][y+1] = true;
        double t = 0, g = 0;
        for (int i=0; i<N; i++) {
            if ( i != y ) {
                if ( Games[x][i] != '.' ) {
                    t ++;
                }
                if ( Games[x][i] == '1' ) {
                    g ++;
                }
            }
        }
        WP[x][y+1] = g/t;
    }
    return WP[x][y+1];
}

bool   OWP_done[101];
double OWP[101];

double teamOWP(int x) {
    double & res = OWP[x];
    if(! OWP_done[x] ) {
        OWP_done[x] = true;
        int t = 0;
        res = 0;
        for (int i=0; i<N; i++) {
            if ( Games[x][i] != '.' ) {
                res += teamWP(i, x);
                t ++;
            }
        }
        res /= t;
    }
    return res;
}

bool   OOWP_done[101];
double OOWP[101];


double teamOOWP(int x) {
    double & res = OOWP[x];
    if(! OOWP_done[x] ) {
        OOWP_done[x] = true;
        int t = 0;
        res = 0;
        for (int i=0; i<N; i++) {
            if ( Games[x][i] != '.' ) {
                res += teamOWP(i);
                t ++;
            }
        }
        res /= t;
    }
    return res;
    
}


void solve() {
    memset(WP_done, 0, sizeof(WP_done));
    memset(OWP_done, 0, sizeof(OWP_done));
    memset(OOWP_done, 0, sizeof(OOWP_done));
    for (int i=0; i<N; i++) {
        TeamRank[i] = 0.25 * teamWP(i,-1) + 0.50 * teamOWP(i) + 0.25 * teamOOWP(i);
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
            for (int j=0; j<N; j++) {
                cin >> Games[i][j];
            }
        }
        
        if( (mode==0) || ( (mode!=2)== (_i*2<=TestCases) ) )
        {            
            cerr<<"["<<_i<<" / "<<TestCases<<"]"<<endl;
            /* program call goes here */
            solve();
            /* output result goes here */
            cout<<"Case #"<<_i<<":"<<endl;
            for (int i=0; i<N; i++) {
                cout.precision(12);
                cout<<TeamRank[i]<<endl;
            }
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
