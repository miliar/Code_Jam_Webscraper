#include<iostream>
int main()
{
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	int t,z,n,i,j,k,x;
	char map[60][60],g[60][60];
	scanf("%d",&t);
	for(z=1;z<=t;z++)
	{
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)scanf("%s",map[i]);
		memset(g,'.',sizeof(g));
		for(i=0;i<n;i++)for(x=0,j=n-1;j>=0;j--)if(map[i][j]!='.')g[i][x++]=map[i][j];
		bool ans1,ans2;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				for(x=0;x<k;x++)if(!(j+x<n&&g[i][j+x]=='R'))break;
				if(x==k)break;
				for(x=0;x<k;x++)if(!(i+x<n&&g[i+x][j]=='R'))break;
				if(x==k)break;
				for(x=0;x<k;x++)if(!(i+x<n&&j+x<n&&g[i+x][j+x]=='R'))break;
				if(x==k)break;
				for(x=0;x<k;x++)if(!(i-x<n&&j+x<n&&g[i-x][j+x]=='R'))break;
				if(x==k)break;
			}
			if(j<n)break;
		}
		ans1=(i<n);
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				for(x=0;x<k;x++)if(!(j+x<n&&g[i][j+x]=='B'))break;
				if(x==k)break;
				for(x=0;x<k;x++)if(!(i+x<n&&g[i+x][j]=='B'))break;
				if(x==k)break;
				for(x=0;x<k;x++)if(!(i+x<n&&j+x<n&&g[i+x][j+x]=='B'))break;
				if(x==k)break;
				for(x=0;x<k;x++)if(!(i-x<n&&j+x<n&&g[i-x][j+x]=='B'))break;
				if(x==k)break;
			}
			if(j<n)break;
		}
		ans2=(i<n);
		printf("Case #%d: ",z);
		if(ans1&&ans2)printf("Both\n");
		else if(ans1)printf("Red\n");
		else if(ans2)printf("Blue\n");
		else printf("Neither\n");
	}
}