#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)

const int N = 15;

char a[20][20];
short d[N*N*4][N*N*4][N][N];

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

int r, c;

struct state {
	int pa, pb;
	int r, c;
	state(int a, int b, int c_, int d) {
		pa = a; pb = b;
		r = c_; c = d;
	}
	state() {}
};


int shoot(int rr, int cc, int d) {
	int nr, nc;
	while (true) {
		nr = rr + dx[d];
		nc = cc + dy[d];
		if (nr < 0 || nc < 0 || nr >= r || nc >= c || a[nr][nc] != '.') break;
		rr = nr;
		cc = nc;
	}
	nr -= dx[d];
	nc -= dy[d];
	return nr*N*4+nc*4+d;
}

bool isportal(int r, int c, int p, int d)
{
	return r*N*4+c*4+d == p;
}

int main()
{
	//ifstream fin("B-small.in");
	//ofstream fout("B-small.out");
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	long long nc;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		fout <<"Case #"<<tc<<": ";

		fin >> r >> c;
		REP(i,r) {
			fin >> a[i];
		}

		memset(d, -1, sizeof(d));
		queue <state> q[200];

		int cr, cc, pr, pc;

		REP(i,r) REP(j,c) if (a[i][j] == 'X') {
			cr = i; cc = j;
		}
		a[cr][cc] = '.';

		REP(i,r) REP(j,c) if (a[i][j] == 'O') {
			pr = i; pc = j;
		}
		a[pr][pc] = '.';

		d[0][0][pr][pc] = 0;
		q[0].push(state(0, 0, pr, pc));
		int res = -1;
		int cnt = 0;
		int nq = 0;
		while (nq < 200) {
			if (q[nq].empty()) { ++nq; continue; }
			
			state s = q[nq].front(); q[nq].pop();
			int time = d[s.pa][s.pb][s.r][s.c];
			//cout << s.r << " " << s.c << endl;
			// shoot portals
			REP(i, 4) FOR(j, i+1, 4) {
				int pa = shoot(s.r, s.c, i);
				int pb = shoot(s.r, s.c, j);
				if (d[pa][pb][s.r][s.c] < 0) {
					d[pa][pb][s.r][s.c] = time;
					q[time].push(state(pa, pb, s.r, s.c));
				}
			}
			// move
			REP(i,4) {
				if (isportal(s.r, s.c, s.pa, i)) {
					int nr = s.pb/(4*N);
					int nc = (s.pb/4)%N;
					if (d[s.pa][s.pb][nr][nc] < 0) {
						d[s.pa][s.pb][nr][nc] = time + 1;
						q[time+1].push(state(s.pa, s.pb, nr, nc));

						if (nr == cr && nc == cc) { res = time + 1; goto end; }
					}
				} else if (isportal(s.r, s.c, s.pb, i)) {
					int nr = s.pa/(4*N);
					int nc = (s.pa/4)%N;
					if (d[s.pa][s.pb][nr][nc] < 0) {
						d[s.pa][s.pb][nr][nc] = time + 1;
						q[time+1].push(state(s.pa, s.pb, nr, nc));
						if (nr == cr && nc == cc) { res = time + 1; goto end; }
					}
				} else {
					int nr = dx[i] + s.r;
					int nc = dy[i] + s.c;
					if (nr < 0 || nc < 0 || nr >= r || nc >= c || a[nr][nc] != '.') continue;
					if (d[s.pa][s.pb][nr][nc] < 0) {
						d[s.pa][s.pb][nr][nc] = time + 1;
						q[time+1].push(state(s.pa, s.pb, nr, nc));
						if (nr == cr && nc == cc) { res = time + 1; goto end; }
					}
				}
			}
		}

end:;
		if (res < 0) fout << "THE CAKE IS A LIE" << endl;
		else fout << res << endl;
		cout << tc << endl;
	}

	fin.close();
	fout.close();

	return 0;
}

