#include <stdio.h> 
#include <math.h>
#include <string.h>
#include <stdlib.h>

long d,k,a,b,n,q,i,j,cas,t,s,na,nb,ka,kb;
long ta[110];
struct eng {
	long h1;
	long m1;
	long h2;
	long m2;
	long d;
	char st;
} se[110];
struct poc {
	long h1;
	long m1;
} tpa[200],tpb[200];
char we1[110],we2[100];
int compare1( const void *p,const void *q)
	{
		if((((eng *)q)->h1==((eng *)p)->h1)&&(((eng *)q)->m1==((eng *)p)->m1))

			return (((eng *)p)->d-((eng *)q)->d);
		else if(((eng *)q)->h1==((eng *)p)->h1)
			return (((eng *)p)->m1-((eng *)q)->m1);	
		else
			return (((eng *)p)->h1-((eng *)q)->h1);	
	}

		void przesa(long j){
			long i;
			for(i=j+1;i<ka;i++){
				tpa[i-1].h1=tpa[i].h1;
				tpa[i-1].m1=tpa[i].m1;
			}
			ka--;
		}

		void przesb(long j){
			long i;
			for(i=j+1;i<kb;i++){
				tpb[i-1].h1=tpb[i].h1;
				tpb[i-1].m1=tpb[i].m1;
			}
			kb--;
		}

int main() {

	//freopen( "d:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin);
		//int czas=clock();


					
	//while(1){
	scanf("%ld",&t);	
	
	for(cas=1;cas<=t;cas++){
		scanf("%ld",&s);
		scanf("%ld%ld",&na,&nb);
		for(i=0;i<na;i++){
			scanf("%s%s",&we1,&we2);
			se[i].h1=10*(we1[0]-'0')+(we1[1]-'0');
			se[i].m1=10*(we1[3]-'0')+(we1[4]-'0');
			se[i].h2=10*(we2[0]-'0')+(we2[1]-'0');
			se[i].m2=10*(we2[3]-'0')+(we2[4]-'0');
			se[i].d=60*(se[i].h2-se[i].h1)+se[i].m2-se[i].m1;
			se[i].st='A';
		}
		for(i=na;i<na+nb;i++){
			scanf("%s%s",&we1,&we2);
			se[i].h1=10*(we1[0]-'0')+(we1[1]-'0');
			se[i].m1=10*(we1[3]-'0')+(we1[4]-'0');
			se[i].h2=10*(we2[0]-'0')+(we2[1]-'0');
			se[i].m2=10*(we2[3]-'0')+(we2[4]-'0');
			se[i].d=60*(se[i].h2-se[i].h1)+se[i].m2-se[i].m1;

			se[i].st='B';
		}
		
		qsort(se,na+nb,sizeof(eng),compare1);

		ka=0;
		kb=0;

		a=0;
		b=0;
		for(i=0;i<na+nb;i++){
			if(se[i].st=='A'){
				q=0;
				for(j=0;j<ka;j++){
					if(se[i].h1>tpa[j].h1){
						przesa(j);
						tpb[kb].h1=se[i].h2;
						tpb[kb].m1=se[i].m2+s;
						if(tpb[kb].m1>=60){
							tpb[kb].m1-=60;
							tpb[kb].h1++;
						}
						kb++;
						q=1;
						break;
					}
					else if(se[i].h1==tpa[j].h1&&se[i].m1>=tpa[j].m1){
						przesa(j);
						tpb[kb].h1=se[i].h2;
						tpb[kb].m1=se[i].m2+s;
						if(tpb[kb].m1>=60){
							tpb[kb].m1-=60;
							tpb[kb].h1++;
						}
						kb++;
						q=1;
						break;
					}
				}
				if(q==0){
					a++;
					tpb[kb].h1=se[i].h2;
					tpb[kb].m1=se[i].m2+s;
					if(tpb[kb].m1>=60){
						tpb[kb].m1-=60;
						tpb[kb].h1++;
					}
					kb++;
				}
			}
			else {
				q=0;
				for(j=0;j<kb;j++){
					if(se[i].h1>tpb[j].h1){
						przesb(j);
						tpa[ka].h1=se[i].h2;
						tpa[ka].m1=se[i].m2+s;
						if(tpa[ka].m1>=60){
							tpa[ka].m1-=60;
							tpa[ka].h1++;
						}
						ka++;
						q=1;
						break;
					}
					else if(se[i].h1==tpb[j].h1&&se[i].m1>=tpb[j].m1){
						przesb(j);
						tpa[ka].h1=se[i].h2;
						tpa[ka].m1=se[i].m2+s;
						if(tpa[ka].m1>=60){
							tpa[ka].m1-=60;
							tpa[ka].h1++;
						}
						ka++;
						q=1;
						break;
					}
				}
				if(q==0){
					b++;
					tpa[ka].h1=se[i].h2;
					tpa[ka].m1=se[i].m2+s;
					if(tpa[ka].m1>=60){
						tpa[ka].m1-=60;
						tpa[ka].h1++;
					}
					ka++;
				}
			}
		}


		
		printf("Case #%ld: %ld %ld\n",cas,a,b);


	}
		//czas = clock() - czas;
	//printf("%lf\n",double(czas)/CLOCKS_PER_SEC);
	return 0;
}
