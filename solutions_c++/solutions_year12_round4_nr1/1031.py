#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;
int d[10001], l[10001];
int D;
int dp[10001];
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int n;
		cin >> n;
		for(int i = 0; i < n; i++){
			scanf("%d%d", &d[i], &l[i]);
		}
		cin >> D;
		memset(dp, 0, sizeof dp);
		dp[0] = min(l[0], d[0]);
		bool ans = false;
		for(int i = 0; i < n; i++){
			if(dp[i]){
				for(int j = i + 1; j < n && d[i] + dp[i] >= d[j]; j++){
					dp[j] = max(dp[j], min(d[j] - d[i], l[j]));
				}
			}
			if(dp[i] + d[i] >= D){
				ans = true;
				break;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if(ans)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
