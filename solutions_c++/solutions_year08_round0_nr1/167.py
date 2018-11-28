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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
map<string,int> M;
int v[1010];
int a[110][1010];
int res;
int do_dp(int n, int m)
{
	int i, j;
	for (i=0;i<n;i++)
		a[i][0]=0;
	a[v[0]][0]=1;
	for (j=1;j<m;j++)
	{
		for (i=0;i<n;i++)
			a[i][j]=a[i][j-1];
		a[v[j]][j]+=2;
		for (i=0;i<n;i++)
		{
			if (i!=v[j])
				a[v[j]][j]=min(a[v[j]][j], a[i][j-1]+1);
		}
	}
	res=1e9;
	for (i=0;i<n;i++)
		res=min(res,a[i][m-1]);
	return 0;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int i, j, n, k, l, m, t, T;
	scanf("%d", &T);
	char c[110];
	string s;
	for (t=1;t<=T;t++)
	{
		M.clear();
		scanf("%d\n", &n);
		for (i=0;i<n;i++)
		{
			gets(c);
			s=c;
			M[s]=i;
		}
		scanf("%d\n", &m);
		if (m==0)
		{
			res=0;
			goto l1;
		}
		for (i=0;i<m;i++)
		{
			gets(c);
			s=c;
			v[i]=M[s];
		}
		do_dp(n,m);
l1:;
		printf("Case #%d: %d\n", t,res);
	}
	return 0;
}