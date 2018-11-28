#include <iostream>
#include <string>
using namespace std;
const int maxl = 16;
const int maxd = 5001;
string word[maxd];
string pattern;
int l, d;
int solve()
{
	int i, j, k, len, n = 0;
	bool start = false, end = true;
	string token[maxl];
	len = pattern.length();
	for (i = 0; i < len; i++)
	{
		if (pattern[i] == '(')
		{
			start = true;
			end = false;
		}
		else if (pattern[i] == ')')
		{
			end = true;
			start = false;
			n++;
		}
		else
		{
			if (start)
			{
				token[n] += pattern[i];
			}
			else if (end)
			{
				token[n] = pattern[i];
				n++;
			}
		}
	}
	int res = 0;
	for (i = 0; i < d; i++)
	{
		bool match = true;
		for (j = 0; j < l; j++)
		{
			bool found = false;
			len = token[j].length();
			for (k = 0; k < len; k++)
			{
				if (token[j][k] == word[i][j])
				{
					found = true;
					break;
				}
			}
			if (!found)
			{
				match = false;
				break;
			}
		}
		if (match)
		{
			res++;
		}
	}
	return res;
}
int main()
{
	int i, n;
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("in.txt", "r", stdin);
	cin>>l>>d>>n;
	for(i = 0; i < d; i++)
	{
		cin>>word[i];
	}
	for (i = 0; i < n; i++)
	{
		cin>>pattern;
		int res = solve();
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
