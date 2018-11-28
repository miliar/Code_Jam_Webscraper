#include<cstring>
#include<cstdio>
#include<cstring>
#include<cmath>
#define MAX_N 110
using namespace std;
int N;
char s[MAX_N][MAX_N];
double wp[3][MAX_N], m[MAX_N];
void solve(){
	for(int i=0;i<N;++i){
		wp[0][i] = wp[1][i] = wp[2][i] = 0.0;
	}
	for(int i=0;i<N;++i){
		m[i] = 0.0;
		for(int j=0;j<N;++j){
			if(s[i][j] != '.'){
				m[i] += 1.0;
			}
			if(s[i][j] == '1'){
				wp[0][i] += 1.0;
			}
		}
		wp[0][i] = wp[0][i] / m[i];
	}
	for(int k=1;k<3;++k){
		for(int i=0;i<N;++i){
			for(int j=0;j<N;++j){
				if(s[i][j] != '.'){
					if(k == 1){
						if(s[i][j] == '1'){
							wp[k][i] += (wp[k-1][j] * m[j] - 0.0) / (m[j] - 1.0);
						}
						else{
							wp[k][i] += (wp[k-1][j] * m[j] - 1.0) / (m[j] - 1.0);
						}
					}
					else{
						wp[k][i] += wp[k-1][j];
					}
				}
			}
			wp[k][i] = wp[k][i] / m[i];
		}
	}
	for(int i=0;i<N;++i){
		double res = 0.0;
		res += wp[2][i] * 0.25;
		res += wp[1][i] * 0.50;
		res += wp[0][i] * 0.25;
		printf("%.10lf\n", res);
	}
}
int main(){
	int T;
	scanf("%d", &T);
	for(int k=0;k<T;++k){
		scanf("%d", &N);
		for(int i=0;i<N;++i){
			scanf("%s", s[i]);
		}
		printf("Case #%d:\n", k+1);
		solve();
	}
	return 0;
}
