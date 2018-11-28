#include <string>
#include <fstream>
#include <iostream>

using namespace std;
#define min(x,y)  ((x)<(y)?(x):(y))
int main()
{
	int T;

	ifstream is("1.txt");
	ofstream os("2.txt");

	is >> T;

	int i, j, k, m, n;

	int dp[505][20];

	string s, ret;
	string t="welcome to code jam";
	getline(is, s);

	for(k=0; k<T; k++)
	{
		getline(is, s);
		
		n = s.size(), m = t.size();

		memset(dp, 0, sizeof(dp));

		dp[0][0] = s[0] == t[0];

		for(i=1; i<n; i++)
			for(j=0; j< min(i+1, m); j++)
			{
				if(s[i] == t[j])
					dp[i][j] = dp[i-1][j] + (j==0 ? 1:dp[i-1][j-1]);
				else
					dp[i][j] = dp[i-1][j];

				dp[i][j] %= 10000;

			}

		int tmp = dp[n-1][m-1];



		os << "Case #"<< k+1 << ": ";
		os.width(4);
		os.fill('0');
		os << tmp  << endl;
	}


	return 0;

}