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
#include <ctime>

using namespace std;


vector<bool> v;
int l,t,n,c;
vector<int>a;

int dist(int idx)
{
	return a[idx%c];
}

int calc(int i,int now)
{
	int ret=0;
	if(now>=t)
	{
		ret = dist(i);
		if(!v[i]) return (ret*2);
		else return ret;
	}
	else
	{
		ret = dist(i)*2;
		if(now+ret>=t)
		{
			int x = now+ret-t;
			ret = t+x/2;
			return ret;
		}
		else
			return (ret*2);
	}
}

bool comp(const pair<int,int>& p,const pair<int,int> &q)
{
	if(p.first!=q.first) return p.first<q.first;
	else return p.second >= q.second;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tnum;int n,l,h;
	cin>>tnum;
	for(int q=1;q<=tnum;q++)
	{
		vector<int>a;
		cin>>n>>l>>h;
		a.clear();a.resize(n);
		for(int i=0;i<n;i++)
			cin>>a[i];
		int mini=-1;
		for(int i=l;i<=h;i++)
		{
			bool flag=true;
			for(int j=0;j<n;j++)
				if(i%a[j]==0 || a[j]%i==0);
				else {flag=false;break;}
				if(flag) { mini=i;break;}
		}
		if(mini==-1)
			printf("Case #%d: NO\n",q);
		else
			printf("Case #%d: %d\n",q,mini);
			

	}
}