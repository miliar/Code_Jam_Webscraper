#include <stdio.h>


char grilla[5][5];
	

char comprobarH(){
	char ganador=0;
	
	for(int i=0;i<4 && !ganador;i++){
		
		if(grilla[i][0]!='.'){
			
			if(grilla[i][0]=='T' && grilla[i][1]!='.'){
				ganador=grilla[i][1];
				for(int j=2;j<4;j++){
					if(grilla[i][j]!=ganador){
						ganador=0;
					}
				}
			}
			else{
				ganador=grilla[i][0];
				for(int j=1;j<4;j++){
					if(grilla[i][j]!=ganador && grilla[i][j]!='T'){
						ganador=0;
					}
				}
			}
			
			
			
			
		}
	}
	
	
	
	
	

	return ganador;
}

char comprobarV(){
	char ganador=0;
	
	for(int i=0;i<4 && !ganador;i++){
		
		if(grilla[0][i]!='.'){
			
			if(grilla[0][i]=='T' && grilla[1][i]!='.'){
				ganador=grilla[1][i];
				for(int j=2;j<4;j++){
					if(grilla[j][i]!=ganador){
						ganador=0;
					}
				}
			}
			else{
				ganador=grilla[0][i];
				for(int j=1;j<4;j++){
					if(grilla[j][i]!=ganador && grilla[j][i]!='T'){
						ganador=0;
					}
				}
			}
			
			
			
			
		}
	}
	
	
	
	
	
	
	return ganador;
}

char comprobarDP(){
	char ganador=0;
	
	if(grilla[0][0]!='.'){
		
		if(grilla[0][0]=='T'){
			ganador=grilla[1][1];
			for(int i=2;i<4;i++){
				if(grilla[i][i]!=ganador){
					ganador=0;
				}
				
				
			}
		}
		else{
			ganador=grilla[0][0];
			for(int i=1;i<4;i++){
				if(grilla[i][i]!=ganador && grilla[i][i]!='T'){
					ganador=0;
				}
				
				
			}
		}
	}
	return ganador;
}

char comprobarDS(){
	char ganador=0;
	
	if(grilla[0][3-0]!='.'){
		
		if(grilla[0][3-0]=='T'){
			ganador=grilla[1][3-1];
			for(int i=2;i<4;i++){
				if(grilla[i][3-i]!=ganador){
					ganador=0;
				}
				
				
			}
		}
		else{
			ganador=grilla[0][3-0];
			for(int i=1;i<4;i++){
				if(grilla[i][3-i]!=ganador && grilla[i][3-i]!='T'){
					ganador=0;
				}
				
				
			}
		}
	}
	return ganador;
}


char comprobarVacante(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(grilla[i][j]=='.'){
				return 1;
			}
		}
	}
}








int main(){
	
	
	
	freopen("TTTT.txt","r",stdin);
	freopen("TTTT.out.txt","w",stdout);
	
	int dump;
	int ganador;
	int cant;
	scanf("%d",&cant);
	
	
	
	for(int n=0;n<cant;n++){
		
		scanf("%s\n%s\n%s\n%s\n",&grilla[0][0],&grilla[1][0],&grilla[2][0],&grilla[3][0]);
//		for(int Notelopuedocreer=0;Notelopuedocreer<4;Notelopuedocreer++){
//			
//			
//			for(int txtplease=0;txtplease<4;txtplease++){
//				
//				scanf("%c",&grilla[Notelopuedocreer][txtplease]);
//				
//				scanf("%c",&dump);
//				(dump=='O'||dump=='X'||dump=='T'||dump=='.')?printf("ERROR: %c\n",dump):dump=0;
//			}
//			
//			scanf("%c",&dump);
//			(dump=='O'||dump=='X'||dump=='T'||dump=='.')?printf("ERROR: %c\n",dump):dump=0;
//		}
		
		
		ganador=0;
		
		ganador=comprobarH();
		if(ganador){printf("Case #%d: %c won\n",n+1,ganador);continue;}
		ganador=comprobarV();
		if(ganador){printf("Case #%d: %c won\n",n+1,ganador);continue;}
		ganador=comprobarDP();
		if(ganador){printf("Case #%d: %c won\n",n+1,ganador);continue;}
		ganador=comprobarDS();
		if(ganador){printf("Case #%d: %c won\n",n+1,ganador);continue;}
		
		if(!ganador){
			if(comprobarVacante()){
				printf("Case #%d: Game has not completed\n",n+1);
				continue;
			}
			else{
				
				printf("Case #%d: Draw\n",n+1);
				continue;
			}
		}
		
		
		
	}
	
	
	
	
	
}
