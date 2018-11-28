#include <stdio.h>
#include <stdlib.h>

#define INVOKES 36
#define OPPOSITES 28
#define LETRAS 26
#define BASES 8

char combines[INVOKES][INVOKES];
char opposites[LETRAS][LETRAS];

int main(int argc, char *argv[]){
	FILE *fin = fopen(argv[1],"r");

	//Reading

	//char bases [8] = {'Q','W','E','R','A','S','D','F'};
	char basesChars [8] = {'A','D','E','F','Q','R','S','W'};
	int *bases = (int*)calloc(LETRAS,sizeof(int));
	int *basesAppeared = (int*)calloc(LETRAS,sizeof(int));

	for(int i=0;i<BASES;++i){
		bases[((int)basesChars[i])-65]=1;
	}


	int casos;
	fscanf(fin,"%d\n",&casos);
	for(int caso = 1; caso<=casos; ++caso){
		for(int i=0;i<INVOKES;++i){
			if(i<LETRAS){
				basesAppeared[i]=0;
			}
			for(int j=0;j<INVOKES;++j){
				combines[i][j] = 'a';
				if(i < OPPOSITES && j<OPPOSITES)
					opposites[i][j] = false;
			}
		}


		int nCom, nOpp, n;
		char aux1, aux2, aux3;
		//Invokes
		fscanf(fin,"%d ",&nCom);
		for(int i=0;i<nCom;++i){
			fscanf(fin,"%c%c%c ",&aux1,&aux2,&aux3);
			combines[((int)aux1)-65][((int)aux2)-65] = aux3;
			combines[((int)aux2)-65][((int)aux1)-65] = aux3;
		}
		//Opposites
		fscanf(fin,"%d ",&nOpp);
		for(int i=0;i<nOpp;++i){
			fscanf(fin,"%c%c ",&aux1,&aux2);
			opposites[((int)aux1)-65][((int)aux2)-65] = true;
			opposites[((int)aux2)-65][((int)aux1)-65] = true;
		}
		//Chain
		fscanf(fin,"%d ",&n);
		int posActual=0;
		char *salida = (char*)malloc(sizeof(char)*n);

		int last, valor;
		bool inicio = true;
			
		for(int i=0;i<n;++i){
			fscanf(fin,"%c",&aux1);
			int valor = ((int)aux1)-65;	
			if(!inicio){
				if(combines[last][valor]<'a'){
					--posActual;
					aux1 = combines[last][valor];
					if(bases[last]>0)
						--basesAppeared[last];
				}				 
			}

			salida[posActual++]=aux1;
			last = ((int)aux1)-65;

			inicio = false;
			if( bases[last] == 1){
				++basesAppeared[last];
				bool opposed = false;
				for(int k=0;k<BASES && !opposed;++k){
					int valorBase = ((int)basesChars[k])-65;
					if(basesAppeared[valorBase]>0 && opposites[last][valorBase]==1 ){
						opposed = true;
					}
				}
				if(opposed){
					posActual = 0;
					inicio = true;
					for(int ba=0;ba<LETRAS;++ba){
						basesAppeared[ba]=0; 
					}
				}

			}

		}
		
		fprintf(stdout,"Case #%d: [",caso);
		for(int i=0;i<posActual;++i){
			fprintf(stdout,"%c",salida[i]);
			if(i==posActual-1)
				fprintf(stdout,"]");
			else
				fprintf(stdout,", ");
		}
		if(posActual==0){
			fprintf(stdout,"]");
		}
		fprintf(stdout,"\n");
		free(salida);

	}
	
	
	free(bases);
	fclose(fin);


	return 0;
}
