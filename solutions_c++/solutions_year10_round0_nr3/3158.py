#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
#include <stack>
#include <ctime>
using namespace std;

typedef long long LL;
#define FOR(i,n) for(int i=0;i<n;i++)
#define clr(s,x)   memset(s,x,sizeof(s))
#define INF 0xfffffff
#define NINF -0xfffffff
#define pi acos(-1.0)

int q[105000],head,tail;

int main()
{
	int t,i,j,r,n,k,p,cases=0,num;
	int sum,tmp;
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		clr(q,0);
		sum=0;head=0;tail=0;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&p);
			q[tail++]=p;
		}
		for(i=0;i<r;i++)
		{
			tmp=0;num=0;
			while(1)
			{
				p=q[head];
				if(tmp+p<=k){tmp+=p;q[tail++]=q[head];head++;num++;}
				else break;
				if(num==n)break;
			}
			sum+=tmp;
		}

		printf("Case #%d: %d\n",++cases,sum);
	}

	return 0;
}