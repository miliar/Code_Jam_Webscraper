#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int _n=n,i=0;i!=_n;++i)
#define CL(v,x) memset((v),(x),sizeof(v))
#define SZ(v) (int)(v).size()

typedef long long ll;

const int MAXN = 2050;
const ll inf = 100000000000LL;
ll F[MAXN][MAXN];
int view[MAXN];
int cost[MAXN];
int N, P;

ll solve(int i, int j) {
	if (i >= N) {
		if (j >= view[i]) return 0; else return inf;
	}
	ll& ret = F[i][j];
	if (ret != -1) return ret;

	ret = solve(i+i, j+1) + solve(i+i+1, j+1) + cost[i];
	ll tmp = solve(i+i, j) + solve(i+i+1, j);
	if (tmp < ret) ret = tmp;
	return ret;
}

int main(){
	freopen("input.in", "r", stdin);
	int T;
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d", &P);
		N = 1 << P;
		CL(view,0);
		CL(cost,0);
		REP(i,N) {
			int k;
			scanf("%d", &k);
			view[i+N] = P - k;
		}
		for (int i=P-1;i>=0;--i) {
			int len = 1 << i;
			for (int j=0;j<len;++j) {
				int k;
				scanf("%d", &k);
				cost[len+j] = k;
			}
		}	
		CL(F,-1);
		printf("Case #%d: %lld\n", t+1, solve(1,0));
	}
	return 0;
}
