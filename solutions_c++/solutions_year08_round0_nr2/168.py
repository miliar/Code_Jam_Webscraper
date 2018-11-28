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
vector<pair<int,int> > v1, v2;
int a1[110], a2[110];
int N;
int proceed(int n, int m, int k, int p, int tim)
{
	int t;
	while(1)
	{	
		if (p==0)
		{
			t=v1[k].second+tim;
			for (int i=0;i<m;i++)
			{
				if (v2[i].first>=t && a2[i]==0)
				{
					N--;
					a2[i]=1;
					p=1;
					k=i;
					goto l1;
				}
			}
			break;
		}
		if (p==1)
		{
			t=v2[k].second+tim;
			for (int i=0;i<n;i++)
			{
				if (v1[i].first>=t && a1[i]==0)
				{
					N--;
					a1[i]=1;
					p=0;
					k=i;
					goto l1;
				}
			}
			break;
		}
l1:;
	}
	return 0;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int i, j, n, k, l, m, t, T, h1, h2, m1, m2, tim;
	scanf("%d", &T);
	for (t=1;t<=T;t++)
	{
		v1.clear();
		v2.clear();
		scanf("%d %d %d", &k, &n, &m);
		for (i=0;i<n;i++)
		{
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			h1-=20;
			h2-=20;
			v1.push_back(pair<int,int>(60*h1+m1, 60*h2+m2));
		}
		for (i=0;i<m;i++)
		{
			scanf("%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
			h1-=20;
			h2-=20;
			v2.push_back(pair<int,int>(60*h1+m1, 60*h2+m2));
		}
		int res1=0, res2=0;
		for (i=0;i<n;i++)
			a1[i]=0;
		for (i=0;i<m;i++)
			a2[i]=0;
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		N=n+m;
		int i1=0, i2=0;
		while(N)
		{
			while(i1<n && a1[i1])
				i1++;
			while(i2<m && a2[i2])
				i2++;
			if (i2==m || (i1<n && v1[i1].first<v2[i2].first))
			{
				res1++;
				a1[i1]=1;
				N--;
				proceed(n,m,i1,0,k);
			}
			else
			{
				res2++;
				a2[i2]=1;
				N--;
				proceed(n,m,i2,1,k);
			}
		}
		printf("Case #%d: %d %d\n", t,res1,res2);
	}
	return 0;
}