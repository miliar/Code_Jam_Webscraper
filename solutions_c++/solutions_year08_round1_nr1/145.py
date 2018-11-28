#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

#define PB push_back
#define FORE(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();++i)

int a[1000],b[1000];

int main()
{
	int Z;
	scanf("%d",&Z);
	for(int z=1;z<=Z;++z)
	{
		printf("Case #%d: ",z);
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%d",a+i);
		for(int i=0;i<n;++i)
			scanf("%d",b+i);
		sort(a,a+n);
		sort(b,b+n);
		int ap=0,ak=n-1,bp=0,bk=n-1;
		ll r=0;
		for(int i=0;i<n;++i)
		{
			if(b[bk]-a[ap]>a[ak]-b[bp])
			{
				r+=b[bk]*a[ap];
				--bk;
				++ap;
			}
			else
			{
				r+=a[ak]*b[bp];
				--ak;
				++bp;
			}
		}
		printf("%lld\n",r);
	}
}
