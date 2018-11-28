#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int T, H, W;

int world[110][110];
int color[110][110];
int clr;
int choose[4];
int INF = 1000000;
int nr, nc, caseNum;
char palette[10100], p;


void flow(int r, int c) {
	//printf("now: %d %d\n",r,c);
	
	choose[0]=INF; choose[1]=INF; choose[2]=INF; choose[3]=INF;
	if (r>0) 	choose[0] = world[r-1][c]*10 + 0;
	if (c>0) 	choose[1] = world[r][c-1]*10 + 1;
	if (c<W-1) 	choose[2] = world[r][c+1]*10 + 2;
	if (r<H-1) 	choose[3] = world[r+1][c]*10 + 3;
	
	sort(choose,choose+4);
	
	if (choose[0]==INF) return;
	
	nr = r; nc = c;
	if (choose[0]%10==0) nr = r-1;
	else if (choose[0]%10==1) nc = c-1;
	else if (choose[0]%10==2) nc = c+1;
	else nr = r+1;
	
	//printf("best choice: %d %d (%d) among %d %d %d %d\n",nr,nc,world[nr][nc],choose[0],choose[1],choose[2],choose[3]);
	
	if (color[r][c]==color[nr][nc]) return;
	if (world[r][c]<=world[nr][nc]) return;
	
	color[r][c]=color[nr][nc];
	
	flow(nr,nc);
}


int getRepr( int row, int col ) {
	int i = color[row][col]/100;
	int j = color[row][col]%100;
	
	if (i != row || j != col) {
		color[row][col] = getRepr( i, j );
	}
	return color[row][col];
}

void read() {
	scanf("%d %d", &H,&W);
	
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			scanf("%d",&world[i][j]);
			color[i][j] = i*100 + j;
		}
	}
}

void process() {
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			flow(i,j);
		}
	}
	
	memset(palette,0,sizeof(palette));
	int count = 0;
	
	caseNum++;
	printf("Case #%d:\n",caseNum);
	
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (j!=0) printf(" ");
			clr = getRepr(i,j);
			if (palette[clr]==0) {
				palette[clr]='a'+count;
				count++;
			}
			printf("%c",palette[clr]);
		}
		printf("\n");
	}
	
}


int main() {
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d", &T);
	
	caseNum=0;
	while (T--) {
		read();
		process();
	}
	
	return 0;
}


