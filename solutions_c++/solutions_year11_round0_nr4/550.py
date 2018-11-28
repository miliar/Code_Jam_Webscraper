#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <complex>
using namespace std;

#define mem(a, b) memset(a, b, sizeof(a))

long long f(int num)
{
	if(num <= 1)
		return 0;
	return num;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, n;
	int nums[1001];
	bool visited[1001];
	cin >> t;
	for(int c = 1; c <= t; c++)
	{
		cin >> n;
		for(int i = 0; i < n; i++)
		{
			cin >> nums[i];
		}
		mem(visited, false);
		long long res = 0;
		for(int i = 0; i < n; i++)
		{
			if(!visited[i])
			{
				int cnt = 0;
				int idx = i;
				while(!visited[idx])
				{
					cnt++;
					visited[idx] = true;
					idx = nums[idx] - 1;
				}
				res += f(cnt);
			}
		}
		printf("Case #%d: %lld.000000\n", c, res);

	}
	return 0;
}
