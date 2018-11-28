using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )
#define rrep( i, a, b ) for( __typeof(b) i = ( a ); i >= ( b ); --i )
#define xrep( i, a, b ) _rep( i, a, b, 1 )

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

typedef vector <int> vi;
const int MAX = 105;
double WP[MAX], OWP[MAX], OOWP[MAX];
char g[MAX][MAX];

int main()
{
	#ifdef Local
		freopen("/home/wasi/Desktop/input.txt", "r", stdin);
		freopen("/home/wasi/Desktop/output.txt", "w", stdout);
	#endif

	int T, n;
	scanf("%d", &T);
	xrep(ncase, 1, T)
	{
	    printf("Case #%d:\n", ncase);
        scanf("%d", &n);
        rep(i,n) scanf("%s", g[i]);

        rep(i,n)
        {
            int w = 0, p = 0;
            rep(j,n) if (g[i][j] != '.')
            {
                p++;
                w += g[i][j] == '1';
            }
            WP[i] = (w * 1.0) / p;
            double owp = 0;
            int oppo = 0;
            rep(j,n) if (j != i)
            {
                if (g[i][j] == '.') continue;
                oppo++;
                p = w = 0;
                rep(k, n) if (k != i)
                {
                    if (g[j][k] == '.') continue;
                    p++;
                    w += g[j][k] == '1';
                }
                owp += (w*1.0)/p;
            }

            owp /= oppo;
            OWP[i] = owp;

        }


        rep(i,n)
        {
            int p = 0;
            OOWP[i] = 0;
            rep(j,n) if (g[i][j] != '.')
            {
                p++;
                OOWP[i] += OWP[j];
            }
            OOWP[i] /= p;
            printf("%.15lf\n", .25*WP[i] + .5*OWP[i] + .25*OOWP[i]);
        }
	}

	return 0;
}
