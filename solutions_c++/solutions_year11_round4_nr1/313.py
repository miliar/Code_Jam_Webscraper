#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back
#define VS vector<string>

int L;
double T;
int S,R;
int N;

VI B;
VI E;
VI sp;

int main()
    {
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        cin >> L >> S >> R >> T >> N;
        B.resize(N);
        E.resize(N);
        sp.resize(N);
        FOR(i,0,N) cin >> B[i] >> E[i] >> sp[i];

        if ( R < S ) 
            { T = 0; }

        FOR(i,0,N)
            FOR(j,i+1,N)
                if ( B[j] < B[i] )
                    {
                    swap(B[i],B[j]); swap(E[i],E[j]); swap(sp[i],sp[j]);
                    }
        
        vector< pair<int,int> > dio;

        if ( B[0] > 0 ) dio.pb(make_pair(  0,B[0] ));
        FOR( i, 0, N-1)
            {
            dio.pb( make_pair( sp[i], E[i] - B[i] ));
            if ( B[i + 1] > E[i] )
                dio.pb( make_pair(  0, B[i+1] - E[i] ) );
            }
        dio.pb( make_pair(sp[N-1], E[N-1] - B[N-1]));
        if ( E[N-1] < L ) dio.pb(make_pair( 0, L - E[N-1]));

        sort( dio.begin(),dio.end());

        double sol = 0;

        FOR( i, 0 , dio.size() )
            {
            double v = dio[i].first;
            double l  = dio[i].second;
            if ( T > 0 )
            {
            v += S;
            double t1 = l / v;
            double t2 = l / ( v - S + R );
            if ( t2 >= T )
                {
                double d = l - T*(v-S+R);
                sol += T;
                T = 0;
                sol += d / v;
                }
            else 
                {
                
                sol += t2;
                T-=t2;
                }
            }
            else 
            {
            v += S;
            double t1 = l / v;
            sol += t1;
            }
            }
        
        printf("Case #%d: %lf\n",tc+1,sol);
        }
    //system("pause");
    return 0;
    }
