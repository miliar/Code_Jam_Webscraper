#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

bool used[1010];
int dp[1010];
int main () {
	int T;
	cin >> T;
	memset(dp,-1,sizeof(dp));
	dp[0] = 0;
	dp[1] = 0;
	dp[2] = 2;
	for(int z = 3; z < 1001; z++) {
		dp[z] = 10000;
		for(int i = 1; i < z;i++) {
			dp[z] = min(dp[z],dp[i]+dp[z-i]+2);
		}
	}
	for(int caso = 1;caso <= T; caso++) {
		int N, a;
		cin >> N;
		vector<int> v(N,-1);
		for(int i = 0; i < N; i++ ) {
			cin >> a;a--;
			v[a] = i;
		}
		
		int total = 0;
		memset(used,0,sizeof(used));
		for(int i = 0; i < v.size(); i++) if(!used[i]) {
			if(v[i]!=i) {
				int ptr = i, clen = 0;
				used[ptr] = true;
				while(v[ptr]!=i) {
					clen++;
					ptr = v[ptr];
					used[ptr] = true;
				}
				used[v[ptr]] = true;
				total += clen+1;
			}
		}

		cout << "Case #" << caso << ": " << total << ".000000000" << endl;
	}
	return 0;
}

