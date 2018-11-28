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
#include <ctime>
#include <string.h>

using namespace std;

#define forn(i,n) for(int i=1;i<=n;i++)
#define Min(a,b) ((a)>(b)?(b):(a))
const double pi=acos(-1.0);
const double eps=1e-11;

int t,n,l,h;
int a[1000005];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	forn(tcase,t)
	{
		scanf("%d%d%d",&n,&l,&h);
		forn(i,n)
		{
			scanf("%d",&a[i]);
		}
		bool judge=0;
		int ans=-1;
		for(int k=l;k<=h;k++)
		{
			forn(i,n)
			{
				if(a[i]%k!=0 && k%a[i]!=0)
				{
					judge=1;
					break;
				}
			}
			if(!judge)
			{
				ans=k;
				break;
			}
			judge=0;
		}
		printf("Case #%d: ",tcase);
		if(ans==-1)
			printf("NO\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}