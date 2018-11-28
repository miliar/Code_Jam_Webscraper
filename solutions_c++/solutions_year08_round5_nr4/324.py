#include<cstdio>
#include<cstring>
const int mn=105;

int T,h,w,r;
long long f[mn][mn];

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tn=1;tn<=T;tn++)
	{
		scanf("%d%d%d",&h,&w,&r);
		memset(f,0,sizeof(f));
		for(int i=1;i<=r;i++)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			f[x][y]=-1;
		}
		f[1][1]=1;
		for(int i=1,tx,ty;i<=h;i++)
			for(int j=1;j<=w;j++)
			{
				if(f[i][j]==-1){f[i][j]=0;continue;}
				tx=i-1,ty=j-2;
				if(tx>0&&tx<=h&&ty>0&&ty<=w)f[i][j]+=f[tx][ty];
				tx=i-2,ty=j-1;
				if(tx>0&&tx<=h&&ty>0&&ty<=w)f[i][j]+=f[tx][ty];
			}
		printf("Case #%d: %I64d\n",tn,f[h][w]%10007);
	}
	return 0;
}
