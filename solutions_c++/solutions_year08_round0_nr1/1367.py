#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("a.in");
  ofstream out("a.out");
#define cin in
#define cout out
#endif


int dp[1024][128];
int query[1024];
int main()
{
	int cs;
	cin >> cs;

	for(int t = 1; t <=cs; t ++) 
	{
		cout << "Case #"<< t <<": ";
		int s,q;
		map<string, int> m;

		cin >> s;

		string str;
		getline(cin,str);
		for(int i = 0; i < s; i++)
		{
			getline(cin, str);
			m[str] = i;
		}

		cin >> q;
		getline(cin,str);
		for(int i = 0; i < q; i++)
		{
			string str;
			getline(cin, str);
			query[i] = m[str];
		}

		if(q == 0 || q == 1)
		{
			cout<<0<<endl;
			continue;
		}

		memset(dp, 0, sizeof(dp));

		int max = 10000;
		for(int i = 0; i < q; i++)
		{
			dp[i][query[i]] = max;

		}

		for(int i = 0; i < s; i ++)
		{
			if(i == query[q - 1])
				dp[q-1][i] = max;
			else dp[q-1][i] = 0;
		}

		for(int i = q - 2; i >=0; i--)
		{
			for(int j = 0; j < s; j++)
			{
				if(j != query[i])
				{
					int best = max;

					if(query[i+1] != j)
					{
						best = dp[i+1][j];
					}else
					{

						for(int k = 0; k < s; k ++)
						{
							int temp = dp[i+1][k] + 1;
							if( temp < best)
								best = temp;

						}
					}
					dp[i][j] = best;
				}
			}
		}

		int ans = max;
		for(int i = 0; i < s; i++)
			if(dp[0][i] < ans)
				ans = dp[0][i];
		cout << ans << endl;

	}
	return 0;
}
