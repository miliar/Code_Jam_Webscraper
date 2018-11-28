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
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int v[150],x[150],c,n,k,b,t,i,j,sum,ans,ct;
    double nt[150],tt[150],div;
	scanf("%d",&c);
	for (i = 1;i <= c;i++)
	{
		ct=sum=ans=0;;
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for (j = 1;j <= n;j++)
		{
			scanf("%d",&x[j]);
			x[j] = b-x[j];
		}
		for (j = 1;j <= n;j++)
			scanf("%d",&v[j]);
		for (j = 1;j <= n;j++)
		{
			nt[j] = double(x[j])/double(v[j]);
			tt[j] = nt[j];
		}
		sort(&nt[1],&nt[n+1]);
		div=nt[k];
		if (div > double(t)) {
			printf("Case #%d: IMPOSSIBLE\n",i);
			continue;
		}
		if (double(t) > div) 	div = double(t)	;	
		for (j = n;ct < k&&j >= 1;j--)
		{
			if (tt[j] > div) sum++;
			else
			{
				ct ++;
			    ans+=sum;
			}
		}
		printf("Case #%d: %d\n",i,ans);
				
	}
	
}
