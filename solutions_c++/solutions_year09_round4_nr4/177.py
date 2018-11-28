#include<stdio.h>
#include<math.h>

#define MAX 45

#define S(x)	((x)*(x))

int n;
int x[MAX],y[MAX],r[MAX];

double min(double x,double y){
	if(x<y)	return x;
	return y;
}
double max(double x,double y){
	if(x>y)	return x;
	return y;
}

int main(){

	int T,N;
	double best,d,now;
	int i,j,k;

	scanf("%d",&T);
	for(N=1;N<=T;N++){
		
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d%d",&x[i],&y[i],&r[i]);

		if(n==1)
			printf("Case #%d: %.8lf\n",N,1.*r[0]);
		else if(n==2)
			printf("Case #%d: %.8lf\n",N,max(r[0],r[1]));
		else{
			best = 1e50;

			for(i=0;i<n;i++){
				for(j=0;j<n;j++)if(j!=i){
					for(k=0;k<n;k++)if(k!=j && k!=i){
						d = sqrt(S(x[i]-x[j]) + S(y[i]-y[j]));

						now = max( (r[i]+d+r[j])/2., r[k]);
						best = min(best,now);
					}
				}
			}
			printf("Case #%d: %.8lf\n",N,best);


		}
		
		

	}

	return 0;
}