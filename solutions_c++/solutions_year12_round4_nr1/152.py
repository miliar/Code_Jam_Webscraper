#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

#define MAXN 10100

int T, N, DD;
int D[MAXN], L[MAXN];
int acc[MAXN];

bool cmpi(int i1, int i2) {
	return D[i1] < D[i2];
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d", &N);
		REP(i,N) scanf("%d%d", D+i, L+i);
		scanf("%d", &DD);
		memset(acc, -1, sizeof acc);
		acc[0] = D[0];
		bool res = false;
		REP(i,N) {
			if (acc[i] != -1) {
				int j = i+1;
				while (j < N && D[j] <= D[i]+acc[i]) {
					acc[j] = max(acc[j], min(D[j]-D[i], L[j]));
					++j;
				}
			}
			if (acc[i]+D[i] >= DD) res = true;
		}
		printf("Case #%d: ", t+1);
		if (res) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
