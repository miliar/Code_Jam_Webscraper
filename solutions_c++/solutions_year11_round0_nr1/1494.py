#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#define MAX 100
using namespace std;
int T, N;
char R[MAX];
int P[MAX];
int solve(){
	int res, t, bx, ox;
	char c = 'X';
	bx = ox = 1;
	res = t = 0;
	for(int i=0;i<N;++i){
		int *x;
		if(R[i] == 'B'){
			x = &bx;
		}
		else{
			x = &ox;
		}
		if(R[i] != c){
			res += t;
			t = max(abs(P[i] - *x) + 1 - t, 1);
		}
		else{
			t += abs(P[i] - *x) + 1;
		}
		*x = P[i];
		c = R[i];
	}
	res += t;
	return res;
}
int main(){
	scanf("%d", &T);
	for(int t=1;t<=T;++t){
		scanf("%d", &N);
		for(int i=0;i<N;++i){
			char str[8];
			scanf("%s%d", str, &P[i]);
			R[i] = str[0];
		}
		printf("Case #%d: %d\n", t, solve());
	}
	return 0;
}
