#include <iostream>
using namespace std;

const int xx[4] = {-1,0,0,1};
const int yy[4] = {0,-1,1,0};

int test,n,m;
int a[101][101];
char b[101][101];

int search(int x, int y)
{
	int mn=a[x][y], l=-1;
	for (int i=0; i<4; i++) {
		int x1=x+xx[i];
		int y1=y+yy[i];
		if (x1<0 || y1<0 || x1>=n || y1>=m) continue;
		if (a[x1][y1]<mn) { mn=a[x1][y1]; l=i; }
	}
	return l;
}

char dfs(int x, int y)
{
	if (b[x][y]>0) return b[x][y];
	char c=0;
	int l=search(x,y);
	if (l>=0) c=dfs(x+xx[l],y+yy[l]);
	return c;
}

void dfs_make(int x, int y, char c)
{
	b[x][y]=c;
	int l=search(x,y);
	if (l>=0) dfs_make(x+xx[l],y+yy[l],c);
	return;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%i",&test);
	for (int tt=1; tt<=test; tt++) {
		printf("Case #%i:\n",tt);
		scanf("%i%i",&n,&m);
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				scanf("%i",&a[i][j]);
				b[i][j]=0;
			}

		char c=0, cc='a';
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				if (b[i][j]!=0) continue;
				c=dfs(i,j);
				if (c==0) {
					dfs_make(i,j,cc);
					cc++;
				}
				else dfs_make(i,j,c);
			}
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) 
				printf("%c ",b[i][j]);
			printf("\n");
		}
	}

	return 0;
}