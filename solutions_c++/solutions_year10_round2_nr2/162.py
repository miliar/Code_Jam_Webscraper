#include <iostream>

using namespace std;

int main(){
	
	int C; cin >> C;
	int N, K, B, T;
	int x[1000];
	int v[1000];
	int s[1000];
	int ans;

	for(int testcase=1; testcase <=C; ++testcase){
		cin >> N >> K >> B >> T;
		ans = 0;
		for(int i=0; i<N; ++i){
			cin >> x[i];
		}
		for(int i=0; i<N; ++i){
			cin >> v[i];
		}
		for(int i=0; i<N; ++i){
			if(B-x[i] <= v[i]*T){
				s[i] = 1;
			}else{
				s[i] = 0;
			}
		}
		for(int i=N-1; i>=0 && K > 0; --i){
			if(s[i] == 1){
				--K;
				for(int j=i+1; j<N; ++j){
					if(s[j] == 0){
						++ans;
					}
				}
			}
		}
		if(K == 0){
			printf("Case #%d: %d\n", testcase, ans);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", testcase);
		}
	}
	return 0;
}
