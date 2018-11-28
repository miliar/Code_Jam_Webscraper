#include<stdio.h>
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
int from[1024][11],to[1024][11];

void pl(int n){	
	int pr;
	for(int i=0;i<1024;i++)
		for(int j=0;j<=10;j++)
			to[i][j]=1000000000;
	for(int i=0;i<n;i++){
		int x=2*i,y=2*i+1;
		scanf("%d",&pr);
		for(int tx=0;tx<=10;tx++)
			for(int ty=0;ty<=10;ty++)
				for(int tz=0;tz<=min(tx,ty);tz++)
					if(to[i][tz]>from[x][tx]+from[y][ty]+pr)
						to[i][tz]=from[x][tx]+from[y][ty]+pr;
		for(int tx=0;tx<=10;tx++)
			for(int ty=0;ty<=10;ty++)
				for(int tz=0;tz<=min(tx,ty)-1;tz++)
					if(to[i][tz]>from[x][tx]+from[y][ty])
						to[i][tz]=from[x][tx]+from[y][ty];
	}
	for(int i=0;i<1024;i++)
		for(int j=0;j<=10;j++)
			from[i][j]=to[i][j];
}

int main()
{
	int c;
	scanf("%d",&c);
	for(int cc=1;cc<=c;cc++){
		int p;
		scanf("%d",&p);
		for(int i=0;i<1024;i++)
			for(int j=0;j<=10;j++)
				from[i][j]=1000000000;
		for(int i=0;i<(1<<p);i++){
			int x;
			scanf("%d",&x);
			for(int j=0;j<=x;j++)
				from[i][j]=0;
		}
		for(int i=p-1;i>=0;i--)
			pl(1<<i);
		int ans=1000000000;
		for(int i=0;i<(1<<p);i++)
			for(int j=0;j<=p;j++)
				if(ans>from[i][j])
					ans=from[i][j];
		printf("Case #%d: %d\n",cc,ans);
	}
}
