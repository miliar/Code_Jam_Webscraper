#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
#define all(x) (x.begin(),x.end())
using namespace std;
int p[1200];
int gc[1200];
vector<pair<int,int> >a;
void fac(int n)
{
	int i,j,k;
	for (i=2;i*i<=n;i++)
	{
		if (n%i)continue;
		int c=0;
		while (n%i==0)
		{
			c++;
			n/=i;
		}
		a.pb(mp(i,c));
	}
	if (n!=1)a.pb(mp(n,1));
}
int main()
{
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,n,cc=0,cas;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		if (n==1)
		{
			printf("Case #%d: %d\n",++cc,0);
			continue;
		}
		for (i=0;i<n;i++)p[i]=i;
		int mi=10000000;
		int mx=1;
		map<int,int>g;
		for (i=2;i<=n;i++)
		{
			a.clear();
			fac(i);
			
			for (j=0;j<a.size();j++)
			{
				if (g[a[j].first]<a[j].second)
					break;
			}
			if (j==a.size())continue;
			mx++;
			for (j=0;j<a.size();j++)
			{
				g[a[j].first]=max(g[a[j].first],a[j].second);
			}
		}
		
		a.clear();
		g.clear();
		for (i=1;i<=n;i++)
		{
			a.clear();
			fac(i);
			
			for (j=0;j<a.size();j++)
			{
				g[a[j].first]=max(g[a[j].first],a[j].second);
			}
		}
		mi=g.size();
		//printf("%d\n",mx);
		printf("Case #%d: %d\n",++cc,mx-mi);
	}
}
					
