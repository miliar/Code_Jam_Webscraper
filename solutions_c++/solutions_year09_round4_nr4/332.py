#include <stdio.h>
#include <math.h>
#define max(a,b) (((a)>(b))?(a):(b))
double x[3],y[3],r[3];
double Dist(int a,int b){
	return sqrt( (x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]) );
}
int main(){
	freopen("inpug.txt","r",stdin);
	freopen("outpug.txt","w",stdout);
	int C, N;
	scanf("%d",&C);
	while(C>0){
		scanf("%d",&N);
		C--;
		int i;
		for(i=0;i<N;i++){
			scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);
		}
		static int t=1;
		if(N == 1){
			printf("Case #%d: %lf\n", t++, r[0]);
			continue;
		}
		else if(N == 2){
			double sol;
			if(r[0] > r[1]) sol = r[0];
			else sol = r[1];
			printf("Case #%d: %lf\n", t++, sol);
			continue;
		}
		else if(N == 3){
			double sol;
			sol = max( Dist(0, 1) + r[0] + r[1], r[2]*2 );
			if(sol > max( Dist(2, 1) + r[2] + r[1], r[0]*2 ) ){
				sol = max( Dist(2, 1) + r[2] + r[1], r[0]*2 ) ;
			}
			if(sol > max( Dist(2, 0) + r[2] + r[0], r[1]*2 ) ){
				sol = max( Dist(2, 0) + r[2] + r[0], r[1]*2 ) ;
			}
			printf("Case #%d: %lf\n", t++, sol/2);

		}
	}
	return 0;
}