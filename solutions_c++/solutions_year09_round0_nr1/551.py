#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int L, d, n;
vector<string> dict;

int main()
{
	scanf("%d %d %d", &L, &d, &n);
	for (int i = 0; i < d; i++)
	{
		string s;
		cin >> s;
		dict.push_back(s);
	}
	for (int i = 0; i < n; i++)
	{
		int ans = 0;
		string s;
		cin >> s;
		
		for (int j = 0; j < d; j++)
		{
			int cur = 0;
			for (int l = 0; l < (int)s.size(); l++)
			{
				if (s[l] == '(')
				{
					l++;
					bool found = false;
					while (s[l] != ')')
					{
						if (s[l] == dict[j][cur])
							found = true;
						l++;
					}
					if (!found)
						break;
				}
				else
				{
					if (s[l] != dict[j][cur])
						break;
				}
				cur++;
			}
			if (cur == L)
				ans++;
		}
		
		cout << "Case #" << (i + 1) << ": " << ans << endl;
	}
	return 0;
}
		
