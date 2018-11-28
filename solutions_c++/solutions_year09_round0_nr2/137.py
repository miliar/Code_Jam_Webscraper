#include <iostream>
using namespace std;

#define MAXX 128
#define MAXY 128
#define INFH 16384

int dx[4] = {0, -1, +1, 0};
int dy[4] = {-1, 0, 0, +1};

int m[MAXX][MAXY];
char r[MAXX][MAXY], c;

char dfs(int x, int y) {
   int d, bd;

   if (r[x][y] == 0) {
		bd = -1;
	   for (d=0; d<4; d++) {
		   if (m[x][y] > m[x+dx[d]][y+dy[d]] && (bd == -1 || m[x+dx[bd]][y+dy[bd]] > m[x+dx[d]][y+dy[d]])) bd = d;
		}
		if (bd == -1) {r[x][y] = c; c++;}
		else {r[x][y] = dfs(x+dx[bd], y+dy[bd]);}
	}
   return r[x][y];
}

int main() {

int X, Y, i, j, t, T;

cin >> T;

for (t=1; t<=T; t++) {

cin >> Y;
cin >> X;

for (i=0; i<=X+1; i++) m[i][0] = m[i][Y+1] = INFH;
for (j=0; j<=Y+1; j++) m[0][j] = m[X+1][j] = INFH;

for (j=1; j<=Y; j++) {
   for (i=1; i<=X; i++) {
      cin >> m[i][j];
   }
}

cout << "Case #" << t << ":" << endl;

memset(r, 0, sizeof(r)); c = 'a';
for (j=1; j<=Y; j++) {
   for (i=1; i<=X; i++) {
	   dfs(i, j);
		cout << r[i][j];
		if (i < X) cout << ' ';
   }
	cout << endl;
}

}

return 0;
}
