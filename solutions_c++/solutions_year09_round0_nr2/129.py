#include <cstdio>
#include <string>
using namespace std;

int dx[]={-1,0,0,1},dy[]={0,-1,1,0};
char ans[10005];
int a[105][105],b[105][105],f[10005];

int getf(int x) {
	if (f[x]!=x) {
		return f[x]=getf(f[x]);
	}
	return x;
}


void make(int xx,int yy) {
	xx=getf(xx);
	yy=getf(yy);
	if (xx!=yy) {
		f[xx]=yy;
	}
}

int main() {
int z,zz,i,j,k,no,x,y,nx,ny,xx,yy,m,n;
char c;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	for (scanf("%d",&zz),z=1;z<=zz;++z) {
		printf("Case #%d:\n",z);
		scanf("%d%d",&m,&n);
		for (i=0;i<m;++i) {
			for (j=0;j<n;++j) {
				scanf("%d",&a[i][j]);
				b[i][j]=-1;
			}
		}
		for (i=no=0;i<m;++i) {
			for (j=0;j<n;++j) {
				if (b[i][j]<0) {
					f[no]=no;
					for (b[x=i][y=j]=no;;) {
						xx=yy=-1;
						for (k=0;k<4;++k) {
							nx=x+dx[k];
							ny=y+dy[k];
							if ((nx<0) || (nx>=m) || (ny<0) || (ny>=n) || (a[nx][ny]>=a[x][y])) {
								continue;
							}
							if ((xx<0) || (a[xx][yy]>a[nx][ny])) {
								xx=nx;
								yy=ny;
							}
						}
						if (xx<0) {
							break;
						}
						if (b[xx][yy]<0) {
							b[xx][yy]=no;
							x=xx;
							y=yy;
						}
						else {
							make(b[i][j],b[xx][yy]);
							break;
						}
					}
					ans[no++]=0;
				}
			}
		}
		for (i=0,c='a';i<m;++i) {
			for (j=0;j<n;++j) {
				k=getf(b[i][j]);
				if (ans[k]==0) {
					ans[k]=c++;
				}
				if (j) {
					printf(" ");
				}
				printf("%c",ans[k]);
			}
			printf("\n");
		}
	}
	return 0;
}
				

							



	