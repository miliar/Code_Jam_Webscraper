#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n;

struct node
{
	int x,y;
}no[1010];

int cmp(const void *a,const void *b)
{
	if(((node *)a)->x<((node *)b)->x)
		return -1;
	else
		return 1;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,ca;
	scanf("%d",&T);
	ca=1;
	while(T--)
	{
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&no[i].x,&no[i].y);
		}
		qsort(no,n,sizeof(no[0]),cmp);
		int sign[1010];
		memset(sign,0,sizeof(sign));
		int q;
		int ans=0;
		for(i=0;i<n;i++)
		{
//			sign[i]=1;
			for(q=i+1;q<n;q++)
			{
				if(no[i].y>no[q].y/*&&sign[q]==0*/)
					ans++;
			}
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}