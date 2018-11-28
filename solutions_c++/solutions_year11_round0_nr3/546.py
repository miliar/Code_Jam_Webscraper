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

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t;
	int arr[1001];
	int n;
	cin >> t;
	
	for(int c = 1; c <= t; c++)
	{
		cin >> n;
		int res = 0;
		int sum = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> arr[i];
			sum += arr[i];
			res ^= arr[i];
		}

		if(!res)
		{
			sort(arr, arr + n);
			int sol = 0;
			for(int i = 1; i < n; i++)
			{
				int pile1 = 0, pile2 = 0;
				int sum1 = 0, sum2 = 0;
				for(int j = 0; j < i; j++)
				{
					pile1 ^= arr[j];
					sum1 += arr[j];
				}
				for(int j = i; j < n; j++)
				{
					pile2 ^= arr[j];
					sum2 += arr[j];
				}
				if(pile1 == pile2)
				{
					sol = max(sol, max(sum1, sum2));
				}
			}
			printf("Case #%d: %d\n", c, sol);
		}
		else
			printf("Case #%d: NO\n", c);
	}
	return 0;
}
