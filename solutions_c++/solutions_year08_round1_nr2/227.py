#include <stdio.h>

int K;
int l[100][20][2],nl[100];



int Cul(int obj)
{
	int ret=0;
	while (obj)
	{
		ret += obj&1;
		obj>>=1; 
	}
	return ret;
}
int main()
{
	freopen("ans.out","w",stdout);
	int i,j,k,n;
	int t,st,suc,ans;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d %d",&K,&n);
		for (i=0;i<n;++i)
		{
			scanf("%d",nl+i);
			for (j=0;j<nl[i];++j)
			{
				scanf("%d %d",&l[i][j][0],&l[i][j][1]);
			}
		}
		ans=-1;
		for (i=0;i<(1<<K);++i)
		{
			for (j=0;j<n;++j)
			{
				suc=0;
				for (k=0;k<nl[j]&&!suc;++k)
				{
					if ( (i & (1<<(l[j][k][0]-1)))>>(l[j][k][0]-1)
						==l[j][k][1]) suc=1;
				}
				if (!suc) break;
			}
			if (j==n)
			{
				if (ans==-1||Cul(i)<Cul(ans)) ans = i;
			}
		}
		if (ans==-1) printf("Case #%d: IMPOSSIBLE\n",t+1);
		else
		{
			printf("Case #%d: ",t+1);
			for (i=0;i<K;++i)
			{
				if (i) printf(" ");
				printf("%d",ans&(1<<i)?1:0);
			}
			printf("\n");
		}		
	}	
	return 0;	 
}