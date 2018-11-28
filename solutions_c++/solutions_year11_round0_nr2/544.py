#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
using namespace std;

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int t, c, d, n;
	char comb[26][26];
	bool opposed[26][26];
	string basic;
	cin >> t;
	for(int k = 1; k <= t; k++)
	{
		memset(opposed, false, sizeof(opposed));
		for(int i = 0; i < 26; i++) for(int j = 0; j < 26; j++) comb[i][j] = '*';
		cin >> c;
		for(int i = 0; i < c; i++)
		{
			cin >> basic;
			comb[basic[0] - 'A'][basic[1] - 'A'] = basic[2];
			comb[basic[1] - 'A'][basic[0] - 'A'] = basic[2];
		}

		cin >> d;
		for(int i = 0; i < d; i++)
		{
			cin >> basic;
			opposed[basic[0] - 'A'][basic[1] - 'A'] = true;
			opposed[basic[1] - 'A'][basic[0] - 'A'] = true;
		}
		cin >> n;
		cin >> basic;
		string out;
		int a, b;
		for(int i = 0; i < n; i++)
		{
			out += basic[i];
			if(out.size() < 2) continue;
			a = out[out.size() - 2] - 'A';
			b = out[out.size() - 1] - 'A';
			if(comb[a][b] != '*')
			{
				out.erase(out.size() - 2, 2);
				out += comb[a][b];
			}
			else
			{
				for(int j = 0; j < out.size(); j++)
				{
					if(opposed[b][out[j] - 'A'])
					{
						out.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [", k);
		if(out.size() >= 1)
		{
			for(int i = 0; i < out.size() - 1; i++)
				printf("%c, ", out[i]);
			printf("%c", out[out.size() - 1]);
		}
		printf("]\n");
	}
	return 0;
}
