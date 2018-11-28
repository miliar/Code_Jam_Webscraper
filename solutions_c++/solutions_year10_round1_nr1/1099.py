#include <stdio.h>
#include <string.h>


int T;
int N;
int K;

int board[50][50];

int scores[50][50];


int dump() {
	printf("N=%d K=%d\n", N, K);
	for (int y=0;y<N;y++) {
		for (int x=0;x<N;x++) {
			printf("%c", board[y][x]);
		}
		printf("\n");
	}
}

int dump_score() {
	for (int y=0;y<N;y++) {
		for (int x=0;x<N;x++) {
			printf("%d", scores[y][x]);
		}
		printf("\n");
	}
}


int gravity() {
	int i;
	int dist;
	char c;
	int dy;
	for (int x=0;x<N;x++) {
		dy=N-1;
		for (int y=N-1;y>=0;y--) {
			if (board[y][x]=='R'||board[y][x]=='B') {
				board[dy][x]=board[y][x];
				dy--;
			}
		}
		for (;dy>=0;dy--) board[dy][x]='.';
	}
}


int scr=0;
char last='.';
int maxb;
int maxr;

int inline point_score(char a) {

	if (a=='.') {scr=0;}
	else if (last==a) {
		scr++;
	} else if (a=='R'||a=='B') {
		scr=1;
	}
	
	if (a=='R'&&scr>maxr) {
		maxr=scr;
	}
	
	if (a=='B'&&scr>maxb) {
		maxb=scr;
	}
	
	last=a;
	return scr;
}

int check() {
	maxr=0;
	maxb=0;

	
//	memset(scores, sizeof(scores), 0);
	for (int y=0;y<N;y++) {
		scr = 0;
		for (int x=0;x<N;x++) {
//			scores[y][x]=
			point_score(board[y][x]);
		}
	}
//	dump_score();
//	memset(scores, sizeof(scores), 0);
	for (int x=0;x<N;x++) {
		scr = 0;
		for (int y=0;y<N;y++) {
//			scores[y][x]=
			point_score(board[y][x]);
		}
	}
//	dump_score();
	int x=-N;
	int y=0;
	int xx;
//	memset(scores, sizeof(scores), 0);	
	while (x<N) {
		scr=0;
		for (y=0;y<N;y++) {
			xx=x+y;
			if (xx>=0&&xx<N)
//				scores[y][xx]=
				point_score(board[y][xx]);
			else {
				scr=0;
			}
		}
		x++;
	}
//	dump_score();
//	memset(scores, sizeof(scores), 0);
	x=2*N;
	while (x>=0) {
		scr=0;
		for (y=0;y<N;y++) {
			xx=x-y;
			if (xx>=0&&xx<N)
//				scores[y][xx]=
				point_score(board[y][xx]);
			else {
				scr=0;
			}
		}
		x--;
	}
//	dump_score();
}


int main()
{
	int x, y;
	
	scanf("%d", &T);
	char line[100];
	int p;
	for (int t=0;t<T;t++) {
		scanf("%d %d\n", &N, &K);
		for (int y=0;y<N;y++) {
			scanf("%s\n", line);
			p=0;
			while (line[p]) {
				if (line[p]=='.') board[p][N-1-y]='.';
				if (line[p]=='R') board[p][N-1-y]='R';
				if (line[p]=='B') board[p][N-1-y]='B';
				p++;
			}
		}
//		dump();
//		printf("===\n");
		gravity();
//		dump();
		maxb=0;
		maxr=0;
		check();
		printf("Case #%d: ", t+1);
		if (maxr>=K&&maxb>=K) 
			printf("Both\n"); else
		if (maxr>=K) 
			printf("Red\n"); else
		if (maxb>=K) 
			printf("Blue\n"); else
			printf("Neither\n");
	}
	return 0;
}
