#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <map>  
#include <string>
#include <vector> 
#include <iostream>  
#include <sstream> 
#include <queue>
#include <algorithm>

using namespace std; 
 
long i,k,i2,i1,r,k1,j,m,l,n,i3,j10,j2,j3,a1,a2,a3; 
long cas,s,c,a,b,k2,d,z,t,ng;
long tg[10][30],td[10][30],tr[10][30],ts[10][30],ta[30];

long ddn(long n){
	long i,a;

	a=1;
	for(i=0;i<n;i++)
		a*=2;
	return a;
}
int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);
	 
	

	scanf("%ld",&t);
	//cin>>t; 
	for(cas=1;cas<=t;cas++){  
	//while(1){ 
		
		scanf("%ld%ld",&n,&k); 
	

		a=ddn(n);
		if(k%a==a-1)
			printf("Case #%ld: ON\n",cas);
		else
			printf("Case #%ld: OFF\n",cas);
	}
	
		 


//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
