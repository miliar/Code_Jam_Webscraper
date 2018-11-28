#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Chick
{
	long long x;
	long long v;
} a[1000], next[1000];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	scanf("%d\n",&T);
	for (int test=1;test<=T;test++)
	{
		int n,k;
		long long b,t;
		scanf("%d%d%lld%lld",&n,&k,&b,&t);
		for (int i=0;i<n;i++)
			scanf("%lld",&a[i].x);
		for (int i=0;i<n;i++)
			scanf("%lld",&a[i].v);

		for (int i=0;i<n;i++)
		{
			next[i].x=a[i].x+a[i].v*t;
			next[i].v=a[i].v;
		}

		int cnt=0;
		int res=0;
		int slow=0;
		for (int i=n-1;i>=0;i--)
		{
			if (next[i].x>=b)
			{
				res+=slow;

				++cnt;
				if (cnt>=k)
				{
					break;
				}
			} else
			{
				if (i==0)
				{
					//cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
					break;
				}
				++slow;
			}
		}
		if (cnt>=k)
			cout<<"Case #"<<test<<": "<<res<<endl; else
			cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}