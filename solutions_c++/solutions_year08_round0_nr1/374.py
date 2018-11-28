#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

int flag[100];

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		int n, q, c, num = 0;
		string str;
		map<string, int> name;
		memset(flag, 0, 100 * 4);
		cin >> n;
		getline(cin, str);
		for(int i = 0; i < n; ++i)
		{
			getline(cin, str);
			name[str] = i;
		}
		cin >> q;
		getline(cin, str);
		c = n;
		while(q--)
		{
			getline(cin, str);
			int ind = name[str];
			if(flag[ind] <= num)
			{
				flag[ind] = num + 1;
				--c;
			}
			if(c <= 0)
			{
				++num;
				c = n - 1;
				flag[ind] = num + 1;
			}
		}
		printf("Case #%d: %d\n", t, num);
	}
}
