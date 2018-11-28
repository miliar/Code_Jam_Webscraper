#include<iostream>
#include<algorithm>
int d[2][101][101],xm,ym,now,next;
bool check()
{
	int i,j;
	for(i=1;i<=xm;i++)
		for(j=1;j<=ym;j++)
			if(d[now][i][j])return true;
	return false;
}
int main()
{
	int T,cs,i,j,n,ans,xx,yy,xl,xr,yl,yr,sc;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-Large.in","r",stdin);
//	freopen("C-Large.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		memset(d,0,sizeof(d));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d%d",&xl,&yl,&xr,&yr);
			if(xl>xr)std::swap(xl,xr);
			if(yl>yr)std::swap(yl,yr);
			if(xm<xr)xm=xr;
			if(ym<yr)ym=yr;
			for(xx=xl;xx<=xr;xx++)
				for(yy=yl;yy<=yr;yy++)
					d[0][xx][yy]=1;
		}
		sc=0;
		now=0;next=1;
		while(check())
		{
			for(i=1;i<=xm;i++)
				for(j=1;j<=ym;j++)
					if((d[now][i-1][j]||d[now][i][j-1])&&d[now][i][j])d[next][i][j]=1;
					else if(d[now][i-1][j]&&d[now][i][j-1])d[next][i][j]=1;
					else d[next][i][j]=0;
			std::swap(now,next);
			sc++;
		}
		printf("Case #%d: %d\n",cs,sc);
	}
	return 0;
}