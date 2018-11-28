#pragma warning (disable: 4786)
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <sstream>
#include <algorithm>
using namespace std;
int a[10],k,sn,mi,l;
char s[1005],st[1005];
int test()
{
	int i,j=1;
	for (i = 0 ; i < sn ; i++)
	{
		st[i] = s[i/k*k+a[i%k]-1];
	}
	for (i = 1 ; i < sn ; i++)
	{
		if (st[i]!=st[i-1])
			j++;
	}
	return j;
}
void dfs(int d)
{
	int i;
	if (d==k)
	{
		i = test();
		if (mi > i) mi = i;
		return ;
	}
	for (i = d ; i < k ; i++)
	{
		swap(a[i],a[d]);
		dfs(d+1);
		swap(a[i],a[d]);
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int ca,T;
	scanf("%d",&T);
	for (ca = 1 ; ca <= 10 ; ca++) a[ca-1]=ca;
	for (ca = 1 ; ca <= T ; ca++)
	{
		mi = 1<<30;
		scanf("%d%s",&k,s);
		sn = strlen(s);
		l = sn/k;
		dfs(0);
		printf("Case #%d: %d\n",ca,mi);
	}
	return 0;
}