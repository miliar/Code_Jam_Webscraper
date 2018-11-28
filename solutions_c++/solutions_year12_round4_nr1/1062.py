#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
#include<queue>
#include<map>
#include<set>

using namespace std;

#define LONG long long
#define INF 2123123123
#define EP 10e-9
#define PI 3.14159265


#define MAXN 10000

int test, n, f, d, pos[MAXN+5], swp;
pair<int,int> v[MAXN+5];

int main()
{
	int i, j, tc;
	
	freopen("2a.in","r",stdin);
	freopen("2a.out","w",stdout);
	
	scanf("%d", &test);
	for (tc = 1; tc <= test; tc++)
	{
		cout << "Case #" << tc << ": ";
		f = 0;
		memset(pos,0,sizeof(pos));
		
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%d %d", &v[i].first, &v[i].second);
		scanf("%d", &d);	
		
		sort(v,v+n);
		
		
		j = 1;
		for (i = 0; i < n; i++)
			{
				if (i == j) break;
				swp = min(v[i].first - pos[i], v[i].second);
				if (v[i].first + swp >= d) f = 1;
				while (j < n && v[j].first <= v[i].first + swp) { pos[j] = pos[i] + swp; ++j; }
			}
		
		if (f) puts("YES"); else puts("NO");
	}
}