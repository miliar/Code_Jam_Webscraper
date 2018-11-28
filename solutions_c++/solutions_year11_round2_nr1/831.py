#include<stdio.h>
main()
{
	int abc,ab,i,j,n,m,k;
	double ans[150],rwp[150][2],wp[150],owp[150],oowp[150];
	char map[150][150];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&abc);
	for(ab=1;ab<=abc;ab++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				scanf(" %c",&map[i][j]);
		for(i=0;i<n;i++)
		{
			double all=0,w=0;
			for(j=0;j<n;j++)
			{
				if(map[i][j]!='.')
					all++;
				if(map[i][j]=='1')
					w++;
			}
			wp[i]=w/all;
			rwp[i][0]=w;
			rwp[i][1]=all;
		}
		for(i=0;i<n;i++)
		{
			int all=0;
			double w=0;
			for(j=0;j<n;j++)
				if(map[i][j]!='.')
				{
					all++;
					w+=((rwp[j][0]-(map[j][i]-'0'))/(rwp[j][1]-1));
				}
			owp[i]=w/all;
		}
		for(i=0;i<n;i++)
		{
			int all=0;
			double w=0;
			for(j=0;j<n;j++)
				if(map[i][j]!='.')
				{
					all++;
					w+=owp[j];
				}
			oowp[i]=w/all;
		}
		printf("Case #%d:\n",ab);
		for(i=0;i<n;i++)
		{
			ans[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			printf("%.6lf\n",ans[i]);
		}
	}
}
/*
5
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
*/
