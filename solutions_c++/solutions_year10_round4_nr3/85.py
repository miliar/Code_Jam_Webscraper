#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int INF = 1000000100, N = 250;
typedef long long int LL;

int t, ans, n;
int x1, y1, x2, y2;
bool T[N][N];
bool any()
{
	for(int i = 0; i < N; ++i)
		for(int j = 0; j < N; ++j)
			if(T[i][j])
				return true;
	return false;
}
void compute()
{
	for(int i = N - 1; i >= 1; --i)
		for(int j = N - 1; j >= 1; --j)
			if(T[i][j])
			{
				if(!T[i - 1][j] && !T[i][j - 1])
					T[i][j] = false;
			}
			else
			{
				if(T[i - 1][j] && T[i][j - 1])
					T[i][j] = true;
			}
}
int main()
{
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		ans = INF;
		memset(T, 0, sizeof(T));
		cin >> n;
		for(int i = 0; i < n; ++i)
		{
			cin >> x1 >> y1 >> x2 >> y2;
			for(int j = y1; j <= y2; ++j)
				for(int k = x1; k <= x2; ++k)
					T[j][k] = true;
		}
		for(ans = 0; any(); ++ans)
			compute();
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
/*
2
2
 1
2 3
 4
*/
