#include<stdio.h>
#include<string.h>

int bc[10000];
int find(int a) {
	int r=a, t;
	while(bc[r]!=-1) r=bc[r];
	while(a!=r) t=bc[a], bc[a]=r, a=t;
	return r;
}

bool unite(int a, int b) {
	int ra=find(a), rb=find(b);
	if(ra==rb) return false;
	bc[ra]=rb;
	return true;
}

int ht[100][100], H, W;
bool valid(int x, int y) { return x>=0&&x<H&&y>=0&&y<W; }
const int dir[][2]={{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
char id[10000], res[100][100];
void solve() {
	memset(bc, -1, sizeof(bc));
	scanf("%d%d", &H, &W);
	for(int i=0;i<H;i++)
		for(int j=0;j<W;j++)
			scanf("%d", &ht[i][j]);
	for(int i=0;i<H;i++) {
		for(int j=0;j<W;j++) {
			int lx=i, ly=j;
			for(int k=0;k<4;k++) {
				int nx=i+dir[k][0], ny=j+dir[k][1];
				if(valid(nx, ny)&&ht[nx][ny]<ht[lx][ly]) {
					lx=nx; ly=ny;
				}
			}
			unite(i*100+j, lx*100+ly);
		}
	}

	memset(id, -1, sizeof(id));
	char idc='a';
	for(int i=0;i<H;i++) {
		for(int j=0;j<W;j++) {
			int rt=find(i*100+j);
			if(id[rt]==-1) id[rt]=idc++;
			putchar(id[rt]);
			putchar(' ');
		}
		putchar('\n');
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d:\n", c);
		solve();
	}
}