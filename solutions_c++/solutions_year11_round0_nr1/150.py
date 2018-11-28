#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

int t,n,a,b,aa,bb,p,ans,use;
char c;

int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int k=1;k<=t;k++)
	{
		ans = 0;
		a = 1;
		b = 1;
		aa = 0;
		bb = 0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%c%c%d",&c,&c,&p);
			//cout << c << " " << p << endl;
			//printf("a=%d b=%d aa=%d bb=%d ans=%d\n",a,b,aa,bb,ans);
			if (c=='O')
			{
				use = abs(p-a) - aa;
				if (use<0) use = 0;
				use++;
				ans += use;
				bb += use;
				aa = 0;
				a = p;
			}
			else
			{
				use = abs(p-b) - bb;
				if (use<0) use = 0;
				use++;
				ans += use;
				aa += use;
				bb = 0;
				b = p;
			}
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
