#include <stdio.h> 
#include <math.h>
#include <string.h>
#include <stdlib.h>

long d,k,a,n,q,i,j,cas,t,s;
long ta[110];
struct eng {
	char naz[110];
	long nr;
} se[110];
char we[110];
int compare1( const void *p,const void *q)
	{
		//if(((eng *)q)->naz==((eng *)p)->naz)
			return (strcmp(((eng *)p)->naz,((eng *)q)->naz));
		//else 
		//	return (strcmp(((li *)p)->kraj,((li *)q)->kraj));		
	}

int main() {

	//freopen( "d:\\wojtek\\uva\\uva\\debug\\t10.in", "rt", stdin);
		//int czas=clock();


					
	//while(1){
	scanf("%ld",&t);	
	
	for(cas=1;cas<=t;cas++){
		scanf("%ld",&s);
		gets(se[0].naz);
		for(i=0;i<s;i++){
			gets(se[i].naz);
			se[i].nr=i;
		}
		
		qsort(se,s,sizeof(eng),compare1);

		scanf("%ld",&q);
		gets(we);
		d=0;
		a=0;
		for(i=0;i<s;i++)
			ta[i]=0;
		for(i=0;i<q;i++){ 
			gets(we);
			j=0;
			while(we[0]>se[j].naz[0])
				j++;
			while(strcmp(we,se[j].naz)!=0)
				j++;
			k=se[j].nr;
			if(a<s-1&&ta[k]==0){
				
					ta[k]=1;
					a++;
				
			}
			else if(a==s-1&&ta[k]==0){
				d++;
				a=1;
				for(j=0;j<s;j++)
					ta[j]=0;
				ta[k]=1;
			}
			
		}
		printf("Case #%ld: %ld\n",cas,d);


	}
		//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	return 0;
}
