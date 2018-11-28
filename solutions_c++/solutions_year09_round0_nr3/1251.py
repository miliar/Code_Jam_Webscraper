#include <iostream>

using namespace std;

string pat = "welcome to code jam";

void Load()
{

}
string s;
int dp[22][555];

void Solve()
{
	s = "";
	char c;
	c = getchar();
	while ((c < 'a' || c > 'z') && c != ' ') c =getchar();
	while (c != '\n' && c > 0) {
		s += c;
		c = getchar();
	}
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	int i, j;
	for (i = 0; i <= pat.size(); i++) {
		for (j = 0; j < s.size(); j++) {
			if (i < pat.size() && pat[i] == s[j]) {
				dp[i + 1][j + 1] += dp[i][j];
				dp[i + 1][j + 1] %= 10000;
			}
			dp[i][j + 1] += dp[i][j];
			dp[i][j + 1] %= 10000;
		}
	}
	int res = 0;
	for (i = 0; i < s.size() + 1; i++) {
		res += dp[pat.size()][i];
		res %= 10000;		
	}
	res = dp[pat.size()][s.size()];
	if (res < 1000) cout << "0";
	if (res < 100) cout << "0";
	if (res < 10) cout << "0";
	cout << res << "\n";
}



int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ii++) {
		cout << "Case #" << ii << ": ";
		Solve();
	}	
	return 0;
}