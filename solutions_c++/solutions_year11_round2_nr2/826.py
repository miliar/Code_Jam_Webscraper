#include <iostream>

using namespace std;

int list[1000000];
int num[1000000];
int dp[1000000];
int main(){
	int n, counter = 0, ans, x, d;
	cin >> n;
	while (n--){
		ans = 0;
		memset(list, 0, sizeof list);
		memset(num, 0, sizeof num);
		memset(dp, 0, sizeof dp);
		cin >> x >> d;
		for (int i = 0; i < x; i++){
			cin >> list[i] >> num[i];
			if(i)
				dp[i] =dp[i-1] + num[i];
			else
				dp[i] = list[i];
		}
		for (int i = 0; i < x; i++){
			for (int j = i+1; j < x; j++){
				ans = max(ans, (dp[j] - dp[i] + num[i] - 1)* d  - (list[j]-list[i]));
			}
		}
		for (int i = 0; i < x; i++){
			ans = max(ans, (num[i]-1)*d);
		}
		printf("Case #%d: %.1f\n", ++counter, ans/2.0);
	}
}
