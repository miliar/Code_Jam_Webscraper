#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	int tt;
	scanf("%d",&tt);
	for ( int t = 1; t<=tt ; t++)
	{
		int L,P,C;
		scanf("%d%d%d",&L,&P,&C);
		int cnt = 0 ;
		while ( 1)
		{
			int x = (P+C-1)/C;
			if ( x <= L )
				break;
			cnt ++;
			P = x;
		}
		if( cnt == 0 )
			printf("Case #%d: %d\n",t,0);
		else{
			cnt++;
			int res = ceil(log2(cnt));
			printf("Case #%d: %d\n",t,res);
		}
	}
	return 0;
}
