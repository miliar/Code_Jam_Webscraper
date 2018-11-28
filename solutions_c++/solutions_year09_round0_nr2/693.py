#include <cstdio>
#include <cstring>

int a[100][100];
int p[10000];
int f(int x,int y){ return x*100+y; }
int m, n;
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
bool in(int x,int y){ return x>=0&&x<m&&y>=0&&y<n; }
int find(int x) {
	while (x^p[x])
		x = p[x] = p[p[x]];
	return x;
}
int id[10000];
int main() {
	int z;
	scanf("%d", &z);
	for (int Zz=1; Zz<=z; Zz++) {
		scanf("%d%d",&m,&n);
		for (int i=0;i<m;i++)
			for (int j=0;j<n;j++)
				scanf("%d", &a[i][j]);
		for (int i=0;i<m;i++)
			for (int j=0;j<n;j++) {
				int z = f(i,j);
				int Mn = a[i][j], id = -1;
				for (int r=0; r<4; r++) {
					int x = i+dx[r], y = j+dy[r];
					if (in(x,y) && a[x][y]<Mn)
						id = f(x,y), Mn = a[x][y];
				}
				p[z] = id==-1 ? z : id;
			}
		memset(id,-1,sizeof(id));
		char c = 'a';
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++) {
				int k = find(f(i,j));
				if (id[k]==-1)	id[k] = c++;
				p[f(i,j)] = k;
			}
		printf("Case #%d:\n", Zz);
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
				printf("%c%c", id[p[f(i,j)]], j==n-1?'\n':' ');
	}
	return 0;
}
