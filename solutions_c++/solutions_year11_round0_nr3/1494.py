#include<cstdio>
#include<algorithm>
#define MAX_N 1010
#define INF 1000000000
using namespace std;
int T, N;
int C[MAX_N];
int solve(){
	int res, t, sum, x;
	sum = x = 0;
	t = INF;
	for(int i=0;i<N;++i){
		t = min(t, C[i]);
		sum = sum + C[i];
		x = x ^ C[i];
	}
	if(x != 0){
		res = -1;
	}
	else{
		res = sum - t;
	}
	return res;
}
int main(){
	int res;
	scanf("%d", &T);
	for(int t=0;t<T;++t){
		scanf("%d", &N);
		for(int i=0;i<N;++i){
			scanf("%d", &C[i]);
		}
		printf("Case #%d: ", t+1);
		res = solve();
		if(res == -1){
			printf("NO\n");
		}
		else{
			printf("%d\n", res);
		}
	}
	return 0;
}
