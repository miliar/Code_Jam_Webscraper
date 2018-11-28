#include <string>
#include <cstring>
#include <set>
#include <cmath>
using namespace std;
#include <iostream>
#include <cstdio>

//By chyx111
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

const int MAXN = 256;
int mat[MAXN][MAXN];
int mother[MAXN][MAXN];

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int K; cin>>K;
		memset(mat,-1,(sizeof mat));
		
		Rep(s,2*K-1){
			for(int i = 0; i <= s; ++i)if( i < K && s - i < K){
				scanf("%d", &mat[i][s-i]);
			}
		}

		Rep(i,K){
			Rep(j,K){
				fprintf(stderr, "%d ", mat[i][j]);
			}
			fprintf(stderr, "\n");
		}

		int ans = 0;
		for(int L = K; ;++L)Rep(r,L-K+1)Rep(c,L-K+1){
			memset(mother,-1,(sizeof mother));
			Rep(i,K)Rep(j,K){
				mother[i+r][j+c] = mat[i][j];
			}

			bool ok = true;
			Rep(i,L)if(ok)Rep(j,L)if( mother[i][j] != -1){
				int other = mother[L-j-1][L-i-1];
				if( other != -1 && mother[i][j] != other){
					ok = false;
					break;
				}
				other = mother[j][i];
				if( other != -1 && mother[i][j] != other){
					ok = false;
					break;
				}
			}
			if( ok ){
				ans = L*L-K*K;
				goto out;
			}
		}
out:
		printf("Case #%d: ", ica+1);
		printf("%d\n", ans);
	}
	return 0;
}

