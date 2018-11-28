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
int t[128];
int main()
{
	
	int kases;
	in(kases);
	for(int kase = 1;kase <= kases; kase++)
	{
		printf("Case #%d: ",kase);
		int n,s,p;
		in(n);in(s);in(p);
		rep(i,0,n)in(t[i]);
		sort(t,t+n);
		reverse(t,t+n);
		int res=0;
		rep(i,0,n)
		{
			int temp = t[i];
			int a[3];
			a[0] = temp/3;
			temp -= a[0];
			a[1] = temp/2;
			temp -= a[1];
			a[2] = temp;
			sort(a,a+3);
			if(a[2] >= p)
			{
				res++;
			}
			else if(t[i]%3!=1 && s>0 && t[i]!=0 && a[2]+1 >= p)
			{
				s--;
				res++;
			}
			assert(s>=0);

		}
		printf("%d\n",res);




	}
	
	return 0;
}
