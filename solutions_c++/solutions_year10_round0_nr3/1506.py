#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <string>
#include <math.h>
using namespace std;
#define MAX 1001
unsigned long long r,k,n,v[MAX],s[MAX],d[MAX];
unsigned long long qtde,soma;
int main(){
	 int ini,fim;
	 int i,Case=1,t,j;
	 scanf("%d",&t);
	 while(t--){

		 scanf("%lld %lld %lld",&r,&k,&n);
		 for(i=0;i<n;i++)
			 scanf("%lld",&v[i]);

		 soma=0;
		 j=0;
		 j%=n;
		 for(i=0;i<n;i++){
			 while(soma+v[j]<= k){
				 soma+=v[j];
				 j++;
				 j%=n;
				 if(j==i) break;
			 }
			 s[i]=soma;
			 soma-=v[i];
			 d[i]=j;
		 }

		 i=0;
		 qtde=0;
		 for(j=0;j<r;j++){
			 qtde+=s[i];
			 i=d[i];
		 }
    	 printf("Case #%d: %lld\n",Case++,qtde);
   	}
	 return 0;
}
