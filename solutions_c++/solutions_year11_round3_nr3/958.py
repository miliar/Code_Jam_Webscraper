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
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define print(n) printf("%d ",n);
#define printl(n) printf("%lld ",n);
#define println(n) printf("%d\n",n);
#define printlln(n) printf("%lld\n",n);
long long f[128];
int main()
{
	int X;
	scanf("%d",&X);
	int kase=1;
	while(X--)
	{
		long long n,l,h;
		scanf("%lld%lld%lld",&n,&l,&h);
		for(int i=0;i<n;i++)scanf("%lld",&f[i]);
		long long res=-1, j;
		//printlln(l);
		for(int i=l;i<=h;i++)
		{
			for(j=0;j<n;j++)
			{
				if(i%f[j]==0 || f[j]%i==0);
				else break;
			}
			if(j==n)
			{
				if(res==-1)res=i;
			}

		}
		if(res==-1)printf("Case #%d: NO\n",kase);
		else printf("Case #%d: %lld\n",kase,res);
		
		kase++;

	}
}

