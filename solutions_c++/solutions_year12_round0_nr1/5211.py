#include<stdio.h>

char converte(char letra){
	if(letra == 'a') return 'y';
	if(letra == 'b') return 'h';
	if(letra == 'c') return 'e';
	if(letra == 'd') return 's';
	if(letra == 'e') return 'o';	
	if(letra == 'f') return 'c';
	if(letra == 'g') return 'v';
	if(letra == 'h') return 'x';
	if(letra == 'i') return 'd';		
	if(letra == 'j') return 'u';
	if(letra == 'k') return 'i';
	if(letra == 'l') return 'g';
	if(letra == 'm') return 'l';
	if(letra == 'n') return 'b';
	if(letra == 'o') return 'k';
	if(letra == 'p') return 'r';
	if(letra == 'q') return 'z';
	if(letra == 'r') return 't';
	if(letra == 's') return 'n';
	if(letra == 't') return 'w';
	if(letra == 'u') return 'j';
	if(letra == 'v') return 'p';
	if(letra == 'w') return 'f';
	if(letra == 'x') return 'm';
	if(letra == 'y') return 'a';
	if(letra == 'z') return 'q';
	return letra;
					
}


int main(){
	int T;
	int instancia = 1;
	char letra;
	while(scanf("%d",&T)!= EOF){
		scanf("%c",&letra);
		for(int i=0;i<T;i++){
			printf("Case #%d: ",instancia++);
			scanf("%c",&letra);			
			while(letra != '\n'){
				printf("%c",converte(letra));	
				scanf("%c",&letra);			
			}
			printf("\n");			
		}	
	}
}


