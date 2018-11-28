#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int t,n,l,h,i,c;
	bool flag;
	int a[110];
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		printf("Case #%d: ",cnt);
		scanf("%d%d%d",&n,&l,&h);
		for (i=0;i<n;i++)
			scanf("%d",&a[i]);
		flag=false;
		for (c=l;c<=h;c++)
		{
			flag=true;
			for (i=0;i<n;i++)
				if (!(a[i]%c==0 || c%a[i]==0)) flag=false;
			if (flag) break;
		}
		if (flag) printf("%d\n",c);
		else printf("NO\n");
	}
	return 0;
}