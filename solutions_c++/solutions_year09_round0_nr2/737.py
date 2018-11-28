#include <cstdio>
#include <vector>
#include <algorithm>
#define M_HW 200
#define INF 90000
using namespace std;
int alt [M_HW][M_HW];
char labels [M_HW][M_HW];
char last;
int T;
int H, W;
int move[4][2] = {{-1,0}, {0,-1}, {0, 1}, {1,0}};
char ffill(int r, int c) {
	if (labels[r][c]!=' ') return labels[r][c];
	int lowest = alt[r][c];
	int lm = -1;
	for (int m=0;m<4;++m) if (alt[r+move[m][0]][c+move[m][1]]<lowest) {
		lowest = alt[r+move[m][0]][c+move[m][1]];
		lm = m;
	}
	if (lm==-1) {
		labels[r][c] = last;
		++last;
	} else labels[r][c] = ffill(r+move[lm][0], c+move[lm][1]);
	return labels[r][c];
}
int main() {
	scanf("%d", &T);
	for (int t=0;t<T;++t) {
		last = 'a';
		scanf("%d %d", &H, &W);
		for (int i=0;i<=W+1;++i) alt[0][i] = alt[H+1][i] = INF;
		for (int i=0;i<=H+1;++i) alt[i][0] = alt[i][W+1] = INF;
		for (int r=1;r<=H;++r) for (int c=1;c<=W;++c) scanf("%d", &alt[r][c]);
		for (int r=0;r<=H+1;++r) for (int c=0;c<=W+1;++c) labels[r][c] = ' ';	
		/*for (int r=0;r<=H+1;++r) {
			for (int c=0;c<=W+1;++c) printf("%d ", alt[r][c]);
			printf("\n");
		}*/
		for (int r=1;r<=H;++r) for (int c=1;c<=W;++c) ffill(r, c);
		printf("Case #%d:\n", t+1);
		for (int r=1;r<=H;++r) {
			for (int c=1;c<W;++c) printf("%c ", labels[r][c]);
			printf("%c\n", labels[r][W]);
		}
	}

}
