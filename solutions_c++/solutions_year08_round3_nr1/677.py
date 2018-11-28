#include <stdio.h> 
#include <math.h>
#include <string.h>
#include <stdlib.h>

long d,a,b,n,q,i,j,cas,t,m,c;
long ta[1005];

long p,l,k;

int compare( const void *p,const void *q)
	{
		return ((*(int *)q)-(*(int *)p));
			
	}

	

int main() {

	//freopen( "d:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();


					
	//while(1){
	scanf("%ld",&t);	
	
	for(cas=1;cas<=t;cas++){
		scanf("%ld%ld%ld",&p,&k,&l);
		
		for(i=0;i<l;i++)
			scanf("%ld",&ta[i]);
			
		qsort(ta,l,sizeof(long),compare);

		c=0;
		a=1;
		b=0;
		q=0;
		for(i=0;i<l;i++){
			
			if(b==k){
				b=0;
				a++;
			}
			b++;
			if(ta[i]!=0&&a>p){
				q=1;
				break;
			}
			c+=ta[i]*a;
		}
		if(q==1)
			printf("Case #%ld: Impossible\n",cas);
		else
			printf("Case #%ld: %ld\n",cas,c);


	}
		//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	return 0;
}
