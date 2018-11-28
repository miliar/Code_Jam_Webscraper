#include <stdio.h>



int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int ca, cases=0, found;
    int n,m,a;
	scanf("%d",&ca);
	while (ca--)
	{
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d: ",++cases);

        found=0;
    	int u,v,w,x1,y1,x2,y2,x3,y3,k;
    	for (u=-m;u<=m;u++)
    	for (v=-m;v<=m;v++)
    	{
            if (u==0) continue;    		
    		w=-(u+v);
    		for (x1=0;!found && x1<=n ;x1++)
    		for (x2=0;!found && x2<=n;x2++)
    		{
    			x3=(a-v*x1-w*x2)/u;
    			if (x3>=0 && x3<=n && v*x1+w*x2+u*x3==a ) {
    				for (y1=0;y1<=m;y1++) {
    					y2=y1-u;
    					y3=y2-v;
    					if (y2>=0 && y2<=m && y3>=0 && y3<=m) {
    						printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
    						found=true;
    						break;
    					}
    				}
                }
    		}
    	}
    	if (!found)
    	   printf("IMPOSSIBLE\n");

	}
	return 0;
}
