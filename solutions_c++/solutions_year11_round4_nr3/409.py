
/*Paresh Verma*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<list>
#include<map>

#define pub push_back
#define pob pop_back

using namespace std;

long long  * sieve(long long  x){
	long long  i,j,k,*a,*p;
	a=(long long *)calloc(x+1,sizeof(long long ));
	p=(long long *)calloc(x/2,sizeof(long long ));
	a[1]=2;
	for(i=2;i<=x;i++){
		if(a[i]==0){
			a[i]=1;
			p[++p[0]]=i;			
			for(j=i+i;j<=x;j+=i)
				a[j]=2;
		}
	}
	free(a);
	return p;
}
int main(){
	long long  i,j,k,l,x,T,n,a,b;
	scanf("%lld",&T);
	long long  * p = sieve(1000100);
	
	for(x=1; x<=T;x++){
		scanf("%lld",&n);
		a=0;		//least
		b=1;
		for(i=1;i<=p[0];i++){
			if(p[i]<=n){
				a++;
				long long  z=n;
				while(z/p[i]>=1){
					b++;
					z/=p[i];
				}
			}
			else
				break;
		}
		if(a<=0)
			a=1;
		if(b<=0)
			b=1;
		printf("Case #%lld: %lld\n",x,b-a);
	}
	
	return 0;
}
