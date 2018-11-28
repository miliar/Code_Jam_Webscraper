#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

ifstream in("in.txt");
//ofstream out("out.txt");
FILE *out=fopen("out.txt","w");

struct WW {
    double b, e, w;
    WW (double ta, double tb, double tc) {
        b =ta; e=tb; w=tc;
    }
    bool operator<(const WW &foo) const {
        return b < foo.b;
    }
};

typedef long long LL;
const int dx[4]={0,1,0,1}, dy[4]={0,0,1,1};
const double EPS = 1E-6;
bool comp(  WW a,  WW b ) {
    return a.w < b.w;
}


int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        double X, S, R, t;
        int N;
        vector<WW> walk, walkS;
        in >> X >> S >> R >> t >> N;
        for( int i=0; i<N; i++ ) {
            double B, E, W;
            in >> B >> E >> W;
            walk.push_back( WW(B,E,W+S) );
        }
        sort( walk.begin(), walk.end() );
        for( int i=0; i<N; i++ ) {
            if( i==0 ) {
                if( walk[i].b == 0 ) continue;
                else walk.push_back( WW(0,walk[i].b,S) );
            }
            else {
                if( walk[i].b - walk[i-1].e > 0 ) {
                    walk.push_back( WW(walk[i-1].e,walk[i].b,S) );
                }
            }
        }
        if( walk[N-1].e < X ) walk.push_back( WW(walk[N-1].e, X,S) ); //end
        walkS = walk;
        sort( walkS.begin(), walkS.end(), comp );
        cout << walkS[0].w << endl;
        double ans = 0.0;
        R -= S;
        for( int i=0; i<walkS.size(); i++ ) {
            if( t > 0 ) {
                //try and run
                //cout << "run:" << walkS[i].b << " to " << walkS[i].e << endl;
                double run = min(t, (walkS[i].e-walkS[i].b)/(R+walkS[i].w));
                //if( !( fabs( run*(R+walkS[i].w) - (walkS[i].e-walkS[i].b) ) < EPS ) ) {
                if( fabs( run - t ) < EPS ) {
                    //not run entire length
                    ans += ( (walkS[i].e-walkS[i].b) -( run*(R+walkS[i].w) ) )/walkS[i].w;
                }
                ans += run;
                t -= run;
            }
            else {
                ans += (walkS[i].e-walkS[i].b)/walkS[i].w;
            }
        }

        fprintf(out,"Case #%d: %.7lf\n",test,ans);
        //out << "Case #" << test << ":" << ans << endl;

    }

    return 0;
}



