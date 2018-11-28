#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vi vector<int>
#define vs vector<string>

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define INF (2<<29)

using namespace std; 
string s;

int memo[50];
const string welcome = "welcome to code jam";
int main()
{
	int n; cin >> n;
	getline(cin, s);
	
	for(int kase = 1; kase <= n; ++kase)
	{
		getline(cin, s);
		memset(memo, 0, sizeof(memo));
		
		for(int i = 0; i < s.size(); ++i)
		{
			for(int j = 0; j < welcome.size(); ++j)
			{
				if(welcome[j] == s[i])
				{
					if(j)
					{
						memo[j]	+= memo[j-1];
						memo[j] %= 10000;
					}
					else
					{
						memo[j]++;
						memo[j] %= 10000;
					}
				}
			}
		}
		memo[welcome.size() - 1] %= 10000;
		cout << "Case #" << kase << ": ";
		printf("%04d\n", memo[welcome.size() - 1]);
	}
	
	return 0;
}
