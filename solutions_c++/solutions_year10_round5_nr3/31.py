#include <stdio.h>
#include <map>
#include <queue>
using namespace std;
#define N 110
map <int, int> m;
queue <int> q;
int main()
{
	int i, j, n, t, ts, r;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		m.clear();
		for(scanf("%d", &n); n; n--)
		{
			scanf("%d%d", &i, &j);
			m[i]=j;
			if(j>1) q.push(i);
		}
		for(r=0; !q.empty(); )
		{
			i=q.front(); q.pop();
			if(m[i]<2) continue;
			r+=m[i]/2;
			m[i+1]+=m[i]/2;
			m[i-1]+=m[i]/2;
			if(m[i+1]>1) q.push(i+1);
			if(m[i-1]>1) q.push(i-1);
			m[i]=m[i]%2;
		}
		printf("Case #%d: %d\n", t+1, r);
	}
	return 0;
}