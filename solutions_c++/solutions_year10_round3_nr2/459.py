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


int main()
{

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int nCase, i, j;

	scanf("%d", &nCase);
	for(int cc=1; cc<=nCase; cc++)
	{
		__int64 L, P, C;
		int ret = 0;
		int cnt = 0;

		scanf("%I64d%I64d%I64d", &L, &P, &C);
		while( L<P)
		{
			L*=C;
			cnt++;
		}
		
		ret = log(cnt*1.0)/log(2.0);
		if( pow(2.0,ret) < cnt ) ret++;

		printf("Case #%d: %d\n", cc, ret);
	}
	return 0;

}