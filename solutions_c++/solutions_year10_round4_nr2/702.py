#include <iostream>
#include <algorithm>

using namespace std;

int minmatch[4000];
long long dp[4000][20];
long long price[4000];
int P;


long long  dfs(int node,int wat, int rem){
	if( node >= ((1 << P)-1)) return 0;
	if(dp[node][wat] != -1){
		return dp[node][wat];
	}

	if(minmatch[node] <= wat) return 0;

	long long alt1 = 1000000000;
	long long alt2 = 1000000000;
	if(minmatch[node]-wat > rem){
		return 1000000000;
	}
	else if(minmatch[node]-wat == rem){
		alt1 = price[node];
		alt1+= dfs(2*(node+1)-1,wat+1,rem-1);
		alt1+= dfs(2*(node+1),wat+1,rem-1);
	}
	else{
		
		alt1 = price[node];
		alt1+= dfs(2*(node+1)-1,wat+1,rem-1);
		alt1+= dfs(2*(node+1),wat+1,rem-1);

		alt2 = dfs(2*(node+1)-1,wat,rem-1);
		alt2+=dfs(2*(node+1),wat,rem-1);

	}
	alt1 = min(alt1,alt2);
	dp[node][wat] = alt1;
	return dp[node][wat];
}


int main(){

	int T;
	cin >> T;
	for(int teller = 1; teller <= T; teller++){
		cin >> P;
		int start = 1 << P;
		start -= 1;
		for(int i = 0; i < 4000; i++){
			minmatch[i] = 0;
			for(int j = 0; j < 20; j++) dp[i][j] = -1;
		}
		for(int i = 0; i < (1 << P); i++){
			cin >> minmatch[start+i];
			minmatch[start+i] = P - minmatch[start+i];
		}
		for(int level = P; level >= 1; level--){
			for(int i = 0; i < (1 <<level); i++){
				int child = (1<<(level))-1+i;
				int parent = (child+1)/2-1;
				minmatch[parent] = max(minmatch[parent],minmatch[child]);
			}
		}
		for(int level = P-1; level >= 0; level--){
			int start = (1 << level)-1;
			for(int i = 0; i < (1 << level); i++){
				cin >> price[start+i];
			}
		}
		long long best = dfs(0,0,P);
		/*
		for(int i = 0; i < (1 << (P+1))-1; i++){
			cout << minmatch[i];
			if( i < (1 << P)-1) cout << "  x  " << price[i] << "  y  ";
			cout << endl;
		}
		for(int i = 0; i < (1 << P)-1; i++){
			cout << "i = " << i << ":  ";
			for(int j = 0; j <= 10; j++){
				cout << dp[i][j] << " " << endl;
			}
			cout << endl;
		}
		*/
		cout << "Case #" << teller << ": " << best << endl;
	}

}
