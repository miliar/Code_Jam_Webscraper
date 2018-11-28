#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;

int X[1024], Y[1024], R[1024];

int main()
{
freopen("r2\\D-small-attempt0.in", "r", stdin);
freopen("r2\\D-small-attempt0.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int id = 1;
	while (cas--)
	{
		int n;scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%d%d%d", X+i, Y+i, R+i);
		double ans = 0;
		if (n == 1)
		{
			ans = R[0];
		}
		else if (n == 2)
		{
			double ans1 = max(R[0], R[1]);
			int dx = X[0] - X[1], dy = Y[0] - Y[1];
			double ans2 = (sqrt(dx*dx+dy*dy)+R[0]+R[1])/2;
			ans = min(ans1, ans2);
		}
		else
		{
			int dx = X[0] - X[1], dy = Y[0] - Y[1];
			double ans1 = (sqrt(dx*dx+dy*dy)+R[0]+R[1])/2;
			ans1 = max((double)R[2], ans1);
			
			dx = X[0] - X[2], dy = Y[0] - Y[2];
			double ans2 = (sqrt(dx*dx+dy*dy)+R[0]+R[2])/2;
			ans2 = max((double)R[1], ans2);
			
			dx = X[1] - X[2], dy = Y[1] - Y[2];
			double ans3 = (sqrt(dx*dx+dy*dy)+R[1]+R[2])/2;
			ans3 = max((double)R[0], ans2);
			
			ans = min(ans1, ans2);
			ans = min(ans, ans3);
		}
		printf("Case #%d: %.6f\n", id++, ans);
	}
	return 0;
}
