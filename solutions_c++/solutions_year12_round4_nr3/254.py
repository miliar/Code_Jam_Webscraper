#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <iomanip>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long LL;
typedef long double ldb;

const int INF = (1 << 30) - 1;
const ldb EPS = 1e-9;
const ldb PI = fabs(atan2(0.0, -1.0));
const int MAXN = 2005;
const int MAXY = 100000000;

int n;
int nxt[MAXN];
void load()
{
	scanf("%d", &n);
	for (int i = 1; i < n; i++)
		scanf("%d", &nxt[i]);
}

int y[MAXN];
void solve(int test)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = i + 1; j < nxt[i]; j++)
			if (nxt[j] > nxt[i])
			{
				printf("Case #%d: Impossible\n", test);
				return;
			}
	}
	for (int i = 1; i <= n; i++)
		y[i] = rand();
	while (true)
	{
		bool ok = true;
		for (int i = 1; ok && i < n; i++)
		{
			for (int j = i + 1; ok && j <= n; j++)
			{
				double ny = y[i] + ((double)(y[nxt[i]] - y[i]) / (nxt[i] - i)) * (j - i);
				if (j < nxt[i] && !(y[j] + EPS < ny))
				{
					ok = false;
					break;
				}
				if (j >= nxt[i] && !(y[j] - EPS <= ny))
				{
					ok = false;
					break;
				}
			}
		}

		if (ok) break;
		for (int i = 1; i < n; i++)
		{
			int mx = y[nxt[i]];
			for (int j = i + 1; j <= n; j++)
			{
				double cmx = ((double)(y[j] - y[i]) / (j - i)) * (nxt[i] - i) + y[i];
				mx = max((int)ceil(cmx) + 1, mx);
				if (mx > y[nxt[i]]) y[nxt[i]] = mx;
			}
			y[nxt[i]] = mx;
		}
	}
	printf("Case #%d:", test);
	for (int i = 1; i <= n; i++)
		printf(" %d", y[i]);
	printf("\n");	
}

int main()
{
	srand(33034);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		cerr << test << endl;
		load();
		solve(test);
	}	
	return 0;
}
