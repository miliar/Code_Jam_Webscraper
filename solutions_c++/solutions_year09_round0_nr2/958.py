#include<iostream>
#include<cstring>
using namespace std;

int f[20000],map[120][120],g[20000],tr[4][2];
int zz,n,m,h;

int father(int k) {
	if (f[k] == k) return f[k];
	f[k]=father(f[k]);
	return f[k];
}

int work(int x,int y) {
	if (x < 0 || y < 0 || x>=n || y >=m) return 100000;
	return map[x][y];
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&zz);
	tr[0][0]=-1; tr[0][1]=0;
	tr[1][0]=0; tr[1][1]=-1;
	tr[2][0]=0; tr[2][1]=1;
	tr[3][0]=1; tr[3][1]=0;
	for (int z=1;z<=zz;z++) {
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++ )
			for (int j=0;j<m;j++)
			    scanf("%d",&map[i][j]);
		for (int i=0;i<n;i++)
		    for (int j=0;j<m;j++)
		        f[i*m+j]=i*m+j;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++) {
				h=100000;
				int l=0;
				for (int k=0;k<4;k++)
				    if (work(i+tr[k][0],j+tr[k][1]) < h) {
						l=k;
						h=work(i+tr[k][0],j+tr[k][1]);
					}
				if (h < map[i][j]) {
				//	printf("%d %d %d\n",i,j,l);
					int f1=father(i*m+j);
					int f2=father((i+tr[l][0])*m+j+tr[l][1]);
					f[f1]=f2;
				}
			}
		memset(g,0,sizeof(g));
		h=0;
		printf("Case #%d:\n",z);
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++) {
				int f1=father(i*m+j);
				if (g[f1]==0) {
					h++;
					g[f1]=h;
				}
				printf("%c ",g[f1]+'a'-1);
			//	printf("%d ",f1);
			}
			printf("\n");
		}
	}
}


