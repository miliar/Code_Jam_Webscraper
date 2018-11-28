#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define VI vector<int>
#define pb push_back
#define VS vector<string>
#define mp make_pair

int W, L, U, G;

VI dx, dy, gx, gy;

double gornji( double x )
    {
    double sol = 0;
    FOR( i, 1, gx.size() ) 
        {
        if ( gx[i] <= x ) 
            sol += ( gx[i] - gx[i-1] )*(gy[i-1] + gy[i])/2.0;
        else
            {
            double y =  gy[i-1] + ((double)((x-gx[i-1])*(gy[i] - gy[i-1])))/(gx[i] - gx[i-1]);
            sol += ( x - gx[i-1] )*(gy[i-1] + y)/2.0;
            break;
            }
        }
    return sol;
    }
double donji( double x )
    {
    double sol = 0;
    FOR( i, 1, dx.size() ) 
        {
        if ( dx[i] <= x ) 
            sol += ( dx[i] - dx[i-1] )*(dy[i-1] + dy[i])/2.0;
        else
            {
            double y = dy[i-1] + ((double)((x-dx[i-1])*(dy[i] - dy[i-1])))/(dx[i] - dx[i-1]);
            sol += ( x - dx[i-1] )*(dy[i-1] + y)/2.0;
            break;
            }
        }
    return sol;
    }

int main()
    {
    int TC;
    cin >> TC;
    FOR(tc, 0, TC)
        {
        cin >> W >> L>> U >> G;
        dx.clear(); dy.clear();
        gx.clear(); gy.clear();
        dx.resize( L ); dy.resize( L );
        gx.resize(U ); gy.resize( U );
        FOR( i, 0, L ) 
            cin >> dx[i] >> dy[i];
        FOR( i,0 , U ) 
            cin >> gx[i] >> gy[i];

        printf("Case #%d:\n",tc+1);

        double P = gornji(W) - donji(W);
        FOR( i,1,G )
            {
            double mn = 0;
            double mx = W;
            double Pi = (P*i)/G;
            while( (mx - mn) > 1e-8)
                {
                double mid = (mx + mn ) /2;
                double P2 = gornji(mid)-donji(mid);
                if( Pi < P2 ) 
                    mx = mid;
                else mn = mid;
                }
            //cout << Pi << endl;
            printf("%lf\n",mx);
            }

        }
    return 0;
    }
