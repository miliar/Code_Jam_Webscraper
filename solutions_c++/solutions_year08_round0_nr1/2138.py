#include <cstdio>
#include <cstring>

const int LEN = 128, INF = 1 << 20;
char name[128][LEN];
int pos[1024][128];
int dp[1024][128];
int id[1024];
int S, Q;

int getId(char *str){
	for(int i = 0; i < S; ++i) if(strcmp(str, name[i]) == 0) return i;
}

int main(){
	int nCase;
	scanf("%d", &nCase);
	for(int ca = 1; ca <= nCase; ++ca){
		scanf("%d\n", &S);
		for(int i = 0; i < S; ++i){
			gets(name[i]);
		}
		scanf("%d\n", &Q);
		char tmp[LEN];
		for(int i = 0; i < Q; ++i){
			gets(tmp);
			id[i] = getId(tmp);
		}
		memset(pos, -1, sizeof(pos));
		for(int j = 0; j < S; ++j){
			for(int i = Q - 1; i >= 0; --i){
				pos[i][j] = id[i] == j ? i : pos[i + 1][j];
			}
		}
		memset(dp, 0, sizeof(dp));
		for(int i = Q - 1; i >= 0; --i){
			for(int j = 0; j < S; ++j){
				if(pos[i][j] > i){
					int min = INF;
					for(int k = 0; k < S; ++k){
						min <?= dp[pos[i][j]][k] + 1;
					}
					dp[i][j] = min;
				}
				else if(pos[i][j] == -1){
					dp[i][j] = 0;
				}
			}
			int pidx, min = INF;
			for(int j = 0; j < S; ++j){
				if(pos[i][j] != i){
					min <?= dp[i][j] + 1;
				}else{
					pidx = j;
				}
			}
			dp[i][pidx] = min;
		}
		int ans = INF;
		for(int j = 0; j < S; ++j) ans <?= dp[0][j];
		printf("Case #%d: %d\n", ca, ans);
	}
	return 0;
}
