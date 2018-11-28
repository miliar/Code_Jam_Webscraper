#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cassert>
#define rep(i,a,n) for(int i=a;i<n;i++)
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d ",n)
#define outln(n) printf("%d\n",n)
#define outl(n) printf("%lld ",n)
#define outlln(n) printf("%lld\n",n)
#define LL long long 
#define pb push_back
using namespace std;
int getdig(int x)
{
	int r=0;
	while(x)x/=10,r++;
	return r;
}
int seen[2000100];
int main()
{
	int t[10];
	t[0]=10;
	rep(i,1,9)t[i] = t[i-1]*10;
	int kases;
	in(kases);
	for(int kase = 1;kase <= kases; kase++)
	{
		memset(seen,-1,sizeof(seen));
		printf("Case #%d: ",kase);
		int res=0;
		int a,b;
		in(a);in(b);
		rep(i,a,b+1)
		{
			int j=0;
			int dig = getdig(i);;
			int pos = dig-2;
//			printf("i is %d\n",i);
			while(pos>=0)
			{
				int rem = i/t[j];
				int mov = i%t[j];
				int num = rem + mov*t[pos];
				pos--;
				if(mov && num >i && num <=b)
				{
					if(seen[num]!=i)res++;
					seen[num]=i;
				}
				j++;
			}

			
		}

		printf("%d\n",res);




	}
	
	return 0;
}
