
#include <cstdio>
#include <iostream>

using namespace std;

int r[50];

int ans(int level, int n){
	
	if(level == n-1){
		return 0;
	}
	
	int k, x;

	for(int i=level; i<n; ++i){
		if(r[i] <= level){
			k = i;
			x = r[i];
			break;
		}
	}

	for(int i=k; i>=level+1; i--){
		r[i] = r[i-1];
	}
	r[level] = x;

	return ans(level+1, n)+k-level;
}

int main(){
	
	int T; cin >> T;

	char s[50][50];

	for(int testcase=1; testcase <=T; ++testcase){
		
		int N; cin >> N;

		for(int i=0; i<N; ++i){
			scanf("%s", s[i]);
		}

		for(int i=0; i<N; ++i){
			r[i] = 0;
			for(int j=N-1; j>0; j--){
				if(s[i][j] == '1'){
					r[i] = j;
					break;
				}
			}
		}

		printf("Case #%d: %d\n", testcase, ans(0, N));
	}
	return 0;
}
