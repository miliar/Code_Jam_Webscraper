#include <stdio.h>
#include <string.h>

int dir[2][4]={-1,0,0,1,
			   0,-1,1,0};
int f[20000];
char ch[20000];

int Find(int x) {
	int root=x;
	while(f[root]!=root) {
		root=f[root];
	}
	int p;
	while(x!=root) {
		p=f[x];
		f[x]=root;
		x=p;
	}
	return root;
}

void Union(int x, int y) {
	int xx=Find(x);
	int yy=Find(y);
	if (xx!=yy) {
		f[xx]=yy;
	}
}

int main() {
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int T=1;T<=tc;T++) {
		int i,j,k;
		int t=0;
		int n,m;
		int a[200][200];//map
		char b[200][200];//mark;
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++) {
			for(j=0;j<n;j++) {
				scanf("%d",&a[i][j]);
			}
		}

		for(i=0;i<n*m;i++) {
			f[i]=i;
		}

		for(i=0;i<m;i++) {
			for(j=0;j<n;j++) {
				int mink=-1;
				int min;
				for (k=0;k<4;k++) {
					int ii=i+dir[0][k];
					int jj=j+dir[1][k];
					if (ii>=0 && ii<m && jj>=0 && jj<n && a[ii][jj]<a[i][j]) {
						if (mink==-1 || a[ii][jj]<min) {
							mink=k;
							min=a[ii][jj];
						}
					}
				}
				if (mink!=-1) {
					int ii=i+dir[0][mink];
					int jj=j+dir[1][mink];
					Union(ii*n+jj, i*n+j);
				}
			}
		}

		memset(ch,0,sizeof(ch));
		char c='a';
		for(i=0;i<m;i++) {
			for(j=0;j<n;j++) {
				int x=i*n+j;
				int y=Find(x);
				if (ch[y]==0) {
					ch[y]=c;
					c++;
				}
				b[i][j]=ch[y];
			}
		}

		printf("Case #%d:\n", T);
		for(i=0;i<m;i++) {
			for(j=0;j<n;j++) {
				printf("%c ",b[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
