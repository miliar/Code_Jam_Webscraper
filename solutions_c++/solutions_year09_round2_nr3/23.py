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
#define abs(x) (x<0?-x:x)

string m[20][20][1024];
char vis[20][20][1024];

struct node {
	node(int xx, int yy, int vv) { x = xx; y = yy; v = vv; }
	int x, y, v;
};

int main()
{
	int n, w, qr, num;
	string s, b[21];
	const int off = 512;
	const int minv = -150, maxv = 450;

	//ifstream fin("C-small.in");
	//ofstream fout("C-small.out");
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	fin >> n;

	REP(tc,n) {
		fout <<"Case #"<<tc+1<<":"<<endl;
		fin >> w >> qr;
		getline(fin,s);

		REP(i,w) {
			getline(fin,b[i]);
		}

		REP(i,w) REP(j,w) REP(z,1024) vis[i][j][z] = 0;

		queue <node> q;

		REP(i,w) REP(j,w) {
			if (b[i][j] != '+' && b[i][j] != '-') {
				string s; s.append(b[i].substr(j,1));
				q.push(node(i,j,b[i][j]-'0'));
				vis[i][j][b[i][j]-'0'+off] = 1;
				m[i][j][b[i][j]-'0'+off] = s;
			}
		}

		while (!q.empty()) {
			node a = q.front(); q.pop();
			int x = a.x, y = a.y, v = a.v, nx, ny, nx2, ny2, nv;
			string e = m[x][y][v+off], ne;
			char sgn;
			FOR(dx,-1,2) FOR(dy,-1,2) if (abs(dx) != abs(dy)) {
				nx = x+dx; ny = y+dy;
				if (nx < 0 || ny < 0 || nx>=w || ny >=w) continue;
				sgn = b[nx][ny];
				FOR(dx2,-1,2) FOR(dy2,-1,2) if (abs(dx2) != abs(dy2)) {
					nx2 = nx+dx2; ny2 = ny+dy2;
					if (nx2 < 0 || ny2 < 0 || nx2>=w || ny2 >=w) continue;
					if (sgn == '+') nv = v + b[nx2][ny2] - '0';
					else nv = v - (b[nx2][ny2] - '0');

					if (nv < minv || nv > maxv) continue;

					if ( vis[nx2][ny2][nv+off] == 0 || m[nx2][ny2][nv+off].size() > e.size()) {
						ne = e + sgn + b[nx2][ny2];
						if (ne.size() > m[nx2][ny2][nv+off].size() && vis[nx2][ny2][nv+off] != 0) continue;
						if (vis[nx2][ny2][nv+off] != 0 && ne > m[nx2][ny2][nv+off]) continue;
						if (vis[nx2][ny2][nv+off] == 0) {
							vis[nx2][ny2][nv+off] = 1;
							m[nx2][ny2][nv+off] = ne;
							q.push(node(nx2,ny2,nv));
						} else {
							m[nx2][ny2][nv+off] = ne;
						}
					}

				}

			}
		}

		

		REP(i,qr) {
			string best = "";
			fin >> num;
			REP(a,w) REP(b,w) if (vis[a][b][num+off]) {
				if (best == "" || best.size() > m[a][b][num+off].size() || (best.size() == m[a][b][num+off].size() && best > m[a][b][num+off]) )
					best = m[a][b][num+off];
			}
			fout << best << endl;
		}



		
	}

	fin.close();
	fout.close();

	return 0;
}

