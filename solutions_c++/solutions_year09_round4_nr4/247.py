#include <stdio.h>
#include <math.h>

#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))

int main(){
	int t,u,n,x[40],y[40],r[40],i,j,k;
	double m;
	scanf("%d",&t);	
	for (u=0; u<t; u++){
		scanf("%d",&n);
		for (i=0; i<n; i++){
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		}
		m=1000000;
		if (n==1) m=r[0];
		else if (n==2) m=max(r[0],r[1]);
		else{
			for (i=0; i<3; i++){
				j=(i+1)%3;
				k=(i+2)%3;
				double d=(r[i]+r[j]+sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])))/2;
				if (max(d,r[k])<m) m=max(d,r[k]);
			}
		}
		printf("Case #%d: %.8lf\n",u+1,m);
	}
	return 0;
}
