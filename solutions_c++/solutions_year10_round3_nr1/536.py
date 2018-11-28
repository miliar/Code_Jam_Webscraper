#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
typedef long long lld;
using namespace std;
#define clr(NAME,VALUE) memset(NAME,VALUE,sizeof(NAME))
#define MAX 0x7f7f7f7f
#define N 1010
struct node
{
	int a,b;
}q[N];
bool cmp(node a,node b)
{
	return a.a<b.a;
}
int n;
int main()
{
    freopen("A-small-attempt0(2).in","r",stdin);
    freopen("a111.out","w",stdout);
	int T,csn=1;
	scanf("%d",&T);
	int ans;
	while(T--)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&q[i].a,&q[i].b);
		}
		sort(q,q+n,cmp);
		ans=0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if(q[j].b<q[i].b)
				{
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n",csn++,ans);
	}
//	#ifndef ONLINE_JUDGE
//    while(1);
//	#endif
	return 0;
}

