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

int n,d,p;
int main()
{
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
	int t;
	scanf("%d",&t);
	forn(tcase,t)
	{
		scanf("%d%d%d",&n,&d,&p);
		if(p!=d && (p==100 || p==0))
			printf("Case #%d: Broken\n",tcase);
		else
		{
			bool judge=0;
			int k=Min(n,100);
			forn(i,k)
			{
				if((i*d)%100==0)
				{
					printf("Case #%d: Possible\n",tcase);
					judge=1;
					break;
				}
			}
			if(!judge)
				printf("Case #%d: Broken\n",tcase);
		}
	}
	return 0;
}