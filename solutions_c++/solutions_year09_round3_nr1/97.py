#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

#define all(s) s.begin(), s.end()



int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;



	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

		string s;
//		getline(cin, s);
		cin >> s;

		map<char, int> mp;
		int cur_num = 1;
		bool zero_used = false;
		for (int i = 0; i < s.length() ; i++)
		{
			char c = s[i];
			if (mp.find(c) == mp.end())
			{
				if (i && !zero_used)
				{
					mp[c] = 0;
					zero_used = true;
				}
				else
					mp[c] = cur_num++;
			}
		}

		long long res = 0;
		int base = mp.size();
		base = max(base, 2);
		long long step = 1;
		for (int i = s.length() - 1; i >= 0 ; i--)
		{
			res += step * mp[s[i]];
			step *= base;
		}


		printf("Case #%d: %lld\n", test + 1, res);
	}

}