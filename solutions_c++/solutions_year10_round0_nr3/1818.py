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
 
__int64 i,k,i2,i1,r,k1,j,m,l,n,i3,j10,j2,j3,a1,a2,a3; 
__int64 cas,s,c,a,b,k2,d,z,t,ng,c1;
__int64 ta[1010],tb[1010],tc[1010];
int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\c10.in", "rt", stdin); 
	//	int czas=clock(); 
	//pi=2*acos(0.0);
	 
	

	scanf("%I64d",&t);
	//cin>>t; 
	for(cas=1;cas<=t;cas++){  
	//while(1){ 
		
		scanf("%I64d%I64d%I64d",&r,&k,&n); 
		for(i=0;i<n;i++){ 
			scanf("%I64d",&ta[i]);
			tb[i]=0;
			tc[i]=0;
		}
		i=0;
		b=0;
		c=0;
		while(b<r&&tb[i]==0){
			tb[i]=b;
			tc[i]=c;
			a=0;
			j=0;
			while(j<n&&a<=k){
				a+=ta[i++];
				i%=n;
				j++;
			}
			if(a>k){
				i+=n-1;
				i%=n;
				++b;
				c+=a-ta[i]; 
			}
			else {
				++b;
				c+=a;
			}
		}
		//tb[i]=b;
		if(b<r){
			a=r-b;		//r-b - tyle jeszcze zosta³o biegów
			a1=b-tb[i];	//tyle biegów zajmuje jeden cykl
			c1=c-tc[i];	//tyle euro zarabia w 1 cyklu
			c+=(a/a1)*c1;
			r=a%a1;
			b=0;
			//i++;
			while(b<r){
				tb[i]=b;
				tc[i]=c;
				a=0;
				j=0;
				while(j<n&&a<=k){
					a+=ta[i++];
					i%=n;
					j++;
				}
				if(a>k){
					i+=n-1;
					i%=n;
					++b;
					c+=a-ta[i];
				}
				else {
					++b;
					c+=a;
				}
			}
		}


		printf("Case #%I64d: %I64d\n",cas,c);


	

		
	}
	 
		 


//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
