#include <iostream>
using namespace std;

#define MAXN 128
#define SLIM MAXN*MAXN*MAXN

struct pt {
	int x, y, cur;
} p1, p2, s[SLIM];

bool m[2][MAXN][MAXN];

int main() {

//freopen("in.txt", "r", stdin);

int r, R, i, j, S, E, x, y, cur, CUR, RES, t, T;

cin >> T;

for (t=1; t<=T; t++) {

cin >> R;

memset(m, false, sizeof(m));
for (r=0; r<R; r++) {
	cin >> p1.x;
	cin >> p1.y;
	cin >> p2.x;
	cin >> p2.y;

	for (i=p1.x; i<=p2.x; i++) {
		for (j=p1.y; j<=p2.y; j++) {
			m[0][i][j] = true;
		}
	}
}

S = E = 0;
for (i=0; i<MAXN; i++) {
	for (j=0; j<MAXN; j++) {
		if (m[0][i][j] == true) {
			s[E].x = i;
			s[E].y = j;
			s[E].cur = 0;
			E++;
		}
	}
}

CUR = RES = 0;
while (S != E) {
	x = s[S].x;
	y = s[S].y;
	cur = s[S].cur;
	S++; if (S == SLIM) S = 0;

	if (cur != CUR) {
		RES++;
		CUR = cur;
		memset(m[1-cur], false, sizeof(m[1-cur]));

/*		for (i=0; i<51; i++) {
			for (j=0; j<51; j++) {
				cout << m[cur][j][i];
			}
			cout << endl;
		}
		cout << endl;*/
	}

	if (m[cur][x-1][y] == true || m[cur][x][y-1] == true) {
		m[1-cur][x][y] = true;
		s[E].x = x;
		s[E].y = y;
		s[E].cur = 1-cur;
		E++; if (E == SLIM) E = 0;
	}

	if (m[1-cur][x+1][y] == false && m[cur][x+1][y-1] == true) {
		m[1-cur][x+1][y] = true;
		s[E].x = x+1;
		s[E].y = y;
		s[E].cur = 1-cur;
		E++; if (E == SLIM) E = 0;
	}
}
cout << "Case #" << t << ": " << RES+1 << endl;

}

return 0;
}
