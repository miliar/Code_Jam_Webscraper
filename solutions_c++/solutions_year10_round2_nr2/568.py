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
long cas,s,c,t1,a,b,k2,d,z,t,ng;

long tv[100],tx[100];
int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);
	 
	
	scanf("%ld",&s);
	//cin>>t; 
	for(cas=1;cas<=s;cas++){  
		
		scanf("%ld%ld%ld%ld",&n,&k,&b,&t);
		
		for(i=0;i<n;i++){
			scanf("%ld",&tx[i]);
		}
		for(i=0;i<n;i++){
			scanf("%ld",&tv[i]);
		}
		d=0;
		a=0;
		z=0;
		for(i=n-1;i>=0;i--){
			t1=(b-tx[i])/tv[i];
			if((t1*tv[i])+tx[i]<b)
				t1++;
			if(t1<=t){
				a++;
				z+=d;
				if(a>=k)
					break;
			}
			else {
				d++;
			}
		}
		if(a>=k){
			printf("Case #%ld: %ld\n",cas,z);
		}
		else
			printf("Case #%ld: IMPOSSIBLE\n",cas);
	}




//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
