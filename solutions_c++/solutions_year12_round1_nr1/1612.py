#include <iostream>
#include <cstdio>
using namespace std;
double e[100003],f[100003],g[100003];
int main(){
	int n,ii;
	scanf("%d",&n);
	for(ii=1;ii<=n;ii++){
		int a,b,i;
		double c,d,a1,a2,ans=99999999,a3;
		scanf("\n%d %d",&a,&b);
		f[0]=1;
		e[0]=0;
		for(i=a;i>=1;i--){
			scanf("%lf",&e[i]);
			f[0]*=e[i];
		}
		g[0]=f[0];
		for(i=1;i<=a;i++){
			f[i]=((f[i-1]/(1-e[i-1]))*(1-e[i]))/e[i];
			g[i]=g[i-1]+f[i];
		}
		
		a1=f[0]*(b-a+1)+(1-f[0])*(2*b-a+2);
		if(a1<ans){ans=a1;}
		a2=b+2;
		if(a2<ans){ans=a2;}
		for(i=1;i<=a;i++){
			a3=(b-a+2*i+1)*(f[0]+g[i]-g[0])+(b-a+2*i+1+b+1)*(1-f[0]-g[i]+g[0]);
			if(a3<ans){ans=a3;}
		}
		printf("Case #%d: %.6lf\n",ii,ans);
	}
	return 0;
}
			
		
	
