#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <memory.h>

using namespace std;

int n;
int a[1010];

int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		reverse(a, a + n);
		int s = 0;
		for (int i = 0; i < n; ++i)
			s ^= a[i];
		printf("Case #%d: ", t + 1);
		if (s == 0)
		{
			int res = 0;
			for (int i  = 0; i < n - 1; ++i)
				res += a[i];
			printf("%d\n", res);
		}
		else
			printf("NO\n");

		
	}

	
	return 0;
}
