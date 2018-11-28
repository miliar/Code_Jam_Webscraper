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
#include <ctime> 

using namespace std;

struct rec
{
	int a,b,c;
};

rec a[6000];
vector<pair<int,int> > p;
int d[20000];

bool pcmp(rec a,rec b)
{
	return a.a<b.a;
}

int lowbit(int x)
{
	return x^(x&(x-1));
}

void add(int x)
{
	int i;
	if (x==0)
	{
		d[0]++;return;
	}
	for (i=x;i<20000;i+=lowbit(i))
	{
		d[i]++;
	}
}

int get(int x)
{
	int i;
	int tmp;
	tmp=0;
	for (i=x;i>0;i-=lowbit(i))
	{
		tmp+=d[i];
	}
	tmp+=d[0];
	return tmp;

}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i,j,k,l,t,n,tmp,best;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d%d%d",&a[i].a,&a[i].b,&a[i].c);
		}
		best=0;
		p.clear();
		sort(a,a+n,pcmp);
		for (i=0;i<n;i++)
		{
			p.push_back(make_pair(a[i].b,a[i].c));
			sort(p.begin(),p.end());
			memset(d,0,sizeof(d));
			for (j=0;j<p.size();j++)
			{
				if (10000-a[i].a-p[j].first<0) break;
				add(p[j].second);
				tmp=get(10000-a[i].a-p[j].first);
				if (tmp>best) best=tmp;
			}
		}
		printf("Case #%d: %d\n",l+1,best);
	}
	return 0;
}
