#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;
int dp[1001][101];
string name[101];
string queries[1001];
int main()
{
	ifstream cin("input.txt");
	ofstream cout("out.txt");
	int n;
	cin>>n;
	for(int CASE = 1; CASE <= n; CASE++)
	{
		int s, q;
		cin>>s;
		cin.ignore();
		for(int i = 1; i <= s; i++)
			getline(cin, name[i]), dp[0][i] = 0;
		cin>>q;
		cin.ignore();
		for(int i = 1; i <= q; i++)
			getline(cin, queries[i]);
		for(int i = 1; i <= q; i++)
		{
			for(int j = 1; j <= s; j++)
			{
				dp[i][j] = 1<<30;
				if(name[j] == queries[i]) continue;
				for(int k = 1; k <= s; k++)
				{
					if(k == j)
						dp[i][j] = min(dp[i][j], dp[i-1][k]);
					else
						dp[i][j] = min(dp[i][j], dp[i-1][k] + 1);
				}
				
			}
		}
		int ans = 1<<30;
		for(int i = 1; i <= s; i++)
			if(ans > dp[q][i]) 
				ans = dp[q][i];
		cout<<"Case #"<<CASE<<": "<<ans<<endl;
	}
}
