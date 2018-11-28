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



int N, num, T, res;
int main()
{
	freopen("D-large.out","w",stdout);
	freopen("D-large.in","r",stdin);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++)
	{
		scanf("%d", &N);
		res = 0;
		for (int i = 1; i <= N; i++)
		{
			scanf("%d", &num);
			if (num != i)
				res++;
		}
		printf("Case #%d: %.6f\n", cases, (float)res);
	}
	return 0;
}