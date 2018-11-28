#include <iostream>
#include <string.h>
#include <algorithm>

#define R(i,j) for(int i=0; i<j; i++)
#define INF 0x3f3f3f3f

using namespace std;

int dp[1001][1001];
int P, C, L;

int f(int l, int b){
	if (l*C >= b) return 0;

	if (dp[l][b] != -1) return dp[l][b];

	int sol = INF;

	for (int i=1;l+i<b;i++){
		sol = min(sol,1+max(f(l+i,b),f(l,l+i)));
	}

	dp[l][b] = sol;

	return sol;
}

int main(){
	int T;
	cin >> T;
	for (int casos=1;casos<=T;casos++){
		memset(dp,-1,sizeof dp);
		cin >> L >> P >> C;
		cout << "Case #" << casos << ": " << f(L,P) << endl;
	}
	return 0;
}