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
typedef vector<long> VL;
typedef pair<int, int> PII;


void Go()
{
	int N, K, B, T;
	cin >> N >> K >> B >> T;
	VL X(N), V(N);
	for (int i = 0; i < N; i++)
		cin >> X[i];
	for (int i = 0; i < N; i++)
		cin >> V[i];
	VI G(N);
	int res = 0;
	int all = 0;
	for (int i = N - 1; i >= 0; i--)
	{
		if (all >= K)
			break;
		if (B - X[i] <= T * V[i])
		{
			for (int j = i + 1; j < N; j++)
			{
				if (!G[j])
					res++;
			}
			all++;
			G[i] = 1;
		}
	}
	if (all >= K)
		cout << res;
	else
		cout << "IMPOSSIBLE";
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "B-large";
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