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

int n, p;

void Go()
{
	cin >> p;
	n = 1 << p;
	vector<int> C, M;
	C.resize(n);
	M.resize(n);
	for (int i = 0; i < n; i++)
	{
		cin >> M[i];
		M[i] = p - M[i];
	}
	for (int i = 1; i <= p; i++)
	{
		for (int j = (1 << (p - i)); j < (1 << (p - i + 1)); j++)
		{
			cin >> C[j];
		}
	}
	vector<char> B(n);
	int res = 0;
	for (int i = 0; i < n; i++)
	{
		int g = i + n;
		VI pp;
		for (;;)
		{
			g >>= 1;
			if (g == 0)
				break;
			pp.push_back(g);
		}
		reverse(pp.begin(), pp.end());
		for (int k = 0; k < M[i]; k++)
		{
			B[pp[k]] = 1;
		}
	}
	for (int i = 1; i < n; i++)
	{
		if (B[i])
			res += C[i];
	}
	cout << res;
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "B-small-attempt0";
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