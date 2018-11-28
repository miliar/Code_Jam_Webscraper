#include <cstdio>
#include <algorithm>
using namespace std;

int n,m;
int map[512][3000];
char buf[2000];
int res[600];

void inmap(int x, int y, char c) {
	int v = 0;
	if (c >= '0' && c <='9') v = c-'0';
	if (c >='A' && c<='F') v = 10 + c - 'A';
	map[x][y+3] = v%2;
	v/=2;
	map[x][y+2] = v%2;
	v/=2;
	map[x][y+1] = v%2;
	v/=2;
	map[x][y] = v%2;
}

int row[3000];
int kw[512][3000];

int del() {
	int siz = 0, where[2] = {0,0};
	for (int i=0;i<m;i++) {
		if (map[0][i]==-1) row[i]=kw[0][i]=0;
		else row[i]=kw[0][i]=1;
		if (kw[0][i] > siz) {
			siz = kw[0][i];
			where[0] = 0;
			where[1] = i;
		}
	}
	int col = 1;
	for (int x=1;x<n;x++) {
		if (map[x][0]==-1) {
			kw[x][0] = col = 0;
		}
		else {
			kw[x][0] = col = 1;
		}
		if (kw[x][0] > siz) {
			siz = kw[x][0];
			where[0] = x;
			where[1] = 0;
		}
		for (int y=1;y<m;y++) {
			if (map[x][y] == -1) {
				col = 0;
				row[y] = 0;
				kw[x][y] = 0;
				continue;
			}
			if (map[x][y] != map[x][y-1]) col++;
			else col=1;
			if (map[x][y] != map[x-1][y]) row[y]++;
			else row[y] = 1;
			if (map[x][y] == map[x-1][y-1]) {
				/* robimy kwadracik */
				kw[x][y] = min(min(kw[x-1][y-1]+1,col),row[y]);
			}
			else kw[x][y] = 1;
			if (kw[x][y] > siz) {
				siz = kw[x][y];
				where[0] = x;
				where[1] = y;
			}
			//printf("col=%d row[%d]=%d Kw[%d][%d] = %d\n", col,y,row[y],x, y, kw[x][y]);
		}
	}
	if (siz > 0) {
		//printf("wycinam %d z %d,%d, %d\n", siz, where[0]-siz+1, where[1]-siz+1,
		//	map[where[0]-siz+1][where[1]-siz+1]);
		for (int x=where[0]-siz+1;x<=where[0];x++)
			for (int y=where[1]-siz+1;y<=where[1];y++) map[x][y]=-1;
		return siz;
	}
	return 0;
}

void test() {
	scanf("%d%d ", &n, &m);
	for (int i=0;i<550;i++) res[i]=0;
	for (int i=0;i<n;i++) {
		scanf("%s ", buf);
		for (int j=0;j<m/4;j++) {
			inmap(i,j*4,buf[j]);
		}
	}
	int w;
	while ((w = del())) {
		res[w]++;
	}
	int cnt = 0;
	for (int i=0;i<550;i++) if (res[i]) cnt++;
	printf("%d\n", cnt);
	for (int i=550;i>0;i--) if (res[i]) printf("%d %d\n", i, res[i]);
}

main() {
	int z;
	scanf("%d", &z);
	for (int i=0;i<z;i++) {
		printf("Case #%d: ", i+1);
		test();
	}
}

