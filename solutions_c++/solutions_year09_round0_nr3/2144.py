#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
#define NUM 10000

int main()
{
	string blah;
	int N;
	//cin >> N;
	getline(cin,blah);
	N = atoi(blah.data());
	for(int testCase = 0; testCase < N; testCase++)
	{
		string g;
		getline(cin,g);
		//cout << "g is " << g << endl;
		
		string x = "welcome to code jam";
		//string x;
		//cin >> x;
		long long dp[g.size()+1][x.size()+1];
		memset(dp,0,sizeof(dp));
		
		//dp[0][0] = 1;
		
		for(int i = 0; i <= g.size();i++)
			dp[i][0] = 1;
		//for(int i = 0; i < x.size();i++)
			//dp[0][i] = 1;
		
		for(int i = 1; i <= g.size();i++)
		{
			for(int j = 1; j <= x.size();j++)
			{
			
				if(g[i-1] == x[j-1])
					dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % NUM;
				else
					dp[i][j] = dp[i-1][j];
			
			}
		}
		
		/*for(int i = 0; i <= g.size();i++)
		{
			for(int j = 0; j <= x.size();j++)
				cout << dp[i][j] << " ";
			cout << endl;
		}*/
		string zeros;
		if(dp[g.size()][x.size()] == 0)
			zeros = "000";
		else
		{
			double y = 4 - log10(dp[g.size()][x.size()]);
			//cout << "y is " << y << endl;
			for(int i = 1; i < y;i++)
			{
				zeros.push_back('0');
			}
		}
		cout << "Case #" << (testCase+1) << ": " << zeros << dp[g.size()][x.size()] << endl;

		
	}

	
}