#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

#define ll long long
#define rep(i,a,size) for(i=a; i<size; i++)

int check(ll size,ll counter){

	ll a[10000];
	ll b[10000];
	ll aw;
	ll bw;
	ll locator;
	ll times = size;
	ll i,j,k,l,m,n = 0;
	ll cross = 0;
	ll cases = 1;
	ll arraysize = 0;
	
	rep(i,0,10000){
		a[i]=0;
		b[i]=0;
	}	
	
	while(times){
		cross = 0;
		scanf("%lld %lld",&aw, &bw);
		//printf("%lld %lld \n",aw,bw);
		a[aw] = bw;
		b[bw] = aw;
		times--;
		cases++;
		if(arraysize <= aw) arraysize = aw+1;
		if(arraysize <= bw) arraysize = bw+1;
	}

	times = size;
	rep(i,1,arraysize){
		rep(j,i,arraysize){
			//printf("prueba i %lld j %lld %lld %lld %lld %lld \n",i, j ,a[i], a[j], b[a[i]], b[a[j]]);
			if((a[j] < a[i]) && (b[a[i]] < b[a[j]]))cross++;		
		}
	}

	printf("Case #%lld:",counter);
	printf(" %lld\n",cross);
}

int main(int argc, char *argv[]){
	ll cases, times = 0;
   ll counter = 1;
	scanf("%lld",&cases);
	while(cases){
		scanf("%lld",&times);
		check(times, counter);
		counter++;
		cases--;
	}

}


