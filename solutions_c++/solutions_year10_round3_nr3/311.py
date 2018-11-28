#include<cstdio>
#include<algorithm>
#include<cmath>
#include<set>

using namespace std;

set<int> st;
int cnt[109];
char flag[35][35];
int arr[35][35];
char str[109];

int main(){
	int T, X, M, N, a, ret, i, j, k,l, m, r, c, col;
	bool ok;
	char ch[5]; ch[1] = 0;
	
	freopen("C-small-attempt0.in", "r", stdin); freopen("C-small.out", "w", stdout);
	scanf("%d", &T);

	for( X = 1; X<=T; ++X){
		scanf("%d%d", &M, &N);

		st.clear();
		memset(cnt, 0, sizeof(cnt));
		for( i = 0; i<M; ++i){
			scanf("%s", str);
			for(j = 0; j<N; ++j){
				ch[0] = str[j/4];
				sscanf(ch,"%Xd", &a);
				arr[i][j] = (a & (1<<(3-j%4)))!=0;
				//printf("%d", arr[i][j]);
			}
			//puts("");
		}

		memset(flag, 0, sizeof(flag));
		for( k = min(M, N); k>=1; --k){
			for(i = 0; i+k<=M; ++i){
				for( j = 0; j+k<=N; ++j){
					col = arr[i][j];
					ok = true;
					for(l = 0; l<k; ++l){
						for( m = 0; m<k; ++m){
							r = i+l; c = j+m;
							if(flag[r][c]){
								ok = false;
								goto hell;
							}
							if( (arr[r][c] + l+m)%2 != col){
								ok = false; goto hell;
							}
						}
					}
hell:;
					if(ok) {
						st.insert(k);
						cnt[k]++;
						for(l = 0; l<k; ++l){
							for( m = 0; m<k; ++m){
								flag[i+l][j+m] = 1;
							}
						}
					}
				}
			}
		}

		printf("Case #%d: %d\n", X, st.size());
		for( i = 32; i>0; --i){
			if(cnt[i]) printf("%d %d\n", i, cnt[i]);
		}


	}

	return 0;
}