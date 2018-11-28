#include<iostream>
#include<vector>
#include<string>

using namespace std;

int diff(vector<int> & lhs, vector<int> & rhs);

int main()
{
	int num;
	cin >> num;
	for(int i=1;i<=num;i++)
	{
		int S;
		cin >> S;
		cin.ignore(1);
		vector<string> engines(S);
		for(int j=0;j<S;j++)
		{
			getline(cin,engines[j]);
		}
		int Q;
		cin >> Q;
		cin.ignore(1);
		vector<string> queries(Q);
		for(int j=0;j<Q;j++)
		{
			getline(cin,queries[j]);
		}
		
		vector<vector<int> > dp(Q+1,vector<int>(S,0));

		for(int j=1;j<=Q;j++)
		{
			for(int k=0;k<S;k++)
			{
				dp[j][k] = dp[j-1][k];
				if(engines[k]==queries[j-1])
				{
					dp[j][k]++;
				}
			}
		}

#ifdef DEBUG
		for(int j=0;j<dp.size();j++)
		{
			for(int k=0;k<S;k++)
			{
				cout << dp[j][k];
			}
			cout << endl;
		}
		cout << endl;
#endif
		int Y = 0;
		vector<int> start(dp[0]);
		for(int j=1;j<dp.size();j++)
		{
			if(diff(start,dp[j])==-1)
			{
				Y++;
				int old = diff(start,dp[j-1]);
				start = dp[j];
				start[old]--;
			}
		}		
		cout << "Case #" << i << ": " << Y << endl;
	}

	return 0;
}

int diff(vector<int> & lhs, vector<int> & rhs)
{
	for(unsigned int i=0;i<lhs.size();i++)
	{
		if(lhs[i]==rhs[i])
		{
			return i;
		}
	}
	return -1;
}	

