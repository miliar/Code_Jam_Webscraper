#include<cstdio>
#include<cstring>
#include<set>
#include<algorithm>
using namespace std;
#define N 10010
int n,a[N];multiset<int> p[N];
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",a+i);
		for(int i=1;i<=10000;i++)
			p[i].clear();
		sort(a,a+n);
		int S=100000;
		for(int i=0;i<n;i++)
		{
			int w=a[i];
			if(p[w-1].empty())
				p[w].insert(1);
			else
				p[w].insert(*(p[w-1].begin())+1),
				p[w-1].erase(p[w-1].begin());
		}
		for(int i=1;i<=10000;i++)
			if(!p[i].empty())
				S=min(S,*(p[i].begin()));
		if(n==0)S=0;
		printf("Case #%d: %d\n",__,S);
	}
	return 0;
}

