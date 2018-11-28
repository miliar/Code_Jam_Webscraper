#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <vector>
#include <stdlib.h>

int in[101][101];
int out[101][101];

int H,W,drain;
int pode_acima,pode_abaixo,pode_direita,pode_esquerda;
void dfs(int i,int j){
	int menor_i,menor_j,menor_valor,a,b;
	if(i==0){
		pode_acima=0;
	}else{
		pode_acima=1;
	}
	
	if(i==H-1){
		pode_abaixo=0;
	}else{
		pode_abaixo=1;
	}
	
	if(j==0){
		pode_esquerda=0;
	}else{
		pode_esquerda=1;
	}
	
	if(j==W-1){
		pode_direita=0;
	}else{
		pode_direita=1;
	}
	menor_valor = 10002;
	if(pode_acima && (menor_valor > in[i-1][j])) menor_i = i-1, menor_j = j,menor_valor = in[i-1][j];
	if(pode_esquerda && (menor_valor > in[i][j-1])) menor_i = i, menor_j = j-1, menor_valor = in[i][j-1];
	if(pode_direita && (menor_valor > in[i][j+1])) menor_i = i, menor_j = j+1, menor_valor = in[i][j+1];
	if(pode_abaixo && (menor_valor > in[i+1][j])) menor_i = i+1, menor_j = j,menor_valor = in[i+1][j];
	
	out[i][j]=drain;
	if(in[i][j]>menor_valor){
			if(out[menor_i][menor_j]){
				/*A posicao ja esta marcada com alguma letra portanto eu
				 *tenho que marcar todas as celulas atuais com drain com
				 *aquela letra*/
				for(a=0;a<H;a++)
					for(b=0;b<W;b++)
						if(out[a][b]==drain) out[a][b] = out[menor_i][menor_j];
				drain--;		 
			}else{
				out[menor_i][menor_j]=drain; 
				dfs(menor_i,menor_j);
			}
	}
}

/*Desempate vai na ordem North, West, East, South*/
int main(){
	int T,i,j,Case=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d %d",&H,&W);
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				scanf("%d",&in[i][j]);
		drain=97;	
		memset(out,0,sizeof(out));
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				if(!out[i][j]){
					 dfs(i,j);
					 drain++;
				 }
	
		printf("Case #%d:\n",Case++);
		for(i=0;i<H;i++){
			for(j=0;j<W-1;j++)
				printf("%c ",(char)out[i][j]);
			printf("%c\n",(char)out[i][j]);
		}
	}
	return 0;
}

