#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std;

int x[5][5];

int main()
{
	int i,t,T,n;
	double r1,r2,r3,ret=0.0;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1;t<=T;t++) {
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
			scanf("%d %d %d",&x[i][0],&x[i][1],&x[i][2]);
			
		printf("Case #%d: ",t);	
			
		if(n==1) printf("%d\n",x[0][2]);
		if(n==2) {
			ret = max(x[0][2],x[1][2]);
			printf("%lf\n",ret);
		}
		if(n==3) {
			r1 = x[0][2];
			r2 = x[1][2];
			r3 = x[2][2];
			
			r1 = max(r1, (sqrt(pow(x[1][0]-x[2][0],2)+pow(x[1][1]-x[2][1],2))+double(x[1][2]+x[2][2]))/2.0);
			r2 = max(r2, (sqrt(pow(x[0][0]-x[2][0],2)+pow(x[0][1]-x[2][1],2))+double(x[0][2]+x[2][2]))/2.0);
			r3 = max(r3, (sqrt(pow(x[0][0]-x[1][0],2)+pow(x[0][1]-x[1][1],2))+double(x[0][2]+x[1][2]))/2.0);
			
			ret = min( min(r1,r2), r3);
			printf("%lf\n",ret);
		}
	}
}
