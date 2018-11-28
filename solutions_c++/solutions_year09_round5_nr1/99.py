
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
#define maxn 20
map<vector<pair<int, int> > , int> mapa;
int co[maxn][maxn];
int h, w;

int nx[] = {1, 0, -1, 0};
int ny[] = {0, 1, 0, -1};

bool isok(int x, int y) {
	return x >= 1 && x <= h && y >= 1 && y <= w;
}

queue<vector<pair<int, int> > > Q;

int t[maxn][maxn];

vector<pair<int, int> > getStan() {
	vector<pair<int, int> > stan;
	fup(i, 1, h) fup(j, 1, w) if (t[i][j]) stan.PB(MP(i, j));
	sort(ALL(stan));
	return stan;
}

void dodaj(vector<pair<int, int> > stan, int d) {
	if (mapa.find(stan) != mapa.end()) return ;
	mapa[stan] = d;
	Q.push(stan);
}

bool done[maxn][maxn];
int N;
int sum;

void dfs(int x, int y) {
	sum++;
	done[x][y] = true;
	fup(i, 0, 3) {
		int xx, yy;
		xx = x + nx[i];
		yy = y + ny[i];
		if (done[xx][yy] || !isok(xx, yy) || t[xx][yy] != 1) continue;
		dfs(xx, yy);
	}
}

bool getTyp() {
	CLR(done);
	int x = -1, y;
	fup(i, 1, h) fup(j, 1, w) {
		if (t[i][j]) { x = i; y = j; goto done;}
	}
done:;
     sum = 0;
//     debug(x);
     dfs(x, y);
  //   debug(sum);
     if (sum == N) return true;
     return false;
}

void wypisz() {
	cout << "PL " << endl;
	fup(i, 1, h) {
		fup(j, 1, w) cout << t[i][j] ;
		cout << endl;
	}
	cout << endl;
}
void go(vector<pair<int, int> > stan) {
	int d = mapa[stan];
	CLR(t);

	fup(i, 0, siz(stan) - 1) {
		int x, y;
		x = stan[i].FI;
		y = stan[i].SE;
		t[x][y] = 1;
	}

	bool typ = getTyp();
//	debug(typ);
//	wypisz();

	fup(i, 0, siz(stan) - 1) {
		int x, y;
		x = stan[i].FI;
		y = stan[i].SE;
		fup(j, 0, 3) {
			int xx, yy;
			int xxx, yyy;
			xx = x + nx[j];
			yy = y + ny[j];
			xxx = x - nx[j];
			yyy = y - ny[j];
			if (isok(xx, yy) && isok(xxx, yyy)) {
				if (co[xx][yy] != 1 && co[xxx][yyy] != 1 && t[xx][yy] == 0 && t[xxx][yyy] == 0) {
					t[x][y] = 0;
					t[xx][yy] = 1;	
					bool typ2 = getTyp();
					if (!(typ == 0 && typ2 == 0)) {
						vector<pair<int, int> > st = getStan();
						sort(ALL(st));
						dodaj(st, d + 1);
					}
					t[x][y] = 1;
					t[xx][yy] = 0;
				}
			}
		}
	}
			
}

bool ok(vector<pair<int, int> > stan) {
	fup(i, 0, siz(stan) - 1) {
		int x, y;
		x = stan[i].FI;
		y = stan[i].SE;
		if (co[x][y] != 2) return false;
	}
	return true;
}


int main(){
	int cas;
	cin >> cas;
	fup(i, 1, cas) {
		//cout << endl;
		mapa.clear();
		CLR(done);
		while (!Q.empty()) Q.pop();
		CLR(co);
		CLR(t);
		cin >> h >> w;
		vector<pair<int, int> > st;
		fup(i, 1, h) { 
			fup(j, 1, w) {
			char c;
			cin >> c;
	//		cout << c;
			if (c == '.') continue;
			if (c == '#') { co[i][j] = 1; continue; }
			if (c == 'o') { st.PB(MP(i, j)); continue; }
			if (c == 'w') { st.PB(MP(i, j)); co[i][j] = 2; }
			if (c == 'x') { co[i][j] = 2; }
		}
	//		cout << endl;
		}
	//	debug(siz(st));
		/*
		fup(i, 1, h) {
			fup(j, 1, w) cout << co[i][j];
			cout << endl;
		}*/
		N = siz(st);
		sort(ALL(st));
		mapa[st] = 0;
		Q.push(st);
		int best = -1;
		while (!Q.empty()) {
			vector<pair<int, int> > stan = Q.front();
			Q.pop();

			int d = mapa[stan];
			if (ok(stan)) {
				best = d; 
				break;
			}
			go(stan);
		}
	//	cout << best << endl;
		printf("Case #%d: %d\n", i, best);
	}
	return 0;	
}


