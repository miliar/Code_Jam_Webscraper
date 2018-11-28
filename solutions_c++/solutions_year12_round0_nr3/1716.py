#include <stdio.h>
#include <set>

using namespace std;

int main()
{
	int tc,t,a,b,i,j,q,p,n;
	scanf("%d\n",&t);
	for (tc=0;tc<t;++tc)
	{
		scanf("%d %d",&a,&b);
		set<pair<int,int> > x;
		n=1;
		p=0;
		while (a>=10*n) { n*=10; ++p; }
		for (i=a;i<b;++i)
		{
			q=i;
			for (j=0;j<p;++j)
			{
				q=(q/10)+(q%10)*n;
				if (q>i && q<=b) x.insert(make_pair(i,q));
			}
		}
		printf("Case #%d: %d\n",tc+1,(int)x.size());
	}
	return 0;
}
