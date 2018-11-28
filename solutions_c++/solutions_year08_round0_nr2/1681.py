#include<stdio.h>
#include<queue>
#include<stdlib.h>

using namespace std;


// Meter a al motículo heap.push( a );
// Obtener el mejor a= heap.top();
// Sacar el mejor heap.pop();
// Default mayor -> menor;

	
 
typedef struct{
	int S,L,E;
}trenes;

trenes vec[500];

int casos, k,i,j,NA,NB,T,h,m,total,resa,resb,mejor,l,s;

int compara( const void *a, const void *b){
	return (*(int *)a-*(int *)b);
}
void resuelve(){
		priority_queue <int>heapA;
		priority_queue <int>heapB;
		resa=0; resb=0;  
		scanf("%d\n %d %d\n",&T,&NA,&NB);
		for(i=0; i<NA; i++){
			scanf("%d:%d",&h,&m);
			s= h*60 +m;
			scanf("%d:%d",&h,&m);
			l= h*60 +m;
			vec[i].S= s; vec[i].L= l;
			vec[i].E=0;
			//printf("%d %d\n", vec[i].S,vec[i].L);
		}
		total= NA + NB;
		for( ; i<total; i++){
			scanf("%d:%d",&h,&m);
			s= h*60 +m;
			scanf("%d:%d",&h,&m);
			l= h*60 +m;
			vec[i].S= s; vec[i].L= l;
			vec[i].E=1;
		//	printf("%d %d\n", vec[i].S,vec[i].L);
		}
		qsort(vec, total, sizeof( vec[0]), compara);
		for( i=0; i< total ; i++)
			//printf("%d %d\n", vec[i].S,vec[i].L);

			if( vec[i].E ==0){
				if( heapA.size() == 0){
					resa++;
				}else{
					mejor= abs( heapA.top() ) ;
					if( mejor <= vec[i].S )
						heapA.pop();
					else
						resa++;
				}
				heapB.push( (vec[i].L + T) * (-1));	
			}else{
				if( heapB.size() == 0){
					resb++;
				}else{
					mejor= abs( heapB.top() ) ;
					if( mejor <= vec[i].S )
						heapB.pop();
					else
						resb++;
				}
				heapA.push( (vec[i].L + T) * (-1));
			}
		printf("Case #%d: %d %d\n",k,resa,resb);
		return ;
}
main(){
	scanf("%d",&casos);
	for(k=1; k<=casos; k++){
		resuelve();
	
			 
	}
	
	return 0;
}
