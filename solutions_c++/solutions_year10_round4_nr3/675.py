#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <cmath>
using namespace std;
#include <iostream>
#include <cstdio>

//By chyx111
#define DBG(a) cerr << #a << ": " << (a) << endl
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

const int MAXN = 128;
int mat[MAXN][MAXN];
int tmp[MAXN][MAXN];

int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int R;
		memset(mat,0,(sizeof mat));
		
		int x, y, X, Y;
		cin>>R;
		Rep(r,R){
			scanf("%d%d%d%d", &x, &y, &X, &Y);
			for(int i = x; i <= X; ++i){
				for(int j = y; j <= Y; ++j){
					mat[i][j] = 1;
				}
			}
		}
		int ans = 0;
		memcpy(tmp,mat,(sizeof mat));
		
		for(;;){
			memcpy(mat,tmp,(sizeof mat));
			int cnt = 0;
			Rep(i,MAXN)Rep(j,MAXN)if( mat[i][j] )cnt++;
			//DBG(cnt);
			if( !cnt ){
				break;
			}
			ans++;
			for(int i = 1; i < MAXN; ++i)for(int j = 1; j < MAXN; ++j){
				if(mat[i][j]){
					if( !mat[i-1][j] && !mat[i][j-1]){
						tmp[i][j] = 0;
					}else{
						tmp[i][j] = 1;
					}
				}else{
					if( mat[i-1][j] && mat[i][j-1] ){
						tmp[i][j] = 1;
					}else{
						tmp[i][j] = 0;
					}
				}
			}
		}

		printf("Case #%d: ", ica+1);
		printf("%d\n", ans);
	}
	return 0;
}

