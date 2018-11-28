#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int M = 100003;
void Go()
{
	int n;
	cin >> n;
	int mm = (1 << (n - 2));
	int res = 0;
	for (int m = 0; m < mm; m++)
	{
		int st = n;
		bool ok = 1;
		while (st != 1)
		{
			int cn = 0;
			for (int i = 0; i < st - 2; i++)
			{
				if (m & (1 << i))
					cn++;
			}
			if (st == cn + 1)
			{
				ok = 0;
				break;
			}
			st = cn + 1;
			if (st == 1)
			{
				break;
			}
			if (!(m & (1 << (st - 2))))
			{
				ok = 0;
				break;
			}
		}
		if (ok)
			res = (res + 1) % M;
	}
	cout << res;
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "C-small-attempt0";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int yy = 1; yy <= t; yy++)
	{
		printf("Case #%d: ", yy);
		Go();
		printf("\n");
	}
	return 0;
}