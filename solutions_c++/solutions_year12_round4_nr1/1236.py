#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

typedef pair<int,int> pii;

int n;
pii data[10100];
bool visited[10100];

int main()
{
	freopen("A-large.out","w",stdout);
	freopen("A-large.in","r",stdin);
	int t;
	scanf("%d",&t);
	FOR(ca,1,t)
	{
		scanf("%d",&n);
		FOR(i,0,n-1) scanf("%d %d",&data[i].first,&data[i].second);
		int target;
		scanf("%d",&target);
		bool ans = false;
		memset(visited,false,sizeof(visited));
		queue<pii> q;
		q.push(pii(0,data[0].first));
		while(!q.empty())
		{
			pii front = q.front(); q.pop();
			int pos = front.first;
			int l = front.second;
			if(data[pos].first + l >= target) 
			{
				ans = true; 
				break;
			}
			FOR(i,pos+1,n-1)
			{
				int jarak = data[i].first - data[pos].first;
				if(jarak > l) continue;
				if(visited[i]) continue;
				int l2 = min(jarak,data[i].second);
				visited[i] = true;
				q.push(pii(i,l2));
			}
		}
		printf("Case #%d: %s\n",ca,(ans)?"YES":"NO");
	}
    return 0;
}
