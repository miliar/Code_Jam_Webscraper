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
int id[MAX];

int opos[MAX], bpos[MAX], pos[MAX];

int main()
{
	#ifdef Local
		freopen("/home/wasi/Desktop/input.txt", "r", stdin);
		freopen("/home/wasi/Desktop/output.txt", "w", stdout);
	#endif

	int t, n;
	scanf("%d", &t);
	xrep(tcn, 1, t)
	{
	    scanf("%d", &n);
	    char tt[5];
	    int bu, no = 0, nb = 0;

	    rep(i,n)
	    {
	        scanf("%s %d", tt, &bu);
	        pos[i] = bu;
	        id[i] = tt[0] == 'O' ? 0 : 8;
	        if (id[i] == 0) opos[no++] = bu;
	        else bpos[nb++] = bu;
	    }
        int po = 1, pb = 1, cur = 0, co = 0, cb = 0, tm = 0;
        while (cur < n)
        {
            //cout << tm << " " << po << " " << pb << endl;
            bool ook = false, bok = false;
            if (co < no && opos[co] < po) po--, ook = true;
            if (co < no && opos[co] > po) po++, ook = true;
            if (cb < nb && bpos[cb] < pb) pb--, bok = true;
            if (cb < nb && bpos[cb] > pb) pb++, bok = true;

            if (!ook && po == pos[cur] && id[cur] == 0)
                cur++, co++;
            else if (!bok && pb == pos[cur] && id[cur] == 8)
                cur++, cb++;
            tm++;
        }
        printf("Case #%d: %d\n", tcn, tm);
	}

	return 0;
}
