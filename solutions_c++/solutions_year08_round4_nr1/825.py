#include<stdio.h>
#include<string.h>
int tree[100001][2];
int m,v;
int change=0;
int tt[100001][2];
void main()
{
	int n,k=1,i,j;
	int ft;
		freopen("A-large.in","r",stdin);
	freopen("hi.txt","w",stdout);
	scanf("%d",&n);
	while(k<=n)
	{
		change=0;
		scanf("%d%d",&m,&v);
		for(i=1;i<=(m-1)/2;i++)
		{
			scanf("%d%d",&tree[i][0],&tree[i][1]);
		}
		for(i=(m+1)/2;i<=m;i++)
		{
			scanf("%d",&tree[i][0]);
		}
		for(i=0;i<=m;i++)
		{
			tt[i][0]=100000;
			
			tt[i][1]=100000;
		}
		for(i=(m+1)/2;i<=m;i++)
		{
			ft=tree[i][0];
			tt[i][ft]=0;
		}
		for(i=(m-1)/2;i>=1;i--)
		{
			int ft1=tree[i][0];
			int ft2=tree[i][1];
			if(ft2==0)
			{
				int s1=2*i;
				int s2=2*i+1;
				if(ft1==1)
				{
					if(tt[i][1]>tt[s1][1]+tt[s2][1])
						tt[i][1]=tt[s1][1]+tt[s2][1];
						if(tt[i][0]>tt[s1][0]+tt[s2][1])
							tt[i][0]=tt[s1][0]+tt[s2][1];
						if(tt[i][0]>tt[s1][1]+tt[s2][0])
							tt[i][0]=tt[s1][1]+tt[s2][0];
						if(tt[i][0]>tt[s1][0]+tt[s2][0])
							tt[i][0]=tt[s1][0]+tt[s2][0];
				}
				else
				{
					if(tt[i][1]>tt[s1][0]+tt[s2][1])
							tt[i][1]=tt[s1][0]+tt[s2][1];
						if(tt[i][1]>tt[s1][1]+tt[s2][0])
							tt[i][1]=tt[s1][1]+tt[s2][0];
						if(tt[i][0]>tt[s1][0]+tt[s2][0])
							tt[i][0]=tt[s1][0]+tt[s2][0];
					if(tt[i][1]>tt[s1][1]+tt[s2][1])
						tt[i][1]=tt[s1][1]+tt[s2][1];
				}
			}
			else
			{
				int s1=2*i;
				int s2=2*i+1;
				if(ft1==1)
				{
					if(tt[i][1]>tt[s1][1]+tt[s2][1])
						tt[i][1]=tt[s1][1]+tt[s2][1];
						if(tt[i][0]>tt[s1][0]+tt[s2][1])
							tt[i][0]=tt[s1][0]+tt[s2][1];
						if(tt[i][0]>tt[s1][1]+tt[s2][0])
							tt[i][0]=tt[s1][1]+tt[s2][0];
						if(tt[i][0]>tt[s1][0]+tt[s2][0])
							tt[i][0]=tt[s1][0]+tt[s2][0];
				}
				else
				{
					if(tt[i][1]>tt[s1][0]+tt[s2][1])
							tt[i][1]=tt[s1][0]+tt[s2][1];
						if(tt[i][1]>tt[s1][1]+tt[s2][0])
							tt[i][1]=tt[s1][1]+tt[s2][0];
						if(tt[i][0]>tt[s1][0]+tt[s2][0])
							tt[i][0]=tt[s1][0]+tt[s2][0];
					if(tt[i][1]>tt[s1][1]+tt[s2][1])
						tt[i][1]=tt[s1][1]+tt[s2][1];
				}
				ft1=1-ft1;
				if(ft1==1)
				{
					if(tt[i][1]>tt[s1][1]+tt[s2][1]+1)
						tt[i][1]=tt[s1][1]+tt[s2][1]+1;
						if(tt[i][0]>tt[s1][0]+tt[s2][1]+1)
							tt[i][0]=tt[s1][0]+tt[s2][1]+1;
						if(tt[i][0]>tt[s1][1]+tt[s2][0]+1)
							tt[i][0]=tt[s1][1]+tt[s2][0]+1;
						if(tt[i][0]>tt[s1][0]+tt[s2][0]+1)
							tt[i][0]=tt[s1][0]+tt[s2][0]+1;
				}
				else
				{
					if(tt[i][1]>tt[s1][0]+tt[s2][1]+1)
							tt[i][1]=tt[s1][0]+tt[s2][1]+1;
						if(tt[i][1]>tt[s1][1]+tt[s2][0]+1)
							tt[i][1]=tt[s1][1]+tt[s2][0]+1;
						if(tt[i][0]>tt[s1][0]+tt[s2][0]+1)
							tt[i][0]=tt[s1][0]+tt[s2][0]+1;
					if(tt[i][1]>tt[s1][1]+tt[s2][1]+1)
						tt[i][1]=tt[s1][1]+tt[s2][1]+1;
				}
			}
		}
		if(tt[1][v]>=100000)
			printf("Case #%d: IMPOSSIBLE\n",k);
		else
		printf("Case #%d: %d\n",k,tt[1][v]);
		k++;
	}
}