#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

struct point {
	LD x, y;
	point(LD _x=0.0, LD _y=0.0) : x(_x), y(_y) {}
};

LD cross(const point &o, const point &a, const point &b) {
	return (a.x-o.x)*(b.y-o.y)-(a.y-o.y)*(b.x-o.x);
}

LD pole(vector<point> &P) {
	LD res=0.0;
	FOR(i,2,SZ(P))
		res+=cross(P[0],P[i-1],P[i]);
	return fabsl(res);
}

vector<point> U, D; int W; LD P;

LD get(LD sto) {
	LD l=1e-12, r=W-1e-9, mid;
	for(int i=0; i<100; ++i) {
		mid=(l+r)*0.5;
		vector<point> up, down;
		REP(j,SZ(D)) {
			if(D[j].x<mid)
				down.PB(D[j]);
			else {
				LD t=(mid-D[j-1].x)/(D[j].x-D[j-1].x);
				down.PB(point(mid, D[j-1].y+t*(D[j].y-D[j-1].y)));
			}
		}
		REP(j,SZ(U)) {
			if(U[j].x<mid)
				up.PB(U[j]);
			else {
				LD t=(mid-U[j-1].x)/(U[j].x-U[j-1].x);
				up.PB(point(mid, U[j-1].y+t*(U[j].y-U[j-1].y)));
			}
		}
		for(int j=SZ(down)-1; j>=0; --j)
			up.PB(down[j]);
		LD ss=pole(up)/P;
		if(ss<sto)
			l=mid;
		else
			r=mid;
	}
	return 0.5*(l+r);
}
				
int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		fprintf(stderr, "%d\n", t);
		U.clear(); D.clear();
		vector<point> Q;
		int n, m, G; scanf("%d%d%d%d", &W, &n, &m, &G);
		REP(i,n) {
			point tmp;
			scanf("%Lf%Lf", &tmp.x, &tmp.y);
			D.PB(tmp);
		}
		REP(i,m) {
			point tmp;
			scanf("%Lf%Lf", &tmp.x, &tmp.y);
			U.PB(tmp);
		}
		Q=D;
		for(int i=SZ(U)-1; i>=0; --i)
			Q.PB(U[i]);
		P=pole(Q);
		vector<LD> res;
		FOR(i,1,G) {
			LD sto=(0.0+i)/(0.0+G);
			//printf("%Lf\n", sto);
			res.PB(get(sto));
		}
		printf("Case #%d:\n", t);
		REP(i,SZ(res))
			printf("%Lf\n", res[i]);
	}
	return 0;
}
