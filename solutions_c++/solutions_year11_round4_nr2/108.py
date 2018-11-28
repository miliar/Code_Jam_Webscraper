#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

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

int c[510][510]; char buf[510];
LL sx[510][510], sy[510][510], ma[510][510];

LL suma(int a, int b, int c, int d) {
	LL r=ma[c][d]-(a>0?ma[a-1][d]:0)-(b>0?ma[c][b-1]:0)+((a>0&&b>0)?ma[a-1][b-1]:0);
	return r;
}

LL sumx(int a, int b, int c, int d) {
	LL r=sx[c][d]-(a>0?sx[a-1][d]:0)-(b>0?sx[c][b-1]:0)+((a>0&&b>0)?sx[a-1][b-1]:0);
	return r-suma(a,b,c,d)*a;
}

LL sumy(int a, int b, int c, int d) {
	LL r=sy[c][d]-(a>0?sy[a-1][d]:0)-(b>0?sy[c][b-1]:0)+((a>0&&b>0)?sy[a-1][b-1]:0);
	return r-suma(a,b,c,d)*b;
}

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		int n, m, D; scanf("%d%d%d", &n, &m, &D);
		REP(i,n) {
			scanf("%s", buf);
			REP(j,m)
				c[i][j]=D+buf[j]-'0';
		}
		REP(i,n) {
			REP(j,m) {
				sx[i][j]=(LL)c[i][j]*i;
				if(i>0)
					sx[i][j]+=sx[i-1][j];
				if(j>0)
					sx[i][j]+=sx[i][j-1];
				if(i>0 && j>0)
					sx[i][j]-=sx[i-1][j-1];
				sy[i][j]=c[i][j]*j;
				if(i>0)
					sy[i][j]+=sy[i-1][j];
				if(j>0)
					sy[i][j]+=sy[i][j-1];
				if(i>0 && j>0)
					sy[i][j]-=sy[i-1][j-1];
				ma[i][j]=c[i][j];
				if(i>0)
					ma[i][j]+=ma[i-1][j];
				if(j>0)
					ma[i][j]+=ma[i][j-1];
				if(i>0 && j>0)
					ma[i][j]-=ma[i-1][j-1];
			}
		}
		int res=0;
		REP(i,n) {
			REP(j,m) {
				for(int k=3; i+k<=n && j+k<=m; ++k) {
					LL x, y, m;
					LL X=sumx(i, j, i+k-1, j+k-1)-(k-1)*(c[i+k-1][j]+c[i+k-1][j+k-1]);
					LL Y=sumy(i, j, i+k-1, j+k-1)-(k-1)*(c[i][j+k-1]+c[i+k-1][j+k-1]);
					LL M=suma(i, j, i+k-1, j+k-1)-c[i][j]-c[i+k-1][j]-c[i][j+k-1]-c[i+k-1][j+k-1];
					if(X*2LL==M*(k-1) && Y*2LL==M*(k-1)) {
						//printf("%d %d %d\n", i, j, k);
						res=max(res, k);
					}
				}
			}
		}
		if(res<3)
			printf("Case #%d: IMPOSSIBLE\n", t);
		else
			printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
