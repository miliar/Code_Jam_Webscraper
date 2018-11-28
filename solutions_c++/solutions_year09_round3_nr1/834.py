#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 
#include <string>
#include <vector> 
#include <iostream> 
#include <sstream>
#include <queue>
using namespace std;

__int64 d,n,i,k,i2,c,i1,k1,j,m,z,k2,w,q,l;
__int64 t,cas,k0,dmax;
char we[100],we2[100];
double p1,p2; 
/*
struct li {
	char z;
	long n;
	long k;
} ta[50],ta2[50];
long tb[100];
*/
__int64 ta[50],a,b;


	
int main() { //convex hull
	freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();
	

	//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	//while(1){
	scanf("%I64d",&t);
	for(cas=1;cas<=t;cas++){
	
		scanf("%s",&we);

		k=strlen(we);
 
		for(i=0;i<50;i++)
			ta[i]=-1;

		d=1;
		i=0;
		if(we[i]>='0'&&we[i]<='9'){
			ta[we[i]-'0']=1;
			
		}
		else {
			ta[we[i]-'a'+10]=1;
			
		}
		i++;
		while(we[i]==we[i-1]&&i<k)
			i++;
		if(i<k){
			if(we[i]>='0'&&we[i]<='9'){
				ta[we[i]-'0']=0;
				
			}
			else {
				ta[we[i]-'a'+10]=0;
				 
			}
			i++;
			d=2;
			for(;i<k;i++){
				if(we[i]>='0'&&we[i]<='9'){
					if(ta[we[i]-'0']<0)
						ta[we[i]-'0']=d++;

				}
				else {
					if(ta[we[i]-'a'+10]<0)
						ta[we[i]-'a'+10]=d++;

				}
			}
		}
		if(d==1)
			d++;
		a=0;
		b=1;
		for(i=k-1;i>=0;i--){
			if(we[i]>='0'&&we[i]<='9'){
				
					a+=b*ta[we[i]-'0'];

			}
			else {
				
				a+=b*ta[we[i]-'a'+10];

			}
			b*=d;
		}

					
		printf("Case #%I64d: %I64d\n",cas,a);

		

	} 

	return 0;

} 
