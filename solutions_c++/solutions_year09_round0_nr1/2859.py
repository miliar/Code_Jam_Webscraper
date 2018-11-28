#include <cstdio>
#include <cstdlib>
#include <cstring>
#define MAX_LETRAS 16
#define MAX_LINEAS 5002
int main(){
	int l,d,n;
	char cad[MAX_LETRAS];	
	char car;
	
	scanf("%d %d %d\n",&l,&d,&n);	
	char lineas[MAX_LINEAS][MAX_LETRAS];
	for(int i=0; i<d;i++)
		scanf("%s\n",lineas[i]);			
		
	//how many words match the patern
	char automata[MAX_LETRAS][28];
	char patron[28];
	for(int i=1; i<=n; i++){		
		int index=0;
		int cont_ks=0;
		while((car=getc(stdin)) && car!='\n'){
			ungetc(car,stdin);
			int c1 = scanf("(%[^)])",patron);
			if(c1==0){//conocemos la cadena
				scanf("%c",&car);
				automata[index][0]=1;
				automata[index][1]=car;
			}
			else{
				automata[index][0]=strlen(patron);
				strcpy(&automata[index][1],patron);
			}
			index++;
		}
				
		///evalua patron sobre cada palabra
		for(int j=0; j<d; j++){//numero de palabras
			int cont=0;
			for(int k=0; k<l; k++){//por cada letra de la palabra
				bool empato=false;
				for(int l=1; l<=automata[k][0];l++){//cada camino posible
					if(lineas[j][k]==automata[k][l]){
						cont++;
						empato=true;
						break;
					}
				}
				if(empato==false) //no coincide la k-esima letra de la i-esima linea
					break;				
			}					
			if (cont==l)
				cont_ks++;
		}
		printf("Case #%d: %d\n",i,cont_ks);	
	}
}
