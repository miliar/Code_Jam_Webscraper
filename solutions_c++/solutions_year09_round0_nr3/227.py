#include <iostream>
#include <cstring>
#include <iomanip>
using namespace std;

const int MOD = 10000;
const char pstr[] = "welcome to code jam";
int dp[30][600];

char str[1000];

int calc(){
	memset(dp, 0, sizeof(dp));
//	dp[0][0] = 1;
	int len = strlen(str);
	for(int i = 0; i < len; ++i)
		if(str[i] == pstr[0])
			dp[1][i+1] = 1;
	
	for(int i = 0; i < 19; ++i)
		for(int j = 0; j < len; ++j){
			dp[i+1][j+1] += dp[i+1][j];
			if(pstr[i] == str[j]){
				dp[i+1][j+1] += dp[i][j];
			}
			dp[i+1][j+1] %= MOD;
	//		if(dp[i+1][j+1])cout<<i<<' '<<j<<' '<<dp[i+1][j+1]<<endl;
		}
	return dp[19][len];
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int N, ans;
	cin>>N;
	cin.ignore();
	for(int t = 1; t <= N; ++t){
		cin.getline(str, 900);
		ans = calc();
//		cout<<str<<endl;
		cout<<"Case #"<<t<<": "<<setw(4)<<setfill('0')<<ans<<endl;
	}
	return 0;
}
