#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const string welcome = "welcome to code jam";

int dp[20][501];

int main()
{
	fstream file("C-small.in");
	fstream output("C-small.out", ios_base::out);
	int caseCount;
	file >> caseCount;
	file.get();

	int caseIndex = 0;
	string line;
	while (++caseIndex <= caseCount)
	{
		getline(file, line);
		memset(dp, 0, sizeof(dp));
		for (int i = 0; i < line.length(); ++ i)
		{
			dp[19][i] = 1;
		}
		for (int i = 18; i >= 0; -- i)
		{
			for (int j = line.length() - 1; j >= 0; -- j)
			{
				dp[i][j] = dp[i][j + 1];
				if (line[j] == welcome[i]) {
					dp[i][j] += dp[i + 1][j];
				}
				dp[i][j] %= 10000;
			}
		}
		output << "Case #" << caseIndex << ": ";
		for (int i = 1000; i > 0; i /= 10)
		{
			output << dp[0][0] / i;
			dp[0][0] = dp[0][0] % i;
		}
		output << endl;
	}
	file.close();
	output.close();
	return 0;
}