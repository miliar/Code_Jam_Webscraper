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
#include <cctype>
using namespace std;

char str[50001];
int perm[17];
int K;
char next[50001];

int compress()
{
	int i, j;
	int len = strlen(str);
	for (i = 0;i < len;i += K)
		for (j = 0;j < K;j++)
			next[i + j] = str[i + perm[j]];
	int res = 0;
	for (i = 0;i < len;i++)
		res += (i == 0 || next[i - 1] != next[i]);
	return res;
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d", &K);
		scanf("%s", str);
		
		int i;
		for (i = 0;i < K;i++)
			perm[i] = i;

		int ans = strlen(str);
		do
		{
			int res = compress();
			if (ans > res)
				ans = res;
		} while(next_permutation(perm, perm + K));
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}