#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
using namespace std;

const int N=3;

int i,j,k,m,n,l;
double a[N+10];
double s[N+10];

double dfs(int dep, int n)
{	
	int i,j,k;
	if (dep==n+1)
	{
		double rst=1;
		bool flag=false;
		for (i=1; i<=n; i++)
			if (s[i]==0)
				rst*=a[i];
			else
			{
				flag=true;
				rst*=1-a[i];
			}
	//	cout<<rst<<' ';
		if (flag)
        {
         //   cout<<m-n+1+m+1<<endl;
			rst*=m-n+1+m+1;
        }
		else
		{
		//    cout<<m-n+1<<endl;
			rst*=m-n+1;
        }
		return rst;
	}
	s[dep]=0;
	double tmp = dfs(dep+1,n);
	
	s[dep]=1;
	tmp += dfs(dep+1,n);
	
	return tmp;
}

double get(int n, int m)
{
	return dfs(1, n);
}

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d%d", &n, &m);
		for (i=1; i<=n; i++)
			scanf("%lf", &a[i]);
		double ans=min(m+2, n+m+1);
		for (i=0; i<n; i++)
			ans=min(ans, get(n-i,m)+i);
		printf("Case #%d: %.6lf\n",t,ans);
	}
	return 0;
}
