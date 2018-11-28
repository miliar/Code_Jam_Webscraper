#include <stdio.h>
#include <string.h>

int main()
{
	int n,ca=0,i,j,x,m,xx,yy;
	scanf("%d",&n);
	while (scanf("%d",&n)==1)
	{
		m=1<<20;
		xx=yy=0;
		for (i=0;i<n;++i) 
		{
			scanf("%d",&x);
			if (x<m) m=x;
			xx+=x;
			yy^=x;
		}
		if (yy!=0) printf("Case #%d: NO\n",++ca); else printf("Case #%d: %d\n",++ca,xx-m);
	}
	return 0;
}
