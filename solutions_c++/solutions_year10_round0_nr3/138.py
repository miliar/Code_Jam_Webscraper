#include <iostream>

using namespace std;

int main(){
	int T; cin >> T;
	for(int test=1;test<=T;test++){
		int R, K, N; cin >> R >> K >> N;
		long long sum = 0;
		int ride[1000];
		int pass[1000];
		int next[1000];
		for(int i=0;i<N;i++){
			cin >> ride[i];
			sum += ride[i];
		}
		if(sum <= K){
			printf("Case #%d: %lld\n", test, sum*R);
			continue;
		}
		for(int i=0;i<N;i++){
			int cur = 0;
			for(int j=0;j<N;j++){
				if(cur+ride[(i+j)%N] > K){
					pass[i] = cur;
					next[i] = (i+j)%N;
					break;
				}
				cur += ride[(i+j)%N];
			}
		}
		long long ans = 0;
		int idx = 0;
		for(int i=0;i<R;i++){
			ans += pass[idx];
			idx = next[idx];
		}
		printf("Case #%d: %lld\n", test, ans);
	}
}