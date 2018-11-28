#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <string>

#define REP(i,n) for(int i=0; i<n; i++)
#define REPD(i,n) for(int i=(n-1); i>=0; i--)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i, a,b) for(int i=a; i>=b; i--)
#define FILL(a, v) memset(&a, v, sizeof(a))
#define DB(x) cout << #x << " : " << x << endl
#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;

const int MAXN = 1001;

int T, n, a[MAXN];
double ans;

int main()
{
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	FOR(Tn, 1, T)
	{
		printf("Case #%d: ", Tn);
		scanf("%d", &n);
		ans = 0.0;
		REP(i, n)
		{
			scanf("%d", &a[i]); a[i]--;
			if (a[i] != i) ans++;
		}
		printf("%.6lf\n", ans);
	}
	return 0;
}
