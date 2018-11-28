#include <stdio.h>
#include <string.h>

int n;

struct p
{
	int x,y;
}xx[1100];

int f(int a,int b)
{
	if(xx[a].x>xx[b].x && xx[a].y<xx[b].y)
	return 1;
	if(xx[a].x<xx[b].x && xx[a].y>xx[b].y)
	return 1;
	return 0;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j,t,res,k;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		res=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		scanf("%d%d",&xx[i].x,&xx[i].y);
		for(i=0;i<n-1;i++)
		{
			for(k=i+1;k<n;k++)
			{
				if(f(i,k))
				res++;
			}
		}
		printf("Case #%d: %d\n",j,res);
	}
	return 0;
}
