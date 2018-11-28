#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int n;
	scanf("%d\n", &n);

	for (int j = 0; j < n; j++)
	{
		char s[100];
		for (int i = 0; i < 100; i++)
			s[i] = 0;

		gets(s);

		map<int, int> mem;
		int x = 0;
		vector <long long> ans;
		for (int i = 0; s[i] != 0; i++)
		{
			if (mem.find(s[i]) == mem.end())
			{
				if (i == 0)
				{
					mem[s[i]] = 1;
					x ++;
				}else if (mem.size() == 1)
				{
					mem[s[i]] = 0;
					x ++;
				}else
				{
					mem[s[i]] = x;
					x ++;
				}
			}

			ans.push_back(mem[s[i]]);
		}

		long long base = mem.size();
		if (base == 1)
			base++;

		unsigned long long res = 0;
		for (int i = 0; i < ans.size(); i++)
			res = res * base + ans[i];

		cout << "Case #" << j + 1 << ": ";
		cout << res << endl;
	}

	return 0;
}