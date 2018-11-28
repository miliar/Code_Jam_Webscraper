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

long a,b,d,n,i,k,i2,c,i1,k1,j,m,z;
long t,cas,k0,dmax;
long ta[30],ta2[30];
char we[100];
int compare( const void *p,const void *q)
	{
		return ((*(int *)p)-(*(int *)q));
			
	}

	

int main() { //convex hull
	freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();
	

	//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	//while(1){
	scanf("%ld",&t);
	for(cas=1;cas<=t;cas++){
	
		scanf("%s",&we);
		k=strlen(we);
		for(i=0;i<k;i++)
			ta[i]=we[i]-'0';

		a=-1;
		for(z=k-2;z>=0;z--){
		
			for(i=z+1;i<k;i++){
				if(ta[z]<ta[i]){
					if(a<0)
						a=i;
					else if(ta[i]<ta[a])
						a=i;
				
				}
				

			}
			if(a>=0)
				break;
		}

		printf("Case #%ld: ",cas);
		if(a<0){
			qsort(ta,k,sizeof(long),compare);
			
			if(ta[0]==0){
				i=0; 
				while(ta[i]==0)
					i++;
				ta[0]=ta[i];
				ta[i]=0;
			}
			printf("%ld0",ta[0]);
			for(i=1;i<k;i++)
				printf("%ld",ta[i]);
			printf("\n");
		}
		else {
			for(i=0;i<z;i++)
				printf("%ld",ta[i]);
			printf("%ld",ta[a]);
			j=0;
			for(i=z;i<k;i++){
				if(i!=a)
					ta2[j++]=ta[i];
			}
			qsort(ta2,j,sizeof(long),compare);
			for(i=0;i<j;i++)
				printf("%ld",ta2[i]);
			printf("\n");
		}


	} 

	return 0;

} 
