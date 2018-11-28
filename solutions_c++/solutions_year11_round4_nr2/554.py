#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

int iCase;
#define SIZMAX 505

struct xy {
	LL x, y;
	xy(): x(0), y(0) {}
	xy(LL _x, LL _y): x(_x), y(_y) {}
};

xy operator+(const xy &a, const xy &b) {
	return xy(a.x+b.x, a.y+b.y);
}
xy operator-(const xy &a, const xy &b) {
	return xy(a.x-b.x, a.y-b.y);
}
xy operator*(const xy &a, LL b) {
	return xy(a.x*b, a.y*b);
}

struct pole {
	long v;
	xy vec;
	xy vhoriz;	// suma w lewo
	xy vrect;	// suma w lewo i w górê
	LL mhoriz, mrect;	// suma wagi w lewo i w lewo&w górê
};
class Problem {
public:
	int R, C, D;
	pole M[SIZMAX][SIZMAX];

	xy vsum(long x, long y, long s) {
		xy center = M[y+s-1][x+s-1].vrect;
		if(x>0) center = center - M[y+s-1][x-1].vrect;
		if(y>0) center = center - M[y-1][x+s-1].vrect;
		if(x>0 && y>0) center = center + M[y-1][x-1].vrect;
		center = center - M[y][x].vec - M[y+s-1][x].vec - M[y][x+s-1].vec - M[y+s-1][x+s-1].vec;
		return center;
	}

	LL mass(long x, long y, long s) {
		LL center = M[y+s-1][x+s-1].mrect;
		if(x>0) center = center - M[y+s-1][x-1].mrect;
		if(y>0) center = center - M[y-1][x+s-1].mrect;
		if(x>0 && y>0) center = center + M[y-1][x-1].mrect;
		center = center - M[y][x].v - M[y+s-1][x].v - M[y][x+s-1].v - M[y+s-1][x+s-1].v;
		return center;
	}

	bool can(long s) {
		long kafle = s*s-4;
		for(int y=R-s+1; y-->0;) {
			for(int x=C-s+1; x-->0;) {
				xy correct(2*x+s, 2*y+s); 
				LL m = mass(x,y,s);
				correct = correct*m;

				xy center = vsum(x,y,s);
				if(center.x==correct.x && center.y==correct.y) 
					return true;
			}
		}
		return false;
	}

	void Solve() {
		// in
		cin>>R>>C>>D;
		REP(y,R) {
			string s;
			cin>>s;
			REP(x,C) {
				pole &p = M[y][x];
				p.v = (s[x]-'0')+D;
				p.vec = xy((2*x+1)*p.v, (2*y+1)*p.v);
			}
		}

		// prepare
		REP(y,R) {
			REP(x,C) {
				pole &p = M[y][x];
				if(x>0) p.vhoriz = p.vec + M[y][x-1].vhoriz;
				else p.vhoriz = p.vec;
				if(y>0) p.vrect = p.vhoriz + M[y-1][x].vrect;
				else p.vrect = p.vhoriz;
				if(x>0) p.mhoriz = p.v + M[y][x-1].mhoriz;
				else p.mhoriz = p.v;
				if(y>0) p.mrect = p.mhoriz + M[y-1][x].mrect;
				else p.mrect = p.mhoriz;
			}
		}

		// solve
		long odp=0;
		for(int s=min<int>(R,C); s>=3; --s) {
			if(can(s)) {
				odp = s;
				break;
			}
		}

		// out
		cout<<"Case #"<<iCase<<": ";
		if(odp>0) cout<<odp; else cout<<"IMPOSSIBLE";
		cout<<endl;

	}
};

int main() {
    ios_base::sync_with_stdio(0);

	int nCases; cin>>nCases;
	for(iCase=1; iCase<=nCases; ++iCase) {
		Problem *P = new Problem();
		P->Solve();
		delete P;
	}
	return 0;
}

/*

22
3 3 7
123
234
345
6 7 2
1111111
1122271
1211521
1329131
1242121
1122211


Case #1: 5
Case #2: IMPOSSIBLE

*/