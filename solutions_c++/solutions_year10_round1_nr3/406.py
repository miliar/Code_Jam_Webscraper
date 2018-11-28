#include <stdio.h>
#include <string.h>
const int MAXN = 1000100;
int critical[MAXN];
int good(int a, int b)
{
	return a<=critical[b] || b<=critical[a];
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	critical[0]=-1;
	critical[1]=0;
	critical[2]=1;
	critical[3]=1;
	for (int i=4;i<=1000000;i++)
	{
		int l=1, r = i;
		while (l<r)
		{
			int c=(l+r+1)/2;
			int ind=0;
			for (int x=c; x<=i; x+=c)
				if (!good(c,i-x))
					ind=1;
			if (ind)	
				l=c;
			else
				r=c-1;
		}
		critical[i] = l;
	}

	int T;
	scanf("%d",&T);
	for (int t=0;t<T;t++)
	{
		int a1,b1,a2,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		
		__int64 ans=0;
		for (int a=a1;a<=a2;a++)
			for (int b=b1;b<=b2;b++)
				if (good(a,b))
					ans++;
		printf("Case #%d: %I64d\n",t+1,ans);
	}
	return 0;
}
