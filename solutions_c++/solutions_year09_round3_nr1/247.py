#include <iostream>
#include <string>
using namespace std;

int used[1000];

int getDig(char c)
{
	if(used[c] == 0) return 1;
	if(used[c] == 1) return 0;
	return used[c];
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++)
	{
		memset(used, -1, sizeof(used));
		string s;
		cin>>s;
		int cur = 0;
		for(int i=0;i<s.length();i++)
		{
			if(used[s[i]] == -1)
			{
				used[s[i]] = cur;
				cur++;
			}
		}
		long long res = 0;
		if(cur == 1)
		{
			cur++;
		}
		for(int i=0;i<s.length();i++)
		{
			res *= cur;
			res += getDig(s[i]);
		}
		printf("Case #%d: %I64d\n", t, res);
	}
	return 0;
}