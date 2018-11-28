#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <vector>

#include <limits.h>
#include <math.h>
#include <stdio.h>

using namespace std;

#define foreach(k, b, N) for (int k = b; k <= N; k++)
#define foreach_r(k, b, N) for (int k = b; k >= N; k--)

int C[2000];
int N;

int c = 0;

long long
f(int index, long long gsum1, long long gsum2, long long bsum1, long long bsum2,
	int count1, int count2) 
{
	int ret1, ret2;

	c++;

	printf("index %d gsum1 %lld gsum2 %lld count1 %d bsum1 %lld bsum2 %lld count2 %d\n", index,
	gsum1, gsum2, count1, bsum1, bsum2, count2);

	if (index == N) {
		if (count1 == 0 || count2 == 0)
			return -1;

		if (bsum1 == bsum2)
			return (gsum1 > gsum2) ? gsum1 : gsum2;
		else
			return -1;
	}
	
	ret1 = f(index + 1, gsum1 + C[index], gsum2, bsum1 ^ C[index], bsum2, count1 + 1, count2);
	ret2 = f(index + 1, gsum1, gsum2 + C[index], bsum1, bsum2 ^ C[index], count1, count2 + 1);

	return (ret1 > ret2) ? ret1 : ret2;
}

int
main()
{
	int cases; 
	long long result = 0;

	cin >> cases;

	foreach(i, 1, cases) {
		string tmp;

		cin >> N;

		c = 0;

		getline(cin, tmp);
		getline(cin, tmp);
		istringstream ss(tmp);

		foreach(j, 0, N - 1)
			ss >> C[j];
		
// brute force
		//result = f(0, 0, 0, 0, 0, 0, 0);

// non-brute force
		long long min = LONG_MAX;
		long long bsum = 0;
		result = 0;
		foreach(j, 0, N - 1) {
			if (min > C[j])
				min = C[j];
			result += C[j];
			bsum = bsum ^ C[j];
		}

		result -= min;

		if (bsum != 0)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %lld\n", i, result);
	}

	return 0;
}
