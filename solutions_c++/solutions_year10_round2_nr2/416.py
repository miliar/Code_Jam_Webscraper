#include <iostream>
#include <algorithm>
using namespace std;

const int N = 55;
int x[N], v[N];
int cand[N];


int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int CASE;
	scanf("%d", &CASE);
	for(int cas = 1; cas <= CASE; ++cas){
		int n, K, B, T, res = 0;
		scanf("%d%d%d%d", &n, &K, &B, &T);
		for(int i = 0; i < n; ++i){
			scanf("%d", &x[i]);
		}
		for(int i = 0; i < n; ++i){
			scanf("%d", &v[i]);
		}
		int m = 0;
		for(int i = 0; i < n; ++i){
			if(x[i] + v[i] * T >= B){
				cand[m++] = x[i];
			}
		}
		if(m < K){
			printf("Case #%d: IMPOSSIBLE\n", cas);
			continue;
		}
		for(int i = 0; i < n; ++i){
			if(binary_search(cand + m - K, cand + m, x[i])){
				for(int j = i + 1; j < n; ++j){
					res += !binary_search(cand + m - K, cand + m, x[j]);
				}
			}
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}