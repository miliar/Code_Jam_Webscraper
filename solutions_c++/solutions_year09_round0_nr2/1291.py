
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
#define maxn 105
using namespace std;
typedef long long lli;
typedef double ld;
int h, w;
pair<int, int> kto[maxn][maxn];
int t[maxn][maxn];
int nx[] = {-1, 0, 0, 1};
int ny[] = {0, -1, 1, 0};
bool ok(int x, int y) { return x >= 1 && x <= h && y >= 1 && y <= w; }

pair<int, int> go(int x, int y) {
	if (kto[x][y].FI != -1) return kto[x][y];
	int besti = -1;
	int mini = inf;
	fup(i, 0, 3) {
		int xx, yy;
		xx = x + nx[i];
		yy = y + ny[i];
		if (!ok(xx, yy)) continue;
		if (t[xx][yy] < mini) { mini = t[xx][yy]; besti = i; }
	}
	if (mini >= t[x][y]) {
		kto[x][y] = MP(x, y);
	} else {
		kto[x][y] = go(x + nx[besti], y + ny[besti]);
	}
	return kto[x][y];
}
char znak[maxn][maxn];
map<pair<int, int>, char> mapa;
int main(){
	int cas;
	scanf("%d", &cas); 
	fup(i, 1, cas) {
		mapa.clear();
		scanf("%d%d", &h, &w);
		fup(i, 1, h) fup(j, 1, w) kto[i][j].FI = -1;
		fup(i, 1, h) fup(j, 1, w) scanf("%d", &t[i][j]);
		char p = 'a' - 1;
		fup(i, 1, h) fup(j, 1, w) { go(i, j); }
		fup(i, 1, h) {
			fup(j, 1, w) {
			//	cout << i << " " << j << " " << kto[i][j].FI << " " << kto[i][j].SE << endl;
			if (mapa.find(kto[i][j]) != mapa.end()) znak[i][j] = mapa[kto[i][j]];
			else { mapa[kto[i][j]] = ++p; znak[i][j] = p; }
		}
		}
			printf("Case #%d:\n", i);
		fup(i, 1, h) {
			fup(j, 1, w) {
			if (j != 1) printf(" ");
			printf("%c", znak[kto[i][j].FI][kto[i][j].SE]);
		}

			printf("\n");
		}

	}

	return 0;	
}


