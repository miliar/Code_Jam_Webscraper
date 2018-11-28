#include<cstdio>

int isSorted(int vector[100],int n){
	for(int i=0;i<n-1;i++){
		if(vector[i]>vector[i+1])
			return 0;
	}
	return 1;
}

int main(){
	char aux;
	int i,j,k,l=1;
	int vector[100],gota;
	int n,cases,count;
	scanf("%d\n",&cases);
	while(cases--){
		scanf("%d\n",&n);
		for(i=0;i<n;i++){
			k=-1;
			for(j=0;j<n;j++){
				scanf("%c\n",&aux);
				if(aux=='1')
					k = j;
			}
			vector[i]=k;
//			printf("%d %d\n",i,k);
		}
		count=0;
		for(i=0;i<n;i++){
			if(vector[i]>i){
//				printf("need to swap line %d\n",i);
				for(j=i+1;j<n;j++){
					if(vector[j]<=i){
						break;
					}
				}
//				printf("best line %d\n",j);
				for(;j>i;j--){
					gota = vector[j];
					vector[j] = vector[j-1];
					vector[j-1] = aux;
					count++;
				}
			}
		}
		printf("Case #%d: %d\n",l++,count);
	}
}
