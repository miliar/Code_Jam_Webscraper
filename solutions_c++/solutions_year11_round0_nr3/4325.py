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
#include <string>

using namespace std;

int main()
{
	freopen("..\\C-small-attempt1.in","r",stdin);
	freopen("..\\C-small-attempt1.out","w",stdout);
	int testcase = 0;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int size = 0, sum = 0, realsum = 0, printsum = 0;
		int a[15] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
		int i,j,k;
		printf("Case #%d: ",caseId);
		scanf("%d",&size);
		for (int s = 0; s < size; s++)
			scanf("%d",&a[s]);
		std::sort(a, a + size);
		for (i = 0; i < size; i++)
		{
			for (j = i + 1; j < size; j++)
			{
				sum ^= a[j];
			}
			realsum += a[i];
			if (sum == realsum)
			{
				for (k = i + 1; k < size; k++)
					printsum += a[k];
				printf("%d\n", printsum);
				continue;
			}
		}
		printf("NO\n");
	}
	return 0;
}

