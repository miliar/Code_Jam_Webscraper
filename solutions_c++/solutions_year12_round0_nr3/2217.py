#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <map>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	int ii;
	int p10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000};
	for(ii = 1; ii <= tt; ii++)
	{
		int a, b;
		cin >> a >> b;
		int tmp = a;
		int len = 1;
		while(tmp > 9)
		{
			tmp /= 10;
			len++;
		}
		int i;
		int s = 0;
		for(i = a; i <= b; i++)
		{
			int j;
			int tmp = i;
			vector<int> v;
			for(j = 0; j < len; j++)
			{
				int dig = tmp % 10;
				tmp = tmp / 10 + dig * p10[len - 1];
				if(dig == 0) continue;
				if(tmp > i && tmp <= b) v.push_back(tmp);
			}
			sort(v.begin(), v.end());
			s += unique(v.begin(), v.end()) - v.begin();
		}
		cout << "Case #" << ii << ": " << s << endl;
	}
	return 0;
}
