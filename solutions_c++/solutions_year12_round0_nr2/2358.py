#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <cstring>
#include <string.h>
using namespace std;
int t[100];
int dp[101][101];
int N, S, P; 
bool surprise(int t1, int t2, int t3)
{
	return abs(t1-t2) == 2 || abs(t1-t3) == 2 || abs(t2-t3) == 2;
}
/*
10 9 10
6 6 8 (*)
2 3 3
6 6 6
6 6 6
6 7 8 (*)
*/
int maxGog(int i, int s)
{
	if(dp[i][s] != -1)
		return dp[i][s];
	if (s > S)
		return -100;
	if (i == N)
	{
		if (s == S)
			return 0;
		return -100;
	}
	int subMax = 0;
	for (int t1 = 0; t1 <= 10; ++t1)
		for (int t2 = t1; t2 <= t1+2; ++t2)
			for (int t3 = t1; t3 <= t1+2; ++t3)
			{
				if (t1+t2+t3 == t[i] && t2 <= 10 && t3 <= 10 )
				{	
					int adv = max(t1, max(t2, t3)) >= P;
					if (surprise(t1, t2, t3))
						subMax = max(subMax, maxGog(i+1, s+1)+adv);
					else
						subMax = max(subMax, maxGog(i+1, s)+adv);
				}
			}
		return dp[i][s] = subMax;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cin >> N >> S >> P;
		memset(dp, -1, sizeof(dp));
		for (int j = 0; j < N; ++j)
			cin >> t[j];
		cout << "Case #" << i << ": " << maxGog(0, 0) << endl;
	}
}	