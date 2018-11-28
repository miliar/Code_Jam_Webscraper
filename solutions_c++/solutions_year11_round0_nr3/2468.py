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

const int MAX = 1005;
int c[MAX];
int xf[MAX], xb[MAX];
int main()
{
	#ifdef Local
		freopen("/home/wasi/Desktop/input.txt", "r", stdin);
		freopen("/home/wasi/Desktop/output.txt", "w", stdout);
	#endif

	int tt, n;
	scanf("%d", &tt);
	xrep(tc,1,tt)
	{
	    int v = 0;
        scanf("%d", &n);
        rep(i,n) scanf("%d", &c[i]), v ^= c[i];

        printf("Case #%d: ", tc);
        if (v)
        {
            printf("NO\n");
            continue;
        }

        sort(c, c+n);

        rep(i,n)
        {
            if (i==0) xf[i] = c[i];
            else xf[i] = xf[i-1] ^ c[i];
            //cout << i <<" "<<xf[i] <<endl;
        }

        LL val = 0, ans = 0;
        int xb = 0;
        rrep(i,n-1,1)
        {
            val += c[i];
            xb ^= c[i];
            if (xf[i-1] == xb)
                ans = max(ans, val);
        }

        printf("%lld\n", ans);


	}

	return 0;
}
