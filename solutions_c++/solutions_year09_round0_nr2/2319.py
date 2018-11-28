#include <stdio.h>
#include <string.h>
#include <cstdlib>

using namespace std;

int ncase;
int T, W, H;
int d[101][101];
int map[101][101];
int car[101];
int dy[]={-1, 0, 0, 1};
int dx[]={0, -1, 1, 0};
int label;



#define isin(a,b) (((a)>=0)&&((a)<W)&&((b)>=0)&&((b)<H))

void debugmap() {
		for (int i=0; i<W; i++) {
			for (int j=0; j<H; j++) {
				printf("%d ", map[i][j]);
			}
			printf("\n");
		}
}

int traverse(int i, int j) {
	if (map[i][j]>0) return map[i][j];

	int min=d[i][j];
	int bestdir=-1;
	for (int dir=0; dir<4; dir++) {
		if (isin(i+dy[dir], j+dx[dir]) && d[i+dy[dir]][j+dx[dir]]<min) {
			min=d[i+dy[dir]][j+dx[dir]];
			bestdir=dir;
		}
	}
	if (bestdir==-1)
		map[i][j]=++label;
	else
		map[i][j]=traverse(i+dy[bestdir], j+dx[bestdir]);
	//debugmap();
	return map[i][j];

}




int main() {

	scanf(" %d", &T);
	for (ncase=0; ncase<T; ncase++) {
		label=0;

		scanf(" %d %d", &W, &H);
		for (int i=0; i<W; i++)
			for (int j=0; j<H; j++)
				scanf(" %d", &d[i][j]);


		memset(map, 0, sizeof(map));
		for (int i=0; i<W; i++) {
			for (int j=0; j<H; j++) {
				if (map[i][j]==0) {
					traverse(i, j);
				}
			}
		}

		printf("Case #%d:\n", ncase+1);
		memset(car, 0, sizeof(car));



		label='a';
		for (int i=0; i<W; i++) {
			for (int j=0; j<H; j++) {
				if (car[map[i][j]]==0) car[map[i][j]]=label++;
				if (j>0) printf(" ");
				printf("%c", car[map[i][j]]);

			}
			printf("\n");
		}

	}

	return 0;
}
