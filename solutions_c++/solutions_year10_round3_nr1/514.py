#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>	

using namespace std;

int n;
int s[1005][2];

int main()
{

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int nCase, i, j;

	scanf("%d", &nCase);
	for(int cc=1; cc<=nCase; cc++)
	{
		scanf("%d",&n);
		for(i=0; i<n; i++)
			scanf("%d %d", &s[i][0], &s[i][1]);
		int ret = 0;
		for(i=1; i<n; i++)
		{
			for(j=0; j<n; j++)
			{
				if( (s[i][0] < s[j][0] && s[i][1] > s[j][1]) ||
					(s[i][0] > s[j][0] && s[i][1] < s[j][1]) )
					ret ++;
			}
		}

		printf("Case #%d: %d\n", cc, ret);
	}
	return 0;

}