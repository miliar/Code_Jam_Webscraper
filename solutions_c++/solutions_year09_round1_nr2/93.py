#include<cstdlib>
#include<ctime>
#include<cstdio>
#include<cstring>
int mk[40][40],s[20][40],w[20][20],t[20][20];
int x[4000000],y[4000000],dis[4000000],nn,mm;
int checky(int x0,int y0,int xx,int yy,int tt)
{
	if(xx<0||xx>mm||yy<0||yy>nn)return 0;
	if(y0%2==0)//上马路
	{
		if(yy>y0)//往上
		{
			tt-=t[y0/2][x0/2];
			tt%=(s[y0/2][x0/2]+w[y0/2][x0/2]);
			if(tt<s[y0/2][x0/2])return 1;
			else return s[y0/2][x0/2]+w[y0/2][x0/2]-tt+1;
		}
		else//往下
			return 2;
	}
	else//下马路
	{
		if(yy>y0)return 2;//往上
		else//往下
		{
			tt-=t[y0/2][x0/2];
			tt%=(s[y0/2][x0/2]+w[y0/2][x0/2]);
			if(tt<s[y0/2][x0/2])return 1;
			else return s[y0/2][x0/2]+w[y0/2][x0/2]-tt+1;
		}
	}
}
int checkx(int x0,int y0,int xx,int yy,int tt)
{
	if(xx<0||xx>mm||yy<0||yy>nn)return 0;
	if(x0%2==0)//右马路
	{
		if(xx>x0)//往右
		{
			tt-=t[y0/2][x0/2];
			tt%=(s[y0/2][x0/2]+w[y0/2][x0/2]);
			if(tt>=s[y0/2][x0/2])return 1;
			else return s[y0/2][x0/2]-tt+1;
		}
		else//往左
			return 2;
	}
	else//左马路
	{
		if(xx>x0)return 2;//往右
		else//往左
		{
			tt-=t[y0/2][x0/2];
			tt%=(s[y0/2][x0/2]+w[y0/2][x0/2]);
			if(tt>=s[y0/2][x0/2])return 1;
			else return s[y0/2][x0/2]-tt+1;

		}
	}
}
int main()
{
	freopen("B-Large.in","r",stdin);
	freopen("B-Large.out","w",stdout);
	srand(time(NULL));
	int cs,css,i,j,st,ed,xx,yy,x2,y2,n,m,tt;
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d%d",&n,&m);
		for(i=n-1;i>=0;i--)
			for(j=0;j<m;j++)
			{
				scanf("%d%d%d",&s[i][j],&w[i][j],&t[i][j]);
				t[i][j]%=(s[i][j]+w[i][j]);
				t[i][j]-=(s[i][j]+w[i][j]);
			}
		nn=n*2-1;mm=m*2-1;
		for(i=0;i<=nn;i++)
			for(j=0;j<=mm;j++)
				mk[i][j]=0x7fffffff;
		mk[0][0]=0;
		x[0]=y[0]=0;st=0;ed=1;
		for(;st!=ed;st++)
		{
			xx=x[st]+1;
			yy=y[st];
			if(tt=checkx(x[st],y[st],xx,yy,dis[st]))
			{
				if(dis[st]+tt<mk[yy][xx])
				{
					x[ed]=xx;
					y[ed]=yy;
					dis[ed++]=tt+dis[st];
					mk[yy][xx]=tt+dis[st];
				}
			}
			xx=x[st]-1;
			yy=y[st];
			if(tt=checkx(x[st],y[st],xx,yy,dis[st]))
			{
				if(dis[st]+tt<mk[yy][xx])
				{
					x[ed]=xx;
					y[ed]=yy;
					dis[ed++]=tt+dis[st];
					mk[yy][xx]=tt+dis[st];
				}
			}
			xx=x[st];
			yy=y[st]-1;
			if(tt=checky(x[st],y[st],xx,yy,dis[st]))
			{
				if(dis[st]+tt<mk[yy][xx])
				{
					x[ed]=xx;
					y[ed]=yy;
					dis[ed++]=tt+dis[st];
					mk[yy][xx]=tt+dis[st];
				}
			}
			xx=x[st];
			yy=y[st]+1;
			if(tt=checky(x[st],y[st],xx,yy,dis[st]))
			{
				if(dis[st]+tt<mk[yy][xx])
				{
					x[ed]=xx;
					y[ed]=yy;
					dis[ed++]=tt+dis[st];
					mk[yy][xx]=tt+dis[st];
				}
			}
		}
		printf("Case #%d: %d\n",css,mk[nn][mm]);
	}
	return 0;
}
