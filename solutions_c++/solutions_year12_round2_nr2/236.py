#include <stdio.h>      
#include <ctype.h>
#include <math.h>

#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
using namespace std;

#define ALL(x) x.begin(), x.end()
#define VAR(a,b) __typeof (b) a = b
#define REP(i,n) for (int _n=(n), i=0; i<_n; ++i)
#define FOR(i,a,b) for (int _b=(b), i=(a); i<=_b; ++i)
#define FORD(i,a,b) for (int _b=(b), i=(a); i>=_b; --i)
#define FORE(i,a) for (VAR(i,a.begin ()); i!=a.end (); ++i) 
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef double LD;

const int DBG = 0;

string toString(LL k){stringstream ss;ss << k;string res;ss >> res;return res;}
int toInt(string s){stringstream ss; ss << s; int res; ss >> res; return res;}

const int MAXN = 100;
const LD INF = 1e18;

const int dx[] = {-1,1,0,0}, dy[] = {0,0,-1,1};

int n,m;
LD h;

int C[MAXN][MAXN], F[MAXN][MAXN];
LD d[MAXN][MAXN];

bool isOk(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool canGo(int x, int y, int nx, int ny) {

    if (F[nx][ny] + 50.0 > C[nx][ny] ||
	F[x][y] + 50.0 > C[nx][ny])
	return false;

    if (F[nx][ny] + 50.0 > C[x][y])
	return false;
    
    return true;
}

int main() {
  	ios_base::sync_with_stdio(0);
	cout.setf(ios::fixed);

	int T;
	
	cin >> T;

	REP(q,T) {
		cout << "Case #" << q + 1 << ": ";
		cin >> h >> n >> m;

		REP(i,n) REP(j,m)
		    cin >> C[i][j];
		REP(i,n) REP(j,m)
		    cin >> F[i][j];

		REP(i,n) REP(j,m)
		    d[i][j] = INF;

		d[0][0] = 0;

		vector<PII> S;
		S.PB(MP(0,0));

		while (!S.empty()) {
		    PII nxt = S.back(); S.pop_back();
		    int x = nxt.ST, y = nxt.ND;
		    
		    
		    REP(i,4) {
			int nx = x + dx[i], ny = y + dy[i];
			if (isOk(nx,ny) && d[nx][ny] == INF && canGo(x,y,nx,ny) && h + 50 <= C[nx][ny] ) {
			    d[nx][ny] = 0;
			    S.PB(MP(nx,ny));
			}
		    }
		}

		set<pair<LD,PII> > P;
		REP(i,n) REP(j,m)
		    if (d[i][j] == 0)
			P.insert(MP(0,MP(i,j)));

		while (!P.empty()) {
		    pair<LD,PII> nxt = *(P.begin()); P.erase(P.begin());
		    int x = nxt.ND.ST, y = nxt.ND.ND;
		    LD t = nxt.ST;

		    if (t > d[x][y])
			continue;

		    if (x == n - 1 && y == m - 1)
			break;

		    REP(i,4) {
			int nx = x + dx[i], ny = y + dy[i];
			if (isOk(nx,ny) && canGo(x,y,nx,ny)) {
			    LD lev = h - t * 10;
			    LD nt = max(t, (h + 50 - C[nx][ny]) / 10);
			    assert(nt < INF);
			    lev = h - nt * 10;
			    if (lev >= 20 + F[x][y])
				nt += 1;
			    else
				nt += 10;
			    if (nt < d[nx][ny]) {
				d[nx][ny] = nt;
				P.insert(MP(nt,MP(nx,ny)));
			    }
			}
		    }
		    

		}

		cout << setprecision(10) << d[n - 1][m - 1] << endl;
		//return 0;
	}


  	return 0;
}	
