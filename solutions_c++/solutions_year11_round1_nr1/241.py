#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
#define all(x) (x.begin(),x.end())
using namespace std;
__int64 n,pd,pg;
int main()
{
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	__int64 i,j,k;
	int cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		int ok=0;
		scanf("%I64d%I64d%I64d",&n,&pd,&pg);
		if (n>100)n=100;
		for (i=1;i<=n;i++)
		{
			if (i*pd%100==0)
			{
				__int64 win=i*pd/100;
				__int64 lose=(i*(100-pd))/100;
				for (j=i;j<=1000000;j++)
				{
					if (j*pg%100==0)
					{
						__int64 win1=j*pg/100;
						__int64 lose1=(j*(100-pg))/100;
						if (win<=win1&&lose<=lose1)
						{
							ok=1;
							//printf("%d\n",j);
							break;
						}
					}
				}
			}
			if (ok)break;
		}
		printf("Case #%d: %s\n",++cc,ok?"Possible":"Broken");
	}
	return 0;
}
