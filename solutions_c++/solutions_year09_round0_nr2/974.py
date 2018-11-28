#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

int G[105][105];
int R[105][105][5];
int F[105][105];
int S[105][105];
char result[105][105];
int h, w;
int inf = 1000000000;

int move[][2] = {
	-1, 0,
	0, 1,
	1, 0,
	0, -1
};

void dfs(int r, int c, int v) {
	F[r][c] = v;
	int i;

	for(i=0;i<4;i++) {
	  if( R[r][c][i] ) {
		 dfs(r + move[i][0], c + move[i][1], v);
	  }
	}
}

void fill_it(int r, int c, char ch, int v) {
	result[r][c] = ch;
	F[r][c] = 0;
	int i;
	for(i=0;i<4;i++) {
	  int rr = r + move[i][0];
	  int cc = c + move[i][1];
	  if( rr >= 1 && rr <= h && cc >= 1 && cc <= w && F[rr][cc] == v ) {
	     fill_it(rr, cc, ch, v);
	  }
	}
}

int main() {
	int t, cases = 1;
	cin >> t; int i, j, k;
	for( cases = 1; cases <= t; cases++) {
		cin >> h >> w;
		for(i=0;i<=h+1;i++)
		 for(j=0;j<=w+1;j++)
		  G[i][j] = inf;

		for(i=1;i<=h;i++)
		 for(j=1;j<=w;j++)
		   scanf("%d", &G[i][j]), S[i][j] = 0;

		for(i=1;i<=h;i++)
		 for(j=1;j<=w;j++)
		  for(k=0;k<5;k++)
		    R[i][j][k] = 0;

		for(i=1; i<=h; i++)
		 for(j=1;j<=w;j++) {
			int m = inf;
			for(k=0;k<4;k++) {
			  int r = i + move[k][0];
			  int c = j + move[k][1];
			  m <?= G[r][c];
		  	}

			if( m >= G[i][j] ) {
			 S[i][j] = 1;
			}
			else {
			  int r, c;
			  for(int kk=0;kk<4;kk++) {
				 k = 0;
				 r = i + move[k][0];
				 c = j + move[k][1];
				 if( G[r][c] == m ) break;

				 k = 3;
				 r = i + move[k][0];
				 c = j + move[k][1];
				 if( G[r][c] == m ) break;

				 k = 1;
				 r = i + move[k][0];
				 c = j + move[k][1];
				 if( G[r][c] == m ) break;

				 k = 2;
				 r = i + move[k][0];
				 c = j + move[k][1];
				 if( G[r][c] == m ) break;
			  }
			  if( k == 0 ) R[r][c][2] = 1;
			  if( k == 1 ) R[r][c][3] = 1;
			  if( k == 2 ) R[r][c][0] = 1;
			  if( k == 3 ) R[r][c][1] = 1;
			}
		 }

		int v = 1;
		for(i=1;i<=h;i++)
		 for(j=1;j<=w;j++)
		  if( S[i][j] == 1 ) {
		    dfs(i, j, v);
		    v++;
		  }

		char c = 'a';
		for(i=1;i<=h;i++)
		 for(j=1;j<=w;j++)
		  if( F[i][j] ) {
			 fill_it(i, j, c, F[i][j]);
			 c++;
		  }

		printf("Case #%d:\n", cases);
		for(i=1;i<=h;i++, printf("\n"))
		 for(j=1;j<=w;j++) {
			if( j > 1 ) printf(" ");
			printf("%c", result[i][j]);
		 }
	}
	return 0;
}
