#include<cstdio>
#include<cstring>
int main()
{
	int dirx[8]={0,-1,-1,-1,0,1,1,1};
	int diry[8]={-1,-1,0,1,1,1,0,-1};
	bool red,blue;
	int cs,c,i,j,n,k,t,len,tx,ty,l;
	char mp[110][110];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cs);
	for (c=1;c<=cs;c++)
	{
		scanf("%d%d",&n,&k);
		getchar();
		memset(mp,'.',sizeof(mp));
		for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
				scanf("%c",&mp[j][n-1-i]);
			getchar();
		}
/*		for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
				printf("%c",mp[i][j]);
			printf("\n");
		}*/
		for (i=n-2;i>=0;i--)
			for (j=0;j<n;j++)
			{
				t=i;
				while (mp[t+1][j]=='.' && mp[t][j]!='.')
				{
					mp[t+1][j]=mp[t][j];
					mp[t][j]='.';
					t++;
					if (t==n-1) break;
				}
			}
/*		for (i=0;i<n;i++)
		{
			for (j=0;j<n;j++)
				printf("%c",mp[i][j]);
			printf("\n");
		}*/
		red=false;
		blue=false;
		for (i=0;i<n;i++)
			for (j=0;j<n;j++)
				if (mp[i][j]!='.')
					for (l=0;l<8;l++)
						if (mp[i][j]!=mp[i-dirx[l]][j-diry[l]])
						{
							tx=i;
							ty=j;
							len=1;
							while (tx<n && tx>=0 && ty<n && ty>=0 && mp[tx][ty]==mp[tx+dirx[l]][ty+diry[l]])
							{
								len++;
								tx+=dirx[l];
								ty+=diry[l];
								if (tx>=n || ty>=n || tx<0 || ty<0) break;
							}
							if (len>=k)
							{
								if (mp[i][j]=='R') red=true;
								else blue=true;
							//	printf("%d %d %d %d %d\n",i,j,tx,ty,l);
							}
						}
		printf("Case #%d: ",c);
		if (red&&blue) printf("Both\n");
		if (!red && !blue) printf("Neither\n");
		if (red && !blue) printf("Red\n");
		if (!red && blue) printf("Blue\n");
	}
	return 0;
}
