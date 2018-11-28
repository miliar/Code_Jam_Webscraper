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

long long a[1000];
long long b[1000];
int n;
long long fun()
{
	scanf("%d",&n);
	
	for(int i=0;i<n;i++)
	{
		scanf("%lld",&a[i]);
		
	}
	for(int i=0;i<n;i++)
	{
		scanf("%lld",&b[i]);
	}
	sort(a,a+n);
	sort(b,b+n);
	reverse(b,b+n);

	long long res = 0;
	for(int i=0;i<n;i++)
	{
		res += a[i]*b[i];
	}
/*	int start=0;
	int end = n-1;
	while(start<n && a[start]<0 && b[start]>0)
	{
		res += a[start]*b[start];
		start++;
	}
	while(end>=0 && a[end]>0 && b[end]<0)
	{
		res += a[end]*b[end];
		end--;
	}
	for(int i=start;i<=end;i++)
	{
		res += a[i]*b[start+end-i];
	}*/
	return res;


}
int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T = 0;
	scanf("%d",&T);

	for(int i=0;i<T;i++)
	{
		long long res = fun();
		printf("Case #%d: %lld\n",i+1,res);

	}

	
	
	return 0;
}