#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int lim=256;

int cases,ans,n,vd,vi,m;
int f[110][300],g[300],a[300];

void update(int &a,int k) {
	if (a==-1 || k<a) a=k;
}

int gabs(int a) {
	return (a>0)?a:(-a);
}

int main() {
	scanf("%d",&cases);
	for (int dog=1;dog<=cases;dog++) {
		scanf("%d%d%d%d",&vd,&vi,&m,&n);
		for (int i=1;i<=n;i++) {
			scanf("%d",&a[i]);
		}
		ans=n*vd;
		memset(f,-1,sizeof(f));
		f[0][256]=0;
		for (int i=1;i<=n;i++) {
			for (int j=0;j<256;j++) {
				update(f[i][j],f[i-1][256]+gabs(a[i]-j));
			}
			
			for (int j=0;j<=lim;j++) {
				if (f[i-1][j]!=-1) {
					if (j!=256) {
						update(f[i][j],f[i-1][j]+vd);
						for (int k=max(0,j-m);k<=min(255,j+m);k++) {
							update(f[i][k],f[i-1][j]+gabs(k-a[i]));
						}
					} else {
						update(f[i][j],f[i-1][j]+vd);
					}
				}
			}
			
			//for (int j=0;j<=10;j++) printf("%d ",f[i][j]);
			//printf("\n");
			
			for (int j=0;j<lim;j++) g[j]=f[i][j];
			if (m!=0) {
			for (int j=0;j<lim;j++) {
				if (g[j]!=-1) {
					for (int k=0;k<lim;k++) {
						if (k!=j) 
							update(f[i][k],g[j]+((gabs(k-j)-1)/m+1)*vi);
					}
				}
			}
			}
			/*for (int j=0;j<lim;j++) {
				if (g[j]!=-1) {
					//printf("j %d\n",j);
					for (int k=0;k<=255;k++) {
						update(f[i][k],g[j]+gabs(k-j));
					}
				}
			}*/
			

			
			//for (int j=0;j<=10;j++) printf("%d ",f[i][j]);
			//printf("\n\n");

		}
		for (int i=0;i<=lim;i++) {
			if (f[n][i]!=-1 && f[n][i]<ans) ans=f[n][i];
		}
		printf("Case #%d: %d\n",dog,ans);
	}
}
