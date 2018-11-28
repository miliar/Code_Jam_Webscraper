#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
const int N = 10010;
struct point
{
	int d,len;
}a[N];
int dis[N];
int main()
{
	freopen("A-large(2).in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int p = 1; p <= t; p ++) {
		int n,m;
		scanf("%d",&n);
		for(int i = 1; i <= n; i ++)
			scanf("%d%d",&a[i].d,&a[i].len);
		scanf("%d",&m);
		int flag = 0;
		a[0].d = 0;
		a[0].len = 0;
		memset(dis,-1,sizeof(dis));
		dis[0] = 0;
		dis[1] = a[1].d;
		for(int i = 0; i <= n; i ++) {
			for(int j = i + 1; j <= n; j ++) {
			//	if(i == 0 && j != 1) continue;
				if(a[i].d + dis[i] < a[j].d) continue;
				else if(a[j].d - a[i].d > a[j].len) dis[j] = max(dis[j],a[j].len);
				else dis[j] = max(dis[j],a[j].d - a[i].d);
			}
		}
		for(int i = 1; i <= n; i ++)
			if(dis[i] + a[i].d >= m) flag = 1;
		printf("Case #%d: ",p);
		if(flag) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}

