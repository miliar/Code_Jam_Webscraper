
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

#define stala 3000
#define maxn 24
int nx[] = {-1, 0, 1, 0};
int ny[] = {0, 1, 0, -1};


int n, query;

char t[maxn][maxn];
int d[maxn][maxn][stala * 2 + 5];
int lex[maxn][maxn][stala * 2 + 5];
pair<int,int> pop[maxn][maxn][stala * 2 + 5];
char pop2[maxn][maxn][stala * 2 + 5];

struct stan {
	int x, y, val;
	stan(int xx, int yy, int vall) { x = xx; y = yy; val = vall; }
};
int k = 10;
map<pair<int, pair<char, char> >, int> mapa;

inline bool isok(int x, int y) {
	return x >= 1 && y >= 1 && x <= n && y <= n;
}
int eval(char a, char b) {
	if (a == '+') return b - '0';
	else return -(b - '0');
}
inline bool isNumber(char a) { return a >= '0' && a <= '9'; }
inline bool isZnak(char a) { return a == '-' || a == '+'; }
inline bool ok(int x, int y) { return x >= 1 && x <= n && y >= 1 && y <= n; }
 
void wypisz(int x, int y, int val) {
//	cout << "wypisz " << x << " " << y << " " << val << endl;
	if (x == -1) return;
	wypisz(pop[x][y][val + stala].FI, pop[x][y][val + stala].SE, val - eval(pop2[x][y][val + stala], t[x][y]));
	if (pop[x][y][val + stala].FI != -1) cout << pop2[x][y][val + stala];
	cout << t[x][y];
}
int main(){
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
	mapa.clear();
	k = 10;
	cin >> n >> query;
	fup(i, 1, n) fup(j, 1, n) {
		fup(z, 0, 2 * stala) { d[i][j][z] = inf; }
		cin >> t[i][j];
	}

	vector<stan> Q;
	fup(i, 1, n) fup(j, 1, n) {
		if (isNumber(t[i][j])) { 
			Q.push_back(stan(i, j, t[i][j] - '0'));
			d[i][j][t[i][j] - '0' + stala] = 1;
			lex[i][j][t[i][j] - '0' + stala] = t[i][j] - '0';
			pop[i][j][t[i][j] - '0' + stala] = MP(-1, -1);
		}
	}

	int droga = 1;

	while (!Q.empty()) {

		vector<stan> Q2;
		vector<pair<int, pair<char, char> > > tosort;

		fup(i, 0, siz(Q) - 1) {
			int x, y, val;
			x = Q[i].x;
			y = Q[i].y;
			val = Q[i].val;
			fup(a, 0, 3) fup(b, 0, 3) {
				int xx, yy, xxx, yyy;
				xx = x + nx[a];
				yy = y + ny[a];
				xxx = xx + nx[b];
				yyy = yy + ny[b];	
				if (!ok(xx, yy) || !ok(xxx, yyy)) continue;

				if (isZnak(t[xx][yy]) && isNumber(t[xxx][yyy])) {
					int nval = val + eval(t[xx][yy], t[xxx][yyy]);
			//		if (abso(nval) > stala) continue;
				//	if (droga + 2 <= d[xxx][yyy][nval + stala]) {
						tosort.PB(MP(lex[x][y][val + stala], MP(t[xx][yy], t[xxx][yyy])));
				//	}
				}		
			}
		}		
		sort(ALL(tosort));

		fup(i, 0, siz(tosort) - 1) {
			//cout << tosort[i].FI << " " << tosort[i].SE.FI << " " << tosort[i].SE.SE << endl;
			if (i && tosort[i] != tosort[i - 1]) mapa[tosort[i]] = ++k;
		}
		
		
		fup(i, 0, siz(Q) - 1) {
			int x, y, val;
			x = Q[i].x;
			y = Q[i].y;
			val = Q[i].val;
			fup(a, 0, 3) fup(b, 0, 3) {
				int xx, yy, xxx, yyy;
				xx = x + nx[a];
				yy = y + ny[a];
				xxx = xx + nx[b];
				yyy = yy + ny[b];	
				if (!ok(xx, yy) || !ok(xxx, yyy)) continue;

				if (isZnak(t[xx][yy]) && isNumber(t[xxx][yyy])) {
					int nval = val + eval(t[xx][yy], t[xxx][yyy]);
					if (abso(nval) > stala) continue;
					int z = mapa[MP(lex[x][y][val + stala], MP(t[xx][yy], t[xxx][yyy]))];
					if (droga + 2 < d[xxx][yyy][nval + stala] || (droga + 2 == d[xxx][yyy][nval + stala] && 
						mapa[MP(lex[x][y][val + stala], MP(t[xx][yy], t[xxx][yyy]))] < lex[xxx][yyy][nval + stala])) {
/*
						if (lex[x][y][val + stala] == 345 || lex[x][y][val + stala] == 346) {
							cout << "GO " << endl;
							cout << x << " " << y << " " << val << " " << nval << endl;
							cout << xxx << " " << yyy << endl;
							debug(lex[x][y][val + stala]);
							debug(mapa[MP(lex[x][y][val + stala], MP(t[xx][yy], t[xxx][yyy]))]);
							cout << "+++++++++++++++++++++++++" << endl;
							debug(d[5][1][21 + stala]);
							debug(lex[5][1][21 + stala]);
						}
*/
					if (d[xxx][yyy][nval + stala] == inf) Q2.push_back(stan(xxx, yyy, nval));
						d[xxx][yyy][nval + stala] = droga + 2;
						lex[xxx][yyy][nval + stala] = mapa[MP(lex[x][y][val + stala], MP(t[xx][yy], t[xxx][yyy]))];
						pop[xxx][yyy][nval + stala] = MP(x, y);
						pop2[xxx][yyy][nval + stala] = t[xx][yy];
					}
				}

			}
		}
		Q = Q2;
		droga += 2;
	}

	printf("Case #%d:\n", c);
	fup(i, 1, query) {
		int a;
		cin >> a;
		int best = inf;
		int bestlex = inf;
		int x, y;
		fup(i, 1, n) fup(j, 1, n) {
			if (d[i][j][a + stala] < best || (d[i][j][a + stala] == best && lex[i][j][a + stala] < bestlex)) {
				best = d[i][j][a + stala];
				bestlex = lex[i][j][a + stala];
				x = i; y = j;	
			}
		}	
//		debug(best);
//		debug(x);
//		debug(y);
//		debug(a);
		wypisz(x, y, a);
		cout << endl;
	}
}

	return 0;	
}


