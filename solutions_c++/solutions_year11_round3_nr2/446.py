#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back
#define VS vector<string>

long long t, C, N, L;
vector<long long> a;
vector<long long> b;
vector<long long> c;
set< pair<long long, long long> > usteda;

int main()
    {
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        c.clear(); a.clear(); b.clear();
        cin >> L >> t >> N >> C;
        a.resize(C); b.resize(N);
        c.pb(0);
        FOR(i,0,C)  cin >> a[i];
        FOR(i,0,N) 
            { 
            b[i] = a[i%C];
            c.pb( c.back() + b[i] );
            }
        long long sol = 2*c.back();
        //cout << sol << endl;
        long long maxust = 0;
        FOR(i,0,N) 
            FOR(j,0,N)
                {
                long long prvi = 0, drugi  = 0;
                if ( L >= 1 )
                {
                if ( t >= 2*c[i+1] );
                else 
                    { 
                    long long d = min( 2*b[i], 2*c[i+1] - t ); 
                    prvi = d/2;
                    }
                }
                if ( L >= 2 && ( j > i ))
                {
                if ( t - prvi  >= 2*c[j+1] )
                    drugi = 0;
                else
                    {
                    long long d = min( 2*b[j], 2*c[j+1] - t + prvi); 
                    drugi = d/2;
                    }
                }
                //cerr << i << " " << j << " " << prvi + drugi << endl;
                maxust = max( maxust, prvi+drugi);
                }
        sol -= maxust;
        printf("Case #%d: %d\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
