#include <cmath>
using namespace std;
#include <string>
#include <cstring>
#include <cstdio>
#include <set>

//By chyx111
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

int const N = 128;
int arr[N];
int n, ns, least_score;

bool dp[N][N][N];
int solve()
{
	memset(dp, 0, (sizeof dp));
	dp[0][0][0] = 1;
	for(int i = 0; i < n; ++i){
		int base = (arr[i] + 2) / 3;
		Rep(j, N)Rep(k, N)if(dp[i][j][k]){
			bool way[4];
			memset(way, 0, (sizeof way));
			for(int ma = base; ma <= base + 1 && ma <= 10; ++ma){
				int d = ma * 3 - arr[i]; 
				if(d < 0){
					continue;
				}
				bool is_ok = ma >= least_score;
				if(d == 0){
					dp[i + 1][j + is_ok][k] = true;
				}else if(d == 1){
					if(ma - 1 >= 0){
						dp[i + 1][j + is_ok][k] = true;
					}
				}else if(d == 2){
					if(ma - 1 >= 0){
						dp[i + 1][j + is_ok][k] = true;
					}
					if(ma - 2 >= 0){
						dp[i + 1][j + is_ok][k + 1] = true;
					}
				}else if(d == 3 || d == 4){
					if(ma - 2 >= 0){
						dp[i + 1][j + is_ok][k + 1] = true;
					}
				}
			}
		}
	}
	for(int i = n; i >= 1; --i){
		if(dp[n][i][ns]){
			return i;
		}
	}
	return 0;
}

int main() {
	int ca;
	scanf("%d", &ca);
	Rep(ica, ca){
		scanf("%d%d%d", &n, &ns, &least_score);
		Rep(i, n){
			scanf("%d", arr + i);
		}
		printf("Case #%d: %d\n", ica + 1, solve());
	}
	return 0;
}

