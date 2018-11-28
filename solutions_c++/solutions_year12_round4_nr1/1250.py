#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <vector>

#define PI pair<int, int>
#define MP make_pair

const double eps = 1e-10;
const int INF = (1<<30);

using namespace std;

queue<int> Q;
int vis[10010], pos[10010], len[10010], a[10010];

int main()
{
	freopen("A-large.out", "w", stdout);
	freopen("A-large.in", "r", stdin);

	int T, cases = 1;
	int i, j, k, t, n, x, y;

	scanf("%d", &T);
	while( T-- )
	{
		memset(vis, 0, sizeof(vis));

		scanf("%d", &n);
		for( i = 0; i < n; ++i )
			scanf("%d %d", &pos[i], &len[i]);
		scanf("%d", &pos[n]);
		len[n] = 1;

		Q.push(0);
		Q.push(pos[0]);
		a[0] = pos[0];

		while(!Q.empty())
		{
			x=Q.front(); Q.pop();
			y=Q.front(); Q.pop();

			if(a[x]!=y) 
				continue;

			for(i=x+1; i <= n && pos[i]-pos[x] <= y; i++)
			{
				if(vis[i] && min(len[i], pos[i]-pos[x])<=a[i]) 
					continue;
				vis[i] = 1; 
				a[i] = min(len[i], pos[i]-pos[x]);
				Q.push(i);
				Q.push(a[i]);
			}
		}

		if( vis[n] )
			printf("Case #%d: YES\n", cases++);
		else
			printf("Case #%d: NO\n", cases++);
	}

	return 0;
}