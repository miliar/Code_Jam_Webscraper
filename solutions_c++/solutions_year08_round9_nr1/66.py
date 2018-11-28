#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <complex>
#include <bitset>

#define PI 3.14159265358979
#define EPS 1E-10
#define INF 1000000000

using namespace std;

int like[10][3];

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < 3; ++j) cin >> like[i][j];
		}
		int res = 0;
		for(int i = 0; i < (1 << n); ++i)
		{
			int m[3] = {0}, num = 0;
			for(int j = 0; j < n; ++j) if(i & (1 << j))
			{
				for(int k = 0; k < 3; ++k) m[k] = max(m[k], like[j][k]);
				++num;
			}
			int sum = m[0] + m[1] + m[2];
			if(sum > 10000) continue;
			else res = max(res, num);
		}
		printf("Case #%d: ", t);
		printf("%d\n", res);
	}
	return 0;
}
