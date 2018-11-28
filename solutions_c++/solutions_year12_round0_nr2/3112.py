#define _CRT_SECURE_NO_WARNINGS

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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}


int bestScoreWithoutSurprise(int total)
{
	return (total + 2) / 3;
}

int bestScoreWithSurprise(int total)
{
	return (total + 4) / 3;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);

		int y = 0;

		int n;
		int s;
		int p;
		int t[100];
		scanf("%d %d %d",&n,&s,&p);

		for (int i = 0; i < n; i++)
		{
			scanf("%d", &t[i]);
		}

		for (int i = 0; i < n; i++)
		{
			if (bestScoreWithoutSurprise(t[i]) >= p)
			{
				y++;
			}
			else
			{
				if ((s > 0) && (t[i] >= 2) && (bestScoreWithSurprise(t[i]) >= p))
				{
					y++;
					s--;
				}
			}
		}
		printf("%d\n", y);
		fflush(stdout);
	}
	return 0;
}