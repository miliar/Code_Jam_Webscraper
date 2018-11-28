#include<stdio.h>

void rope(){
	int i,j;
	
	int n;
	int win_r[1000],win_l[1000];
	int point;

	scanf("%i",&n);
	for(i=0;i<n;i++) scanf("%i%i",&win_l[i],&win_r[i]);

	point=0;
	for(i=0;i<n-1;i++)
		for(j=i;j<n;j++){
			if((win_l[i]>win_l[j]&&win_r[i]<win_r[j]) || (win_l[i]<win_l[j]&&win_r[i]>win_r[j])) point++;
		}
	printf("%i",point);
}

int main(){
	int n,i;
	scanf("%i",&n);
	for(i=1;i<=n;i++){
		printf("Case #%i: ",i);
		rope();
		printf("\n");
	}
}
