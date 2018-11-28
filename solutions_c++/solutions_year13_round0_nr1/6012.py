#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>    // std::sort
#include <vector>  
using namespace std;

char matriz[4][4];

char win(){
	int pontosl, pontosc;
	int tl=0, tc=0;
	//checa linhas e colunas
	for(int i=0; i<4; i++){
		pontosl=0;
		pontosc=0;
		tl=0;
		tc=0;

		for(int j=0; j<4; j++){
			if(matriz[i][j]=='X'){
				pontosl++;
			}
			else if(matriz[i][j]=='O'){
				pontosl--;
			}
			else if(matriz[i][j]=='T'){
				tl++;
			}

			if(matriz[j][i]=='X'){
				pontosc++;
			}
			else if(matriz[j][i]=='O'){
				pontosc--;
			}
			else if(matriz[j][i]=='T'){
				tc++;
			}

			

		}
		if(pontosl==4 || pontosc==4 ||pontosl==3 && tl==1 || pontosc==3 && tc==1){
			return 'X';
		}
		else if(pontosl==-4 || pontosc==-4 || pontosl==-3 && tl==1 || pontosc==-3 && tc==1){
			return 'O';
		}

		
	}

	int pontos1=0;
	int pontos2=0;
	int t1=0, t2=0;
	//checa diagonais
	for(int i=0; i<4; i++){
		if(matriz[i][i]=='X'){
			pontos1++;
		}
		else if(matriz[i][i]=='O'){
			pontos1--;
		}
		else if(matriz[i][i]=='T'){
			t1++;
		}

		if(matriz[i][3-i]=='X'){
			pontos2++;
		}
		else if(matriz[i][3-i]=='O'){
			pontos2--;
		}
		else if(matriz[i][3-i]=='T'){
			t2++;
		}

	}

	if(pontos1==4 || pontos2==4 || pontos1==3 && t1==1 || pontos2 ==3 && t2==1){
		return 'X';
	}
	if(pontos1==-4 || pontos2==-4 || pontos1==-3 && t1==1 || pontos2==-3 && t2==1){
		return 'O';
	}

	//game not completed
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if(matriz[i][j]=='.'){
				return 'N';
			}
		}
	}

	//draw
	return 'D';

}

int main(){
	FILE *in = fopen("A-small-attempt1.in", "r");
	FILE *out = fopen("out.txt", "w");

	int n;
	
	fscanf(in, "%d ", &n);

	for(int caso=0; caso<n; caso++){
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				fscanf(in, " %c ", &matriz[j][k]);
			}
		}
		

		char c=win();
		fprintf(out, "Case #%d: ", caso+1);

		if(c=='X'){
			fprintf(out, "X won");
		}
		else if(c=='O'){
			fprintf(out, "O won");
		}
		else if(c=='N'){
			fprintf(out, "Game has not completed");
		}
		else{
			fprintf(out, "Draw");
		}
		fprintf(out, "\n");

	}

	
	return 0;
}


