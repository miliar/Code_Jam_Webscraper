#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))
#define pi 3.141592653589
#define VI vector <int>

#define maxn 15
#define Limit 1000000

int s[maxn],n,D;
bool f[Limit+5];
int p[Limit],len;

inline int Check(int A,int B,int base)
{
	for (int i=1;i<n;++i)
	if (s[i]!=((long long)s[i-1]*A+B)%base) return -1;
	return ((long long)s[n-1]*A+B)%base;
}

int main()
{
	freopen("A_small_1.in","r",stdin);
	freopen("A_small_1.out","w",stdout);
	
	memset(f,true,sizeof(f));
	for (int i=2;i<=Limit;++i)
	if (f[i])
	{
		p[len++]=i;
		if (i<=Limit/i)
		for (int j=i*i;j<=Limit;j+=i)
			f[j]=false;
	}
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		printf("Case #%d: ",test);
		
		scanf("%d%d",&D,&n);
		int Max=0;
		for (int i=0;i<n;++i)
		{
			scanf("%d",&s[i]);
			Max=max(Max,s[i]);
		}
		
		if (n<2)
		{
			puts("I don't know.");
			continue;
		}
		
		int base=1;
		for (int i=0;i<D;++i)
			base*=10;
		int ans=-1;
		for (int i=0;i<len && p[i]<base;++i)
		if (p[i]>Max)
		{
			for (int A=0;A<p[i];++A)
			{
				int B=(s[1]-(long long)s[0]*A)%p[i];
				if (B<0) B+=p[i];
				
				int next=Check(A,B,p[i]);
				if (next!=-1)
				{
					if (ans==-1) ans=next;
					if (ans!=next)
					{
						puts("I don't know.");
						goto Break;
					}
				}
			}
		}
		
		if (ans==-1) puts("I don't know.");
		else printf("%d\n",ans);
		
		Break:;
	}
	
	return 0;
}
