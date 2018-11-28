#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	int N;
	int dp[510][30];
	char x[510];
	char y[] = "welcome to code jam";
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	
	int caseNo;
	int i, k;
	ifs >> N;
	ifs.getline(x, 510);
	for(caseNo = 1; caseNo <= N; ++caseNo)
	{
		ifs.getline(x, 510);
		int lenx = strlen(x);
		int leny = strlen(y);
	
		for(i = 0; i < lenx; ++i)
		{
			for(k = 0; k < leny; ++k)
			{
				if(i == 0)
				{
					if(k == 0 && x[i] == y[k])
						dp[i][k] = 1;
					else
						dp[i][k] = 0;
					continue;
				}

				dp[i][k] = dp[i-1][k] % 10000;
				if(x[i] == y[k])
				{
					if(k > 0)
					{
						dp[i][k] += dp[i-1][k-1];
						dp[i][k] %= 10000;
					}
					else
					{
						dp[i][k] += 1;
						dp[i][k] %= 10000;
					}
				}
			}
		}

		ofs << "Case #" << caseNo << ": " ;
		ofs.width(4);
		ofs.fill('0');
		ofs <<  dp[lenx-1][leny-1] << endl;
	}

	return 0;
}