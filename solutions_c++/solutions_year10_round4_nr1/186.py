
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


int k;
int t[204][204];

int getX(int k, int x, int y) {
	return x;
}
int getY(int k, int x, int y) {
	if (x <= k); else x = 2 * k - x;
	return (k - x) + y * 2 - 1;
}

int rowSize(int k, int row) {
	if (row <= k) return row;
	else return 2 * k - row;
}

int ile(int k) {
	int sum = 0;
	fup(i, 1, 2 * k - 1) sum += rowSize(k, i);
		return sum;
}

#define maxn 1500
int mat[maxn][maxn];
bool zle(int a, int b) {
	assert(a != -2);
	assert(b != -2);
	if (a == -1 || b == -1) return false;
	if (a != b) return true;
	return false;
}
bool isok(int x) {
	return x >= 0 && x < maxn;
}

bool checkCase(int roz, int sx, int sy) {
	
	fup(i, 1, 2 * k - 1) {
		fup(j, 1, rowSize(k, i)) {
			if (isok(getX(k, i, j) + sx)== false) return false;
			if (isok(getY(k, i, j) + sy) == false) return false;

			if (mat[getX(k, i, j) + sx][getY(k, i, j) + sy] != -1) return false;
		}
	}
	fup(i, 1, 2 * k - 1) {
		fup(j, 1, rowSize(k, i)) {
			mat[getX(k, i, j) + sx][getY(k, i, j) + sy] = t[i][j];	
		}
	}

/*	map<pair<int, int>, int> mapa;
	//cout << "GGG " << endl;
	fup(i, 1, 2 * roz - 1) {
		fup(j, 1, rowSize(roz, i)) {
		mapa[MP(i, j)] = mat[getX(roz, i, j)][getY(roz, i, j)];
		
	}
	//	cout << endl;
	}*/

	bool ok = true;
	fup(i, 1, 2 * roz - 1) fup(j, 1, rowSize(roz, i)) {
		int ii, jj;
		ii = i;
		jj = rowSize(roz, i) + 1 - j;
		if (mat[getX(roz, i, j)][getY(roz, i, j)] == -1) continue;
		
		if (zle(mat[getX(roz, i, j)][getY(roz, i, j)], mat[getX(roz, ii, jj)][getY(roz, ii, jj)])) {
			ok = false; goto done; }

	}
	fup(i, 1, 2 * roz - 1) fup(j, 1, rowSize(roz, i)) {
		int ii, jj;
		ii = i;
		jj = j;
		ii = 2 * roz - i;

		if (mat[getX(roz, i, j)][getY(roz, i, j)] == -1) continue;
if (zle(mat[getX(roz, i, j)][getY(roz, i, j)], mat[getX(roz, ii, jj)][getY(roz, ii, jj)])) {
			ok = false; goto done; }

	}

done:;
	
	fup(i, 1, 2 * k - 1) {
		fup(j, 1, rowSize(k, i)) {
			mat[getX(k, i, j) + sx][getY(k, i, j) + sy] = -1;
		}
	}
	return ok;

}

bool checkSize(int roz) {
	fup(i, 0, maxn - 1) fup(j, 0, maxn - 1) mat[i][j] = -2;

	fup(i, 1, 2 * roz - 1) {
		fup(j, 1, rowSize(roz, i)) mat[getX(roz, i, j)][getY(roz, i, j)] = -1;
	}

	//fup(sx, 
	//fup(sx, - 5 * roz - 3, 5 * roz  + 3) fup(sy, - 5 * roz - 3, 5 * roz + 3) {
	fup(i, 1, 2 * roz - 1) fup(j, 1, rowSize(roz, i)) {
		int dx, dy;
		int sx = getX(roz, i, j);
		int sy = getY(roz, i, j);
		int aa, bb;
		aa = getX(k, 1, 1);
		bb = getY(k, 1, 1);
		dx = sx - aa;
		dy = sy - bb;

		
		if (checkCase(roz, dx, dy)) return true;
	}
	return false;
}

int main() {
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		cin >> k;		
		fup(i, 1, 2 * k - 1) {
			fup(j, 1, rowSize(k, i)) {
				cin >> t[i][j];

			}	
		}
	
		int best = inf;
		fup(size, k, 6 * k ) {
//			cout << "TRY " << size << endl;
			if (checkSize(size)) {
				best = ile(size) - ile(k);
				break;
			}
		}
//		cout << best << endl;
		printf("Case #%d: %d\n", c, best);

	}
	return 0;
}


