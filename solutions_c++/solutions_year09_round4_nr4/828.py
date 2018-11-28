#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <algorithm>

using namespace std;
#define TAM 15
#define INF 0x3f3f3f3f

double x[TAM],y[TAM],r[TAM];
double calc(int i,int j,int k){
    double raio = (sqrt(((x[i]-x[j])*(x[i]-x[j])) + ((y[i]-y[j])*(y[i]-y[j]))) + r[i] + r[j])/2;
	return max(raio,r[k]);	
}
int main(){
	int i;
	int nt,t,n;
	double ans;
	scanf("%d",&nt);
	for(t=1;t<=nt;t++){
	   scanf("%d",&n);
	   for(i=0;i<n;i++){
		   scanf("%lf %lf %lf\n",&x[i],&y[i],&r[i]);
	   }
	   if(n == 1) ans = r[0];
	   else if(n == 2) ans = max(r[0],r[1]);
	   else{      
	      ans = INF;
	      ans = min(ans,calc(0,1,2));
	      ans = min(ans,calc(0,2,1));
	      ans = min(ans,calc(1,2,0));
	   }
			
	   printf("Case #%d: %lf\n",t,ans);
	}
	return 0;
}