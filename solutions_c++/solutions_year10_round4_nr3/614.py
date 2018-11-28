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

int n;

void Go()
{
	cin >> n;
	set<PII> G;
	for (int i = 0; i < n; i++)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				G.insert(PII(x, y));
	}
	int t;
	for (t = 0; G.size() > 0; t++)
	{
		set<PII> NG;
		for (set<PII>::iterator it = G.begin(); it != G.end(); ++it)
		{
			if (G.count(PII(it->first - 1, it->second + 1)))
			{
				NG.insert(PII(it->first, it->second + 1));
			}
			if (G.count(PII(it->first - 1, it->second)) > 0 || G.count(PII(it->first, it->second - 1)) > 0)
			{
				NG.insert(*it);
			}
		}
		G = NG;
	}
	cout << t;
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