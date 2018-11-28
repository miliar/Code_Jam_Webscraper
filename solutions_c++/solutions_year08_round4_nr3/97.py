#define _CRT_SECURE_NO_DEPRECATE
#include<vector>
#include<algorithm>
#include<iostream>
#include<sstream>
using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define all(X) (X).begin(),(X).end()
#define FOR(I,S,N) for(int I=(S);I<(N);++I)
#define REP(I,N) FOR(I,0,N)

typedef vector<int> VI;

#define DIM 2000

int x[DIM],y[DIM],z[DIM],p[DIM],n;

double up[2][2], down[2][2];
bool can(double g)
{
	REP(i,2) REP(j,2) {
		up[i][j] = 1e15;
		down[i][j] = -1e15;
	}
	REP(i,n) {
		up[0][0] = min(up[0][0], g*p[i] + x[i] + y[i] + z[i]);
		down[0][0] = max(down[0][0], -g*p[i] + x[i] + y[i] + z[i]);
		up[0][1] = min(up[0][1], g*p[i] + x[i] + y[i] - z[i]);
		down[0][1] = max(down[0][1], -g*p[i] + x[i] + y[i] - z[i]);
		up[1][0] = min(up[1][0], g*p[i] + x[i] - y[i] + z[i]);
		down[1][0] = max(down[1][0], -g*p[i] + x[i] - y[i] + z[i]);
		up[1][1] = min(up[1][1], g*p[i] + x[i] - y[i] - z[i]);
		down[1][1] = max(down[1][1], -g*p[i] + x[i] - y[i] - z[i]);
	}
	REP(i,2) REP(j,2) if(up[i][j] < down[i][j]) return false;
	return true;
}
int main() {
	freopen("C-large.in","r",stdin);
	freopen("c-large.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	FOR(tn,1,tc+1) {
		scanf("%d",&n);
		REP(i,n) scanf("%d %d %d %d",&x[i],&y[i],&z[i],&p[i]);
		double l = 0, r = 1e15, m;
		int it = 0;
		while(r-l > 1e-8 && it < 150) {
			m = (l+r)/2;
			if(can(m)) r = m;
			else l = m;
			++it;
		}
		printf("Case #%d: %.7lf\n",tn,m);
	}
	fflush(stdout);
	return 0;
}