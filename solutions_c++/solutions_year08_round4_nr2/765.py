#include <stdio.h>
int main()
{
	freopen("B_ans.txt","w",stdout);
	int x,y,xx,yy;
	int s,t,st,n,m,temp;
	bool suc;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d %d %d",&n,&m,&s);
		suc=0;
		for (x=0;x<=n && !suc ; ++x) for (y=0;y<=m && !suc;++y)
		{
			for (xx=0;xx<=n && !suc;++xx) for (yy=0;yy<=m && !suc;++yy)
			{
				temp=yy*x-xx*y;
				//printf("%d %d %d %d %d\n",x,y,xx,yy,temp);
				if (temp<0) temp=-temp;
				if (temp == s) suc=1;
			}
		}
		if (suc) printf("Case #%d: 0 0 %d %d %d %d\n",t+1,x-1,y-1,xx-1,yy-1);
		else printf("Case #%d: IMPOSSIBLE\n",t+1);
	}
	return 0;
}
