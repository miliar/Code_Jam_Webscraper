#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <list>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define All(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef vector<vector<int> > vvi;

const int inf = 0x0ffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 10000;

char buffer[10000];

vector<int> v;

int Solution(int nTest)
{
	gets(buffer);
	string s = "T"; 
	s += buffer;
	vector<pii> dp(s.size());
	string t = "Twelcome to code jam";
	
	
	for(int i = 0; i < s.size(); i++)
	{
		if(s[i] == t[t.length()-1])
		{
			dp[i].first = 1;
			dp[i].second = 0;
		}
	}
		

	for(int k = t.size() - 2; k >= 0; k--)
	{
		char c = t[k];
		int l = t.size() - k - 1;
		for(int i = 0; i < s.size(); i++)
		{
			if(s[i] == c)
			{
				dp[i].first = 0;
				dp[i].second = l;
				for(int j = i + 1; j < s.size(); j++)
				{
					if(dp[j].second == l - 1)
						dp[i].first += dp[j].first;
					dp[i].first %= 1000;
				}
			}
		}
	}
	printf("Case #%d: %04d\n", nTest + 1, dp[0].first);
	
	return 0;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int n = 0;

	scanf("%d", &n);
	gets(buffer);

	for(int i = 0; i < n; i++) Solution(i);


//	while(Solution(n));

	return 0;
}

