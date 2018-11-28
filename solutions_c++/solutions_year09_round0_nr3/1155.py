//dynamik
#include<iostream>
#include<string>
using namespace std;

#define MR 30
#define MS 10000
int dp[2][MR], n;
string s1, s2;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	s2 = "welcome to code jam";
	cin >> n;
	getline(cin, s1);
	for(int c = 0; c < n; c++)
	{
		getline(cin, s1);
		int sel = 0;
		//pusty ciag na kazdej pozycji wczytanego napisu wystepuje 1 raz
		dp[0][0] = dp[1][0] = 1;
		for(int i = 1; i <= s2.length(); i++)
			dp[sel][i] = 0;
		for(int i = 1; i <= s1.length(); i++)
		{
			sel = 1 - sel;
			for(int j = 1; j <= s2.length(); j++)
				if(s1[i-1] == s2[j-1])
					dp[sel][j] = (dp[1-sel][j-1] + dp[1-sel][j]) % MS;
				else
					dp[sel][j] = dp[1-sel][j] % MS;
		}
		int p = s2.length();
		if(dp[sel][p] < 10)
			cout << "Case #" << c+1 <<": 000" << dp[sel][p] << "\n";
		else if(dp[sel][p] < 100)
			cout << "Case #" << c+1 <<": 00" << dp[sel][p] << "\n";
		else if(dp[sel][p] < 1000)
			cout << "Case #" << c+1 <<": 0" << dp[sel][p] << "\n";
		else
			cout << "Case #" << c+1 <<": " << dp[sel][p] << "\n";
	}
	return 0;
}