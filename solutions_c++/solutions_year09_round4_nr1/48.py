#include <cstdio>
#include <cstring>
#include <cstdlib>
#define inf 100000000
#define maxn 105

int a[maxn],n;
char s[maxn+10];

inline void swap(int &a,int &b)
{
	int t=a;a=b;b=t;
}

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d",&n);
		for (int i=0;i<n;++i)
		{
			scanf("%s",s);
			a[i]=-1;
			for (int j=n-1;j>=0;--j)
			if (s[j]=='1')
			{
				a[i]=j;
				break;
			}
		}
		int Ans=0;
		
		for (int i=0;i<n;++i)
		{
			if (a[i]<=i) continue;
			for (int j=i+1;j<n;++j)
			if (a[j]<=i)
			{
				for (int k=j;k>i;--k)
				{
					swap(a[k],a[k-1]);
					++Ans;
				}
				break;
			}
		}
		
		printf("Case #%d: %d\n",test,Ans);
	}
	
	return 0;
}
