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

char c[101];
int a[101];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("", "w", stderr);
	int t;
	scanf("%d", &t);
	for(int i0 = 1; i0 <= t; ++i0)
	{
		int n;
		scanf("%d", &n);
		FOR(i, n)
			scanf(" %c%d", &c[i], &a[i]);
		int po = 0;
		int pb = 0;
		while (po < n && c[po] != 'O') po++;
		while (pb < n && c[pb] != 'B') pb++;
		int o = 1;
		int b = 1;
		int T = 0;
		while (po < n || pb < n)
		{
			bool ind = false;
			if (po < n)
				if (o != a[po])
					if (o < a[po]) o++;
						else o--;
				else
					if (po < pb)
					{
						ind = true;
						po++;
						while (po < n && c[po] != 'O') po++;
					}
			if (pb < n)
				if (b != a[pb])
					if (b < a[pb]) b++;
						else b--;
				else
					if (pb < po && !ind)
					{
						pb++;
						while (pb < n && c[pb] != 'B') pb++;
					}
			T++;
		}
		printf("Case #%d: %d\n", i0, T);
	}

	return 0;
}




