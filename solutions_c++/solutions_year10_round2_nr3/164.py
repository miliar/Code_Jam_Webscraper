
#include <iostream>

using namespace std;

int main(){
	
	int s[501][501];
	int c[501][501];

	c[0][0] = 1;
	for(int i=1; i<501; ++i){
		c[i][0] = 1;
		for(int j=1; j<501; ++j){
			if(j < i){
				c[i][j] = (c[i-1][j-1]+c[i-1][j])%100003;
			}else if(i==j){
				c[i][j] = 1;
			}else{
				c[i][j] = 0;
			}
		}
	}

	for(int i=0; i<501; ++i){
		for(int j=0; j<501; ++j){
			s[i][j] = 0;
		}
		if(i > 1){
			s[i][1] = 1;
		}
	}

	for(int i=3; i<501; ++i){
		for(int j=2; j<i; ++j){
			for(int k=0; k<=j-2; ++k){
				long long x = c[i-j-1][k];
				x *= s[j][j-k-1];
				s[i][j] = (x+s[i][j])%100003;
			}
		}
	}
	int T; cin >> T;
	int N;

	for(int testcase=1; testcase<=T; ++testcase){
		cin >> N;
		long long ans = 0;
		for(int i=1; i<=N-1; ++i){
			ans += s[N][i];
		}
		ans %= 100003;
		cout << "Case #" << testcase << ": " << ans << endl;
	}

	return 0;
}
