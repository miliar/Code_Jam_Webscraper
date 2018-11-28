#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;

const int INF = (1<<29);

int P, P2;
int M[1<<13];

int tree[1<<13];
int last;

ll memo[1<<13][20];

ll f(int root, int missed) {
	if(root > last) {
		root -= last+1;
		return (M[root] >= missed)?0:INF;
	}
	ll &result = memo[root][missed];
	if(result != -1) return result;
	result = f(2*root, missed+1) + f(2*root+1, missed+1);
	result = min(result, tree[root] + f(2*root, missed) + f(2*root+1, missed));
	return result;
}


ll solve() {
	scanf("%d", &P);
	P2 = (1<<P);
	for(int i = 0; i < P2; i++) scanf("%d", &M[i]);


	last = 0;
	for(int i = 0; i < P; i++) {
		for(int j = 0; j < (1<<(P-i-1)); j++) {
			scanf("%d", &tree[(1<<(P-i-1))+j]);		
			last = max(last, (1<<(P-i-1))+j);
		}
	}

	//for(int i = 0; i < 2*P2; i++) printf("%d ", tree[i]);
	
	memset(memo, -1, sizeof(memo));
	return f(1, 0);


}
int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %lld\n", i, solve());
}