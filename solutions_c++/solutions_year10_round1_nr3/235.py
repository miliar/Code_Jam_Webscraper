#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

// golden ratio
#define GR 1.6180339887498948482

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int a1, a2, b1, b2;
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		long long num = 0;
		for (int i = a1; i <= a2; i++)
		{
			int p = (int)(i / GR);
			p = min(p, b2);
			if (p >= b1)
				num += p - b1 + 1;
		}
		for (int i = b1; i <= b2; i++)
		{
			int p = (int)(i / GR);
			p = min(p, a2);
			if (p >= a1)
				num += p - a1 + 1;
		}
		printf("Case #%d: %lld\n", testCount + 1, num);
	}
	return 0;
}