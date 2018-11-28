#include <cstdio>

#define MAX 1010


int tot;
int vetor[MAX];
int n,t;
int caso;
int total;
int menor;

int main(void){

	
	scanf("%d",&t);

	for(int i=0;i<t;i++){
		scanf("%d",&n);
		tot=0;
		total=0;
		menor=1<<30;
		for(int j=0;j<n;j++){
			scanf("%d",&vetor[j]);		
			tot^=vetor[j];		
			total+=vetor[j];
			if(vetor[j]<menor) menor=vetor[j];		
		}

		if(tot){
			printf("Case #%d: NO\n",++caso);
		}else{
			
			printf("Case #%d: %d\n",++caso,total-menor);
		}



	}


	return 0;


}
