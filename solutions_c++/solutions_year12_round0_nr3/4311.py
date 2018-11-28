#include<stdio.h>

int determinaDig(int num){
	int cont=1;	
	while(num > 9){
		num = num / 10;
		cont ++;
	}
	return cont;
}

int recicla(int num, int dig){
	int div;
	if(dig == 2)
		div = 10;
	if(dig == 3)	
		div = 100;
	if(dig == 4)
		div = 1000;
	int unidade = num/ div;
	int resto = (num % div)*10;
	return resto + unidade;
}

int main(){
	int T,instancia=1;
	int dig,contador,teste;
	int A,B;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d %d",&A, &B);
		contador = 0;
		dig = determinaDig(A);
		//printf("Dig  %d   ",dig );
		for(int j=A;j<=B;j++){
			teste = j;
			for(int k=0;k<dig-1;k++){
				teste = recicla(teste,dig);
				if(teste > j && teste <= B) {contador ++; //printf("ger %d num %d \n",j,teste);
				}
			}			
		}
		printf("Case #%d: %d\n",instancia++,contador);	
	}
	


}
