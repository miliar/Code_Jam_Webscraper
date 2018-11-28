#include <iostream>
#include <string>

using namespace std;




string s1 = "welcome to code jam";
string s2;


int dp[31][3001];

void Load()
{
	char c;
	c = getchar();
	s2 = "";
	while (c == '\n') c = getchar();
	while (c != '\n')
	{
		s2 += c;
		c = getchar();
	}
	memset(dp, 0, sizeof(dp));
}


void Solve()
{

	int i, j;

//	s1  = "abc abc";
//	s2 = "abc abcc";
//	cerr << "\n  ";
	for (i = 0; i <= (int)s2.size(); i++)
	{
		dp[0][i] = 1;
//		cerr << s2[i] << ' ';
	}
//	cerr << "\n";



	for (i = 1; i <= (int)s1.size(); i++)
	{
//		cerr << s1[i] << ' ';
		for (j = 1; j <= (int)s2.size(); j++)
		{
			dp[i][j] = dp[i][j-1];
			if (s1[i-1] == s2[j-1])
				dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % 10000;
//			cerr << ((dp[i][j]<10)?dp[i][j]:(char)0) << " ";
		}
//		cerr << "\n";
	}
	i = dp[s1.size()][s2.size()];
	if (i < 1000) cout << "0";
	if (i < 100) cout << "0";
	if (i < 10) cout << "0";
	cout << i << "\n";

}

int main()
{
    int nt, tt;
    cin >> nt;
    for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
