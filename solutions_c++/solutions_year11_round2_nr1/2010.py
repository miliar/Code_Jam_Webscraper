#include <cstdio>
#include <deque>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int T;

char inp[128][128];
int cnt[128];
int win[128];
int mat[128][128];
int dp[128][128];
double owp[128];
double wp[128], oowp[128];

double rpi(int N){
	for (int p=0;p<N;++p){
		wp[p]  = (double)win[p] / (double)cnt[p];
		double OWP = 0.0f;
		
		for (int i=0;i<N;++i){
			if (inp[p][i] != '.'){
				int w = win[i];
				int c = cnt[i]-1;
				if (inp[p][i] == '0'){
					--w;
				}
				OWP += ((double)w / (double)c);
			}
		}
		OWP /= (double)cnt[p];
		owp[p] = OWP;
	}
	
	for (int p=0;p<N;++p){
		oowp[p] = 0.0f;
		for (int i=0;i<N;++i){
			if (inp[p][i] != '.'){
				oowp[p] += owp[i];
			}
		}
		oowp[p] /= (double)cnt[p];
	}
	for (int p=0;p<N;++p){
		//printf("%d %lf %lf %lf\n", p, wp[p],owpoowp[p]);
		printf("%.10lf\n", wp[p] / 4.0f + owp[p] / 2.0f + oowp[p] / 4.0f);
	}
}

void solve(){
	int N;
	scanf(" %d", &N);
	memset(mat, 0, sizeof mat);
	
	for (int i=0;i<N;++i){
		scanf(" %s", inp[i]);
		cnt[i] = 0;
		win[i] = 0;
		for (int j=0;j<N;++j){	
			if (inp[i][j] == '.' ){
				mat[i][j] =0 ;
			}else{
				cnt[i]++;
				if (inp[i][j] == '1') win[i]++;
				mat[i][j] = inp[i][j] - '0';
			}
		}
	}
	memset(dp, 0, sizeof dp);
	for (int i=0;i<N;++i){
		for (int j=0;j<N;++j){
			dp[i][j] = mat[i][j];
			if (i) dp[i][j] += dp[i-1][j];
			if (j) dp[i][j] += dp[i][j-1];
			if (i && j) dp[i][j] -= dp[i-1][j-1];
		}
	}
	
	rpi(N);
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		printf("Case #%d:\n", tc);
		solve();
	}

	return 0;
}

