#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <deque>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

typedef long long int64;

int main()
{
	int test;
	freopen("input.txt", "rt", stdin);
	freopen("ouput.txt", "wt", stdout);
	scanf("%d", &test);
	for (int t = 0; t < test; t++)
	{
		int c;
		scanf("%d", &c);
		int v = 0;
		int m = 100000000;
		int64 res = 0;
		for (int i = 0; i < c; i++)
		{
			int q;
			scanf("%d", &q);
			res += q;
			v = (v^q);
			m = min(m, q);
		}
		if (v == 0)
			cout << "Case #" << t + 1 << ": " << res - m << endl;
		else
			cout << "Case #" << t + 1 << ": NO" << endl;
	}
  return 0;
}
