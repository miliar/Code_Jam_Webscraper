#include<cstdio>
#include<algorithm>

using namespace std;

int cases,n;

int main()
{
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		scanf("%d",&n);
		int b=1,o=1,xb=0,xo=0,x=0;
		while(n--)
		{
			char r;
			int p;
			scanf(" %c %d",&r,&p);
			if (r=='B')
			{
				x+=max(0,abs(b-p)-xb)+1;
				xo+=max(0,abs(b-p)-xb)+1;
				xb=0;
				b=p;
			}
			else
			{
				x+=max(0,abs(o-p)-xo)+1;
				xb+=max(0,abs(o-p)-xo)+1;
				xo=0;
				o=p;
			}
		}
		printf("Case #%d: %d\n",t,x);
	}
	return 0;
}
