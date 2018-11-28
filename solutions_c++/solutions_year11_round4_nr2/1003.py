#include <stdio.h>
#include <string.h>

#define MAX 512

char w[MAX][MAX];

int xs[MAX][MAX];
int ys[MAX][MAX];
int xc[MAX][MAX][MAX/2];
int yc[MAX][MAX][MAX/2];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int r,c,d;
		scanf("%d%d%d",&r,&c,&d);
		for(int i=0;i<r;++i)
			scanf("%s",&w[i]);
		int ans=2;
		for(int i=0;i<r;++i) {
			xs[i][0]=0;
			for(int j=1;j<=c;++j)
				xs[i][j]=xs[i][j-1]+(w[i][j-1]-'0'+d);
		}
		for(int j=0;j<c;++j) {
			ys[j][0]=0;
			for(int i=1;i<=r;++i)
				ys[j][i]=ys[j][i-1]+(w[i-1][j]-'0'+d);
		}
		for(int i=0;i<r;++i) {
			for(int j=0;j<c;++j) {
				xc[i][j][0]=0;
				for(int k=1;j-k>=0 && j+k<c;++k) {
					xc[i][j][k]=xc[i][j][k-1]+(w[i][j-k]-'0'+d)*(-k)+(w[i][j+k]-'0'+d)*(k);
				}
			}
		}
		for(int j=0;j<c;++j) {
			for(int i=0;i<r;++i) {
				yc[j][i][0]=0;
				for(int k=1;i-k>=0 && i+k<r;++k) {
					yc[j][i][k]=yc[j][i][k-1]+(w[i-k][j]-'0'+d)*(-k)+(w[i+k][j]-'0'+d)*(k);
				}
			}
		}
		for(int i=0;i<r;++i) {
			for(int j=0;j<c;++j) {
				int x=0,y=0;
				for(int k=1;i-k>=0 && i+k<r && j-k>=0 && j+k<c;++k) {
					x=x+(ys[j-k][i+k+1]-ys[j-k][i-k])*(-k)+(ys[j+k][i+k+1]-ys[j+k][i-k])*k;
					x=x+xc[i-k][j][k-1]+xc[i+k][j][k-1];
					y=y+(xs[i-k][j+k+1]-xs[i-k][j-k])*(-k)+(xs[i+k][j+k+1]-xs[i+k][j-k])*k;
					y=y+yc[j-k][i][k-1]+yc[j+k][i][k-1];
					int cx,cy;
					cx=x-(w[i-k][j-k]-'0'+d)*(-k)-(w[i-k][j+k]-'0'+d)*(k)
					    -(w[i+k][j-k]-'0'+d)*(-k)-(w[i+k][j+k]-'0'+d)*(k);
					cy=y-(w[i-k][j-k]-'0'+d)*(-k)-(w[i+k][j-k]-'0'+d)*(k)
					    -(w[i+k][j+k]-'0'+d)*(k)-(w[i-k][j+k]-'0'+d)*(-k);
					if(cx==0 && cy==0) {
						if(ans<2*k+1) ans=2*k+1;
					}
				}
			}
		}
		for(int i=0;i<r;++i) {
			for(int j=0;j<c;++j) {
				xc[i][j][0]=0;
				for(int k=1;j-k+1>=0 && j+k<c;++k) {
					xc[i][j][k]=xc[i][j][k-1]+(w[i][j-k+1]-'0'+d)*(-k)+(w[i][j+k]-'0'+d)*(k);
				}
			}
		}
		for(int j=0;j<c;++j) {
			for(int i=0;i<r;++i) {
				yc[j][i][0]=0;
				for(int k=1;i-k+1>=0 && i+k<r;++k) {
					yc[j][i][k]=yc[j][i][k-1]+(w[i-k+1][j]-'0'+d)*(-k)+(w[i+k][j]-'0'+d)*(k);
				}
			}
		}
		for(int i=0;i<r;++i) {
			for(int j=0;j<c;++j) {
				int x=0,y=0;
				for(int k=1;i-k+1>=0 && i+k<r && j-k+1>=0 && j+k<c;++k) {
					x=x+(ys[j-k+1][i+k+1]-ys[j-k+1][i-k+1])*(-k)+(ys[j+k][i+k+1]-ys[j+k][i-k+1])*k;
					x=x+xc[i-k+1][j][k-1]+xc[i+k][j][k-1];
					y=y+(xs[i-k+1][j+k+1]-xs[i-k+1][j-k+1])*(-k)+(xs[i+k][j+k+1]-xs[i+k][j-k+1])*k;
					y=y+yc[j-k+1][i][k-1]+yc[j+k][i][k-1];
					int cx,cy;
					cx=x-(w[i-k+1][j-k+1]-'0'+d)*(-k)-(w[i-k+1][j+k]-'0'+d)*(k)
					    -(w[i+k][j-k+1]-'0'+d)*(-k)-(w[i+k][j+k]-'0'+d)*(k);
					cy=y-(w[i-k+1][j-k+1]-'0'+d)*(-k)-(w[i+k][j-k+1]-'0'+d)*(k)
					    -(w[i+k][j+k]-'0'+d)*(k)-(w[i-k+1][j+k]-'0'+d)*(-k);
					if(cx==0 && cy==0) {
						if(ans<2*k) ans=2*k;
					}
				}
			}
		}
		if(ans>=3)
			printf("Case #%d: %d\n",test,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",test);
	}
	return 0;
}
