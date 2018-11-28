
#include <cstdio>
#include <cmath>

int main(){
	
	int T;
	int P;
	int s[11][1024];
	int r[11];

	scanf("%d", &T);
	for(int testcase=1; testcase<=T; ++testcase){
		int P;
		scanf("%d", &P);
		int n = pow(2, P);
		for(int i=0; i<n; ++i){
			scanf("%d", &s[0][i]);
			s[0][i] = P-s[0][i];
		}
		int x;
		for(int i=0; i<n-1; ++i){
			scanf("%d", &x);
		}
		for(int i=1; i<=P; ++i){
			for(int j=0; j<n; ++j){
				s[i][j] = 0;
			}
		}
		for(int i=0; i<n; ++i){
			r[0] = i;
			for(int j=1; j<=P; ++j){
				r[j] = r[j-1]/2;
			}
			for(int j=P; j>P-s[0][i] && j>=0; --j){
				s[j][r[j]] = 1;
			}
		}
		int ans = 0;
		for(int i=0; i<n; ++i){
			for(int j=1; j<=P; ++j){
				ans += s[j][i];
			}
		}
		printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}
