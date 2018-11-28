#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <functional>
#include <bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, p, k) for(int i = (p); i <= (k); ++i)
#define FOREACH(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)

#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)

struct vine
{
	int d, l;
};

int n, m;
vine V[100001];
int low[100001];

int main()
{
	int Z;
	scanf("%d", &Z);
	FOR(t, 1, Z)
	{
		scanf("%d", &n);
		FOR(i, 1, n) scanf("%d %d", &V[i].d, &V[i].l);
		scanf("%d", &m);
		
		low[1] = V[1].d;
		bool ans = 0;
		FOR(i, 1, n)
		{
			if(V[i].d + low[i] >= m)
			{
				ans = 1;
				break;
			}
			FOR(j, i + 1, n)
			{
				if(V[i].d + low[i] < V[j].d) break;
				low[j] = max(low[j], min(V[j].d - V[i].d, V[j].l));
			}
		}
		
		printf("Case #%d: ", t);
		if(ans) printf("YES\n");
		else printf("NO\n");
		FOR(i, 1, n) low[i] = 0;
	}
	return 0;
}
