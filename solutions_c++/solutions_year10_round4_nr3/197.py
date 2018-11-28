
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
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
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

#define maxn 105
int co[maxn][maxn];

void dodaj(int x1, int y1, int x2, int y2) {
	fup(x, x1, x2) fup(y, y1, y2) co[x][y] = 1;
}


int tmp[maxn][maxn];

void makeStep() {
	CLR(tmp);
	fup(x, 1, 100) fup(y, 1, 100) {
		if (co[x][y]) {	
			if (co[x][y - 1] == 0 && co[x - 1][y] == 0) {
				tmp[x][y] = 0;
			} else tmp[x][y] = 1;
		} else {
			if (co[x][y - 1] && co[x - 1][y]) tmp[x][y] = 1;
		}
	}
	fup(x, 1, 100) fup(y, 1, 100) co[x][y] = tmp[x][y];

}

bool die() {
	fup(i, 1, 100) fup(j, 1, 100) if (co[i][j]) return false;
	return true;
}

void print() {
	fup(i, 1, 10) {
		fup(j, 1, 10) cout << co[i][j] << " " ;
		cout << endl;
	}
}
int main() {
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		CLR(co);	
		int r;
		cin >> r;
		fup(i, 1, r) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;	
			dodaj(x1, y1, x2, y2);
		}
		int step = 0;
		while (true) {
//			print();
//			cout << endl;
			if (die()) {
				break;
			}
			makeStep();
			++step;
//			if (step > 6) break;
		}
		printf("Case #%d: %d\n", c, step);
//		cout << step << endl;
	}
	return 0;
}

