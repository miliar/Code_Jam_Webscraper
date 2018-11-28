#include <stdio.h>

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("b.txt","w",stdout);
	int c,t,a,n,m,x1,y1,x2,y2;
	scanf("%d",&c);
	for(t=1; t<=c; t++){
		scanf("%d%d%d",&n,&m,&a);
		for(x1=0; x1<=n; x1++){
			for(y1=0; y1<=m; y1++){
				for(x2=0; x2<=x1; x2++){
					for(y2=0; y2<=y1; y2++)
						if(x1*y1-x2*y2==a) goto done;
				}
			}
		}
done:
		printf("Case #%d: ",t);
		if(x1>n)
			printf("IMPOSSIBLE\n");
		else
			printf("0 0 %d %d %d %d\n",x1,y2,x2,y1);
	}
	return 0;
}
