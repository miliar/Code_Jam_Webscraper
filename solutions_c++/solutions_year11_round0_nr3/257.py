#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;



int N, values[1001], res, T, or;
int main()
{
	freopen("C-large.out","w",stdout);
	freopen("C-large.in","r",stdin);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		scanf("%d", &N);
		res = 0;
		or = 0;
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &values[i]);
			res += values[i];
			or ^= values[i];
		}
		sort(values, values + N);
		if (or != 0)
		{
			printf("Case #%d: NO\n", cases);
		}
		else
		{
			printf("Case #%d: %d\n", cases, res - values[0]);
		}
	}
	return 0;
}