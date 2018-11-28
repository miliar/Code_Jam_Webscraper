#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int dp[19][501];
string s;
string ss;

int get(int i, int j) {
	if (i==s.size()) return 1;
	if (j==ss.size()) return 0;
	if (dp[i][j]==-1) {
		dp[i][j]=get(i,j+1);
		if (ss[j]==s[i]) dp[i][j]+=get(i+1,j+1);
		dp[i][j]%=10000;
	}
	return dp[i][j];
}

int main() {
	s = "welcome to code jam";
	int T;
	string dummy;
	cin >> T;
	getline(cin,dummy);
	for (int t=1;t<=T;++t) {
		getline(cin,ss);
		memset(dp,-1,sizeof(dp));
		cout << "Case #" << t << ": ";
		cout.fill('0');
		cout.width(4);
		cout << get(0,0) << endl;
	}
}

