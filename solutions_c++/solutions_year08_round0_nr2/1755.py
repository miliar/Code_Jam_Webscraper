#include <stdio.h>

int depA[24*60];
int depB[24*60];
int arrA[24*60];
int arrB[24*60];

int simulate(int numA, int numB){
	int simEnd = 24*60;
	
	for(int i=0;i<simEnd;i++){
		numA-=depA[i];
		numA+=arrA[i];
		numB-=depB[i];
		numB+=arrB[i];
		if((numA<0)||(numB<0)){
			return 0;
		}
	}	
	return 1;
}

int main(){
	int testCase;
	scanf("%d",&testCase);
	for(int g=0;g<testCase;g++){
		int turnAround;
		for(int j=0;j<24*60;j++){
			depA[j]=0;
			depB[j]=0;
			arrA[j]=0;
			arrB[j]=0;
		}
		scanf("%d",&turnAround);
		int na,nb;
		scanf("%d%d",&na,&nb);
		for(int j=0;j<na;j++){
			int hd,md,ha,ma;
			scanf("%d:%d %d:%d",&hd,&md,&ha,&ma);
			//printf("A %d -> B %d\n",60*hd+md,60*ha+ma);			
			depA[60*hd+md]++;
			arrB[60*ha+ma+turnAround]++;
		}
		for(int j=0;j<nb;j++){
			int hd,md,ha,ma;
			scanf("%d:%d %d:%d",&hd,&md,&ha,&ma);
			//printf("B %d -> A %d\n",60*hd+md,60*ha+ma);
			depB[60*hd+md]++;
			arrA[60*ha+ma+turnAround]++;
		}
		int finish=0;
		for(int i=0;i<=na;i++){
			if(!finish){
				for(int j=0;j<=nb;j++){
					if(simulate(i,j)){
						printf("Case #%d: %d %d\n",g+1,i,j);
						finish=1;
						break;
					}
				}
			}
		}
	}
}