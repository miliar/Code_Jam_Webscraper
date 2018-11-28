#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <vector>

#define ll long long int
#define clr(a) memset(a, 0, sizeof(a))
#define FOR(a, b) for(int a = 0; a < (b); a++)
#define iter(a) typeof(a.begin())
#define foreach(a, it) for(typeof(a.begin()) it = a.begin(); it != a.end(); it++)

using namespace std;

const long double EPS = 1e-8;
const int INF = 1000000001;
const int MAXN = 102;

char a[MAXN][MAXN];
int wns[MAXN], gs[MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];
double r[MAXN];

int main()
{
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("", "w", stderr);
	int T;
	scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        int n;
        scanf("%d", &n);
        FOR(i, n)
            FOR(j, n)
                scanf(" %c", &a[i][j]);
        FOR(i, n)
        {
            gs[i] = 0;
            wns[i] = 0;
            FOR(j, n)
            {
                if (a[i][j] != '.') gs[i]++;
                if (a[i][j] == '1') wns[i]++;
            }
        }
        FOR(i, n)
            wp[i] = ((double)wns[i]) / gs[i];

        FOR(i, n)
        {
            owp[i] = 0.0;
            FOR(j, n)
            {
                if (a[i][j] == '.') continue;
                if (a[i][j] == '1') owp[i] += ((double)wns[j]) / (gs[j] - 1);
                    else owp[i] += ((double)(wns[j] - 1)) / (gs[j] - 1);
            }
            owp[i] /= gs[i];
        }
        FOR(i, n)
        {
            oowp[i] = 0.0;
            FOR(j, n)
                if (a[i][j] != '.') oowp[i] += owp[j];
            oowp[i] /= gs[i];
        }
        FOR(i, n)
            r[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        printf("Case #%d:\n", t);
        FOR(i, n)
            printf("%.7lf\n", r[i]);
    }

	return 0;
}




