#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <map>
#include <set>
#define maxn 1111
#define maxm 21111111

#define INP "A.in"
#define OUP "A.out"

using namespace std;

struct edge_type
{
	int x,y,next;
};

int n,m,total;
edge_type g[maxn + 1];
int first[maxn + 1];

int f[maxn + 1];

void add_edge(int x,int y)
{
	g[++total].x = x; g[total].y = y;
	g[total].next = first[x]; first[x] = total;
}

int head,tail;
int q[maxm*2 + 1];
bool mark[maxn + 1];

bool bfs(int x)
{
	head = tail = 1;
	q[head] = x;
	memset(f,0,sizeof(f));
	memset(mark,0,sizeof(mark));
	f[x] = 1;
	while (head<=tail){
		int cur = q[head];
		for (int i=first[cur];i;i=g[i].next){
			int y = g[i].y;
			f[y] += f[x];
			if (f[y]>1)
				return true;
			if (!mark[y]){
				mark[y] = 1;
				q[++tail] = y;
			}
		}
		head ++;
	}
	return false;
}

int main()
{
	freopen(INP,"r",stdin);
	freopen(OUP,"w",stdout);
	int tc;
	scanf("%d",&tc);
	for (int tt=1;tt<=tc;tt++){
		scanf("%d",&n);
		total = 0;
		memset(first,0,sizeof(first));
		for (int i=1;i<=n;i++){
			int tmp;
			scanf("%d",&tmp);
			for (int j=1;j<=tmp;j++){
				int tt;
				scanf("%d",&tt);
				add_edge(i,tt);
			}
		}
		bool flag = 0;
		for (int i=1;i<=n;i++){
			if (bfs(i)){
				flag = 1;
				break;
			}
		}
		printf("Case #%d: ",tt);
		if (flag)
			printf("Yes\n");
		else
			printf("No\n");
	}
	return 0;
}
