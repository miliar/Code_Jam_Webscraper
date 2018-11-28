#include<cstdio>
#include<list>
#include<algorithm>

using namespace std;

int n;
long long int  h,l,f[10000];
list<long long int>::iterator c;
list<long long int> store;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d %lld %lld",&n,&l,&h);
		for(int j=0;j<n;j++)
		{
			scanf("%lld",&f[j]);
		}
		printf("Case #%d: ",i+1);
		sort(f,f+n);
		store.clear();
		for(long long int j=l;j<=h;j++)
		{
			if(j%f[n-1]==0||f[n-1]%j==0)store.push_back(j);
		}
		for(int j=0;j<n-1;j++)
		{
			if(store.size()==0)break;
			c=store.begin();
			while(c!=store.end())
			{
				if(!((*c)%f[j]==0||f[j]%(*c)==0))
				{
					c=store.erase(c);
				}else{
					c++;
				}
			}
		}
		if(store.size()==0)printf("NO\n");
		else printf("%lld\n",*store.begin());
	}
	return 0;
}
				
