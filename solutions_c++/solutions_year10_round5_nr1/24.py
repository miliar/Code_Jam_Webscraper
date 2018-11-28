#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int p[1000001];
int P;

int ppow(int x, int p)
{
    if (p==0)
        return 1;
    if (p==1)
        return x;
    long long v = ppow(x, p/2);
    v = v*v;
    if (p&1)
        v *= x;
    return v % P;
}

int main()
{
    memset (p, 0, sizeof (p));

    FOR (i, 2, 1000001)
        if (!p[i])
        {
            p[i] = 1;

            for (int j = i+i; j<1000001; j+=i)
                p[j] = 1;
        }
        else
            p[i] = 0;


	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

    int t;
    cin >> t;
    REP (tt, t)
    {
        cout << "Case #" << (tt+1) << ": ";

        int d, k;

        cin >> d >> k;

        int M = 1;
        REP (i, d)
            M *= 10;

        VI r;


        VI a(k);
        REP(i, k)
            cin >> a[i];

        int mi = 0;
        REP (i, k)
            mi = max (mi, a[i]+1);

        if (k == 1)
        {
            r.pb (0);
            r.pb (1);
        }
        else if (a[k-1] == a[k-2])
        {
            r.pb (a[k-1]);
        }
        else if (k==2)
        {
            r.pb (0);
            r.pb (1);
        }
        else {
            FOR (pp, mi, M)
            if (p[pp])
            {
                P = pp;

                long long v1 = a[1]-a[0];
                long long v2 = a[2]-a[1];

                if (v1<0)
                    v1 += P;
                if (v2<0)
                    v2 += P;

                long long A = v2*ppow(v1, P-2)%P;
                long long B = (a[1] - A*a[0])%P;

                if (B<0)
                    B+= P;

                bool ok = true;
                REP (i, k-1)
                {
                    if ((A * a[i] + B)  % P != a[i+1])
                    {
                        ok = false;
                        break;
                    }
                }

                if (ok)
                    r.pb ((a.back()*A + B)%P);
            }
        }
        UNIQUE(r);
        if (r.size ()>1)
            cout << "I don't know." << endl;
        else
            cout << r.back() << endl;
    }

	return 0;
}
