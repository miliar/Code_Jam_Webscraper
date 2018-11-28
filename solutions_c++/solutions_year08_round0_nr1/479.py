#include <stdio.h>
#include <string.h>

#define MAX 1100
#define MAXS 110

int pd[MAXS][MAX];
char sname[MAXS][MAXS];
char query[MAX][MAXS];

int solve(int s, int q)
{
	int i,j;
	int ret=0;
	int max;
	for(i=0;i<s;++i)
		for(j=0;j<=q;++j)
			pd[i][j]=q+1;
	for(i=0;i<s;++i)
	{
		for(j=q-1;j>=0;--j)
		{
			if(strcmp(sname[i],query[j]))
				pd[i][j]=pd[i][j+1];
			else
				pd[i][j]=j;
		}
	}
	for(i=0;i<q;++ret)
	{
		max=0;
		for(j=1;j<s;++j)
			if(pd[j][i]>pd[max][i])
				max=j;
		i=pd[max][i];
	}
	if(q==0)
		ret=1;
	return ret-1;
}

int main()
{
	int casecnt;
	int cnt;
	int s,q;
	int i;
	scanf("%d",&casecnt);
	for(cnt=1;cnt<=casecnt;++cnt)
	{
		scanf("%d",&s);
		scanf("%*[^\n]");
		scanf("%*c");
		for(i=0;i<s;++i)
		{
			scanf("%[^\n]%*c",sname[i]);
		}
		scanf("%d",&q);
		scanf("%*[^\n]");
		scanf("%*c");
		for(i=0;i<q;++i)
		{
			scanf("%[^\n]%*c",query[i]);
		}
		printf("Case #%d: %d\n",cnt,solve(s,q));
	}
	return 0;
}

