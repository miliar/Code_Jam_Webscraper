#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		int n;
		scanf("%d",&n);
		int xo=1,to=0,xb=1,tb=0;
		int now=0;
		for (int i=0;i<n;++i)
		{
			char s[5];
			int x;
			scanf("%s",s);
			scanf("%d",&x);
			if (s[0]=='O')
			{
				now=max(now,to+abs(xo-x))+1;
				xo=x;
				to=now;
			}else
			{
				now=max(now,tb+abs(xb-x))+1;
				xb=x;
				tb=now;
			}
		}
		printf("Case #%d: %d\n",test,now);
	}
	return 0;
}
