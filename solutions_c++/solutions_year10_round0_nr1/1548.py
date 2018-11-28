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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		if ((k + 1) % (1 << n) == 0)
			printf("Case #%d: ON\n", testCount + 1);
		else
			printf("Case #%d: OFF\n", testCount + 1);
	}
	return 0;
}