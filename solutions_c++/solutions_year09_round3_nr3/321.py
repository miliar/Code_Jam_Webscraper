#include <cstdio>
#include <algorithm>

int eval(int len, int arr[]){
	bool flg = false;
	int ret = INT_MAX;
	for(int i = 0; i < len; i++){
		if(!arr[i]) continue;
		flg = true;
		ret = std::min(ret, len - 1 + eval(i, arr) + eval(len - i - 1, arr + i + 1));
	}
	return flg * ret;
}

int main(){
	int N = 0;
	scanf("%d ", &N);
	for(int nnn = 1; nnn <= N; nnn++){
		int P = 0, Q = 0;
		int q_arr[10000] = {0};
		scanf("%d %d ", &P, &Q);
		for(int i = 0; i < Q; i++){
			int x = 0;
			scanf("%d ", &x);
			q_arr[x - 1] = 1;
		}
		printf("Case #%d: %d\n", nnn, eval(P, q_arr));
	}
	return 0;
}
