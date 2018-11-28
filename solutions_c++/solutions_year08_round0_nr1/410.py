#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;

string read_line()
{
	string res;
	char c;
	while (true)
	{
		c = getchar();
		if (c == EOF || c == '\n')
			break;
		res += c;
	}
	return res;
}

void add_hash(string x, map<string,int> &hash)
{
	int num = hash.size();
	if (hash.find(x) == hash.end())
		hash[x] = num;
}

int main()
{
	int t, n, q;

	cin >> t;
	for (int tcase=1;tcase<=t;tcase++)
	{
		cin >> n;
		assert(read_line() == "");

		map<string,int> hash;
		for (int i=0;i<n;i++)
			add_hash(read_line(), hash);

		cin >> q;
		assert(read_line() == "");
		bool used[100];
		fill(used,used+100,false);
		int total_used = 0, ans = 0;
		for (int i=0;i<q;i++)
		{
			string x = read_line();
			assert(hash.find(x) != hash.end());
			if (used[hash[x]] == false)
			{
				used[hash[x]] = true;
				total_used++;
			}
			if (total_used == hash.size())
			{
				fill(used,used+100,false);
				used[hash[x]] = true;
				total_used = 1;
				ans++;
			}
		}
		cout << "Case #" << tcase << ": " << ans << endl;
	}
	return 0;
}		
