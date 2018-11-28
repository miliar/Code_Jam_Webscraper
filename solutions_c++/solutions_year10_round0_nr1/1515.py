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

int main(){
	 string s;
	 unsigned long long n,k,v[32];
	 int i,Case=1,t;
	 scanf("%d",&t);
     v[0]=1;
	 for(i=1;i<=30;i++)v[i]=2*v[i-1];
	 for(i=1;i<=30;i++)v[i]-=1;

	 while(t--){

		 scanf("%lld %lld",&n,&k);

		 if(k>=n){
			 n=v[n];
			 k&=n;
			 if(n == k){
			 	printf("Case #%d: ON\n",Case++);
				continue;
			 }
		}
		printf("Case #%d: OFF\n",Case++);

   	}
	 return 0;
}

