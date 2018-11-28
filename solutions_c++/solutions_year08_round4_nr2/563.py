#include <stdio.h>

int cs,ct,n,m,a;

void done()
{
	int u,v,w,x1,y1,x2,y2,x3,y3,k;
	for (u=-m;u<=m;u++)
	for (v=-m;v<=m;v++)
	{
		w=-(u+v);
		if (u==0) continue;
		for (x1=0;x1<=n;x1++)
		for (x2=0;x2<=n;x2++)
		{
			x3=(a-v*x1-w*x2)/u;
			if (v*x1+w*x2+u*x3==a && x3>=0 && x3<=n) {
				for (y1=0;y1<=m;y1++) {
					y2=y1-u;
					y3=y2-v;
					if (y2>=0 && y2<=m && y3>=0 && y3<=m) {
						printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
						return;
					}
				}
			}
		}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
//	freopen("2.in","r",stdin);
	scanf("%d",&cs);
	for (ct=1;ct<=cs;ct++) {
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",ct);
		done();
	}
	return 0;
}
