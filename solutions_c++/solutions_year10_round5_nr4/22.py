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

#define mod 1000000007

long long r[80*80][80];
int res[64][80][80][2];
long long f[80][80];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

    int t;
    cin >> t;

    memset(f, 0, sizeof (f));

    REP (i, 80)
        REP (j, 80)
        {
            f[i][j] = 1;
            int x = i;
            REP(k, j)
            {
                f[i][j] *= x;
                f[i][j] %= mod;
                x--;
            }
        }

    REP (tt, t)
    {
        cout << "Case #" << (tt+1) << ": ";

        long long n;
        int b;
        cin >> n >> b;

         memset (r, 0, sizeof (r));

        r[0][0] = 1;

        FOR (i, 1, b)
            FORD(j, b*b-i-1, 0)
                REP (k, b)
                {
                    r[i+j][k+1] += r[j][k];
                    r[i+j][k+1] %= mod;
                }

        REP (i, b*b-1)
            REP (k, b)
            {
                //cout << i << " " << k << " " << r[i][k] << endl;
            }

        memset(res, 0, sizeof(res));

        res[0][b][0][0] = 1;

        VI a;
        while (n)
        {
            a.pb (n%b);
            n/=b;
        }

        REP (i, a.size ())
        {
            REP(j, b+1)
                REP (k, b)
                    REP (l, 2)
                        if (res[i][j][k][l])
                        {
                            int add = a[i] - k;
                            if (add < 0)
                                add += b;

                           //
                           // cout << i << " " << j << " " << k << " " << l << " " << add  << " " << res[i][j][k][l]<< endl;

                            while (add <= b*(b-1)/2)
                            {
                                REP (adc,j+1)
                                {
                                    if (!adc && l)
                                        continue;

                                    long long v = res[i][j][k][l] * r[add][adc] % mod;
                                    if (i)
                                        {
                                            if (l)
                                                v = v * adc % mod * f[j-1][adc-1] % mod;
                                            else
                                                v = v * f[j][adc] % mod;
                                        }

                                    res[i+1][adc][(k+add) / b][0] += v;
                                    res[i+1][adc][(k+add) / b][0] %= mod;
                                    //if (v)cout << "to " << i+1 << " " << adc <<  " " << add / b << endl;

                                    if (adc)
                                    {
                                        v = res[i][j][k][l] * r[add][adc-1] % mod;
                                        if (i)
                                        {
                                            if (l)
                                                v = v * adc % mod * f[j-1][adc-1] % mod;
                                            else
                                                v = v * f[j][adc] % mod;
                                        }
                                        res[i+1][adc][(k+add) / b][1] += v;
                                        res[i+1][adc][(k+add) / b][1] %= mod;
                                    }
                                }
                                add += b;
                            }
                        }
        }

        int rr = 0;

        REP (i, b+1)
        {
            rr += res[a.size()][i][0][0];
            rr %= mod;
        }

        cout  << rr << endl;
    }

	return 0;
}
