#include <iostream>
#include <algorithm>
#include <vector>

#define FOR(i,a,b) for(int i=a; i<(b); i++)

using namespace std;

bool ok(int x, int y, int H, int W) {
	if(x < 0 || y < 0 || x >= W || y >= H) return false;
	return true;
}

int main() {
	int xx[4] = { 0, -1, 1, 0 };
	int yy[4] = { -1, 0, 0, 1 };
	int plansza[100][100];
	int we[100][100];
	struct Pkt { 
		int v, x, y; 
		bool operator<(const Pkt& a) const {
			if( v != a.v ) return v < a.v;
			if( y != a.y ) return y < a.y;
			return x < a.x;
		}
	};

	int T;
	cin >> T;
	FOR(q,1,T+1) {
		cout << "Case #"<< q << ":" << endl;
		int H, W;
		cin >> H >> W;
		vector< Pkt > p(H*W);
		FOR(h,0,H) FOR(w,0,W) { 
			cin >> plansza[h][w];
			we[h][w] = plansza[h][w];
			p[h*W+w].v = plansza[h][w];
			p[h*W+w].y = h;
			p[h*W+w].x = w;
		}
		sort(p.begin(), p.end());
		char c = 'A';
		FOR(i,0,H*W) {
			bool done = false;
			int x1=-1, y1=-1;
			FOR(j,0,4) {
				int x = p[i].x + xx[j];
				int y = p[i].y + yy[j];
				if(!ok(x,y,H,W)) continue;
				if(we[y][x] >= plansza[p[i].y][p[i].x]) continue;
				if(plansza[y][x] >= 'A' && plansza[y][x] <= 'Z') {
					if(x1 == -1 || we[y1][x1] > we[y][x]) {
						y1=y;
						x1=x;
					}
					done = true;
				}
			}
			if(!done) {
				plansza[p[i].y][p[i].x] = c++;
			}
			else {
				plansza[p[i].y][p[i].x] = plansza[y1][x1];
			}
		}

		vector<char> m(26,0);
		c = 'a';
		FOR(h,0,H) FOR(w,0,W) { 
			if(plansza[h][w] < 'a' || plansza[h][w] > 'z') {
				if(m[plansza[h][w]-'A'] == 0) {
					m[plansza[h][w]-'A'] = c++;
				}
				plansza[h][w] = m[plansza[h][w]-'A'];
			}
		}
		
		FOR(h,0,H) {
			FOR(w,0,W) {
				cout << (char)plansza[h][w] << " ";
			}
			cout << endl;
		}
	}
	return 0;
}