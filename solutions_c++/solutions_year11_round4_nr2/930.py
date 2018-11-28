#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int t,r,c,d;
#define MAXN 505
int w[MAXN][MAXN];
int s[MAXN][MAXN];
int ans;

int getsum(int x0,int y0,int x1,int y1)
{
	return s[x1][y1]-s[x1][y0-1]-s[x0-1][y1]+s[x0-1][y0-1];
}

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("B-small-attempt2.in","r",stdin);
	//freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d\n",&t);
	for(int ca=1;ca<=t;++ca)
	{
		scanf("%d%d%d\n",&r,&c,&d);
		memset(w,0,sizeof(w));
		memset(s,0,sizeof(s));
		for(int i=1;i<=r;++i)
		{
			for(int j=1;j<=c;++j)
			{
				w[i][j]=getchar()-'0'+d;
			}
			getchar();
		}
		for(int i=1;i<=r;++i)
		{
			for(int j=1;j<=c;++j)
			{
				s[i][j]=w[i][j]+s[i-1][j]+s[i][j-1]-s[i-1][j-1];
			}
		}
		ans=-1;
		for(int k=3;k<=min(r,c);k++)
		{
			for(int i=1;i<=r;++i)
			{
				for(int j=1;j<=c;++j)
				{
					if(i+k-1>r||j+k-1>c)
					{
						continue;
					}
					if(k%2==1)
					{
						int r=k/2;
						double cx=i+r;
						double cy=j+r;
						double tx=0,ty=0;
						for(int i1=i;i1<=i+k-1;++i1)
						{
							for(int j1=j;j1<=j+k-1;++j1)
							{
								if(i1==i&&j1==j||i1==i&&j1==j+k-1||i1==i+k-1&&j1==j||i1==i+k-1&&j1==j+k-1)
								{
									continue;
								}
								tx+=(i1-cx)*w[i1][j1];
								ty+=(j1-cy)*w[i1][j1];
							}
						}
						if(fabs(tx)<1e-6&&fabs(ty)<1e-6)
						{
							ans=k;
						}
						/*
						int su=getsum(i,j,i+r-1,j+k-1)-w[i][j]-w[i][j+k-1];
						int sd=getsum(i+r+1,j,i+k-1,j+k-1)-w[i+k-1][j]-w[i+k-1][j+k-1];
						int sl=getsum(i,j,i+k-1,j+r-1)-w[i][j]-w[i+k-1][j];
						int sr=getsum(i,j+r+1,i+k-1,j+k-1)-w[i][j+k-1]-w[i+k-1][j+k-1];
						if(su==sd&&sl==sr)
						{
							//cout<<i<<' '<<j<<' '<<k<<' '<<endl;
							ans=k;
						}*/
					}
					else
					{
						int r=k/2;
						double cx=i+r-0.5;
						double cy=j+r-0.5;
						double tx=0,ty=0;
						for(int i1=i;i1<=i+k-1;++i1)
						{
							for(int j1=j;j1<=j+k-1;++j1)
							{
								if(i1==i&&j1==j||i1==i&&j1==j+k-1||i1==i+k-1&&j1==j||i1==i+k-1&&j1==j+k-1)
								{
									continue;
								}
								tx+=(i1-cx)*w[i1][j1];
								ty+=(j1-cy)*w[i1][j1];
							}
						}
						if(fabs(tx)<1e-6&&fabs(ty)<1e-6)
						{
							ans=k;
						}
						/*
						int su=getsum(i,j,i+r-1,j+k-1)-w[i][j]-w[i][j+k-1];
						int sd=getsum(i+r,j,i+k-1,j+k-1)-w[i+k-1][j]-w[i+k-1][j+k-1];
						int sl=getsum(i,j,i+k-1,j+r-1)-w[i][j]-w[i+k-1][j];
						int sr=getsum(i,j+r,i+k-1,j+k-1)-w[i][j+k-1]-w[i+k-1][j+k-1];
						if(su==sd&&sl==sr)
						{
							//cout<<i<<' '<<j<<' '<<k<<' '<<endl;
							ans=k;
						}*/
					}
				}
			}
		}
		printf("Case #%d: ",ca);
		if(ans==-1)
		{
			puts("IMPOSSIBLE");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
	return 0;
}
