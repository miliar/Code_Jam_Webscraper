#include <cstdio>
#include <deque>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

#define inf 1000000000LL

using namespace std;

int T;
int L, t, N, C;
int inc[1024];
int inp[1000005] = {0};
int memo[1024][1024];

int dp(int x, int l){
	if (x == N) return 0;
	int tr = 0,t=inf;
	
	if (memo[x][l] != -1) return memo[x][l];
	
	tr = dp(x+1, l) + inp[x] * 2;
	if (l) t = dp(x+1,l-1) + inp[x];
	if (t < tr) tr = t;
	
	memo[x][l] = tr;
	return tr;
}

void solve(){
	int i,j;
	scanf(" %d %d%d%d", &L, &t, &N, &C);
	for (i=0;i<C;++i){
		scanf(" %d", &inc[i]);
	}
	
	for (i=0;i<N;++i){
		inp[i] = inc[i % C];
	}
	
	long long offset = 0;
	for (i=0;i<N;++i){
		if (offset + inp[i]*2 > t) break;
		offset += inp[i] * 2;
	}
	if (offset + inp[i]*2 > t){
		int diff = t - offset;
		// distance travelled here = diff / 2;
		inp[i] -= diff/2;
		offset = t;
		
		memset(memo, -1, sizeof memo);
		printf("%lld\n", offset + dp(i, L));
	}else{
		printf("%lld\n", offset);
	}
	
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		printf("Case #%d: ", tc);
		solve();
	}

	return 0;
}

