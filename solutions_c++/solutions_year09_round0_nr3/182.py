#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstring>
using namespace std;

int dp[2][501];

int main()
{
	string ref = "welcome to code jam";

	cout << setfill('0');

	int N;
	cin >> N;
	cin.ignore();

	for(int t=1 ; t<=N ; t++)
	{
		char str[501];
		cin.getline(str, 501);

		memset(dp, 0, sizeof(dp));

		for(int i=0 ; i<strlen(str) ; i++)
			if(str[i] == ref[0])
				dp[0][i] = 1;

		int i;
		for(i=1 ; i<ref.size() ; i++)
		{
			for(int j=0 ; str[j] ; j++)
				if(str[j] == ref[i])
				{
					int r = 0;
					for(int k=0 ; k<j ; k++)
					{
						r += dp[(i+1)%2][k];
						r %= 10000;
					}
					dp[i%2][j] = r;
				}
				else
					dp[i%2][j] = 0;
		}

		int res = 0;
		for(int j=0 ; str[j] ; j++)
		{
			res += dp[(i+1)%2][j];
			res %= 10000;
		}

		cout << "Case #" << t << ": " << setw(4) << res << endl;
	}

	return 0;
}
