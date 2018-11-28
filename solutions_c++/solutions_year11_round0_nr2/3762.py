#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

int comb[300][300];
int opp[300][300];

int main(void){
	int n;
	scanf("%d ",&n);
	int N, C, D;
	char tmp[3];
	char c, last;
	for(int i=0;i<n;i++){
		for(int j=0;j<30;j++)
			for(int k=0;k<30;k++){
				 comb[j][k] = comb[k][j] = opp[j][k] = opp[k][j] = -1;
			}
		scanf("%d",&C);
		scanf(" ");
		for(int j=0;j<C;j++){
			scanf("%c%c%c",&tmp[0],&tmp[1],&tmp[2]);
			comb[tmp[0]-'A'][tmp[1]-'A'] = 
							comb[tmp[1]-'A'][tmp[0]-'A']  = tmp[2]-'A';			
		}

		scanf("%d",&D);
		scanf(" ");
		for(int j=0;j<D;j++){
			scanf("%c%c",&tmp[0],&tmp[1]);
			opp[tmp[0]-'A'][tmp[1]-'A'] = opp[tmp[1]-'A'][tmp[0]-'A'] = 1;
		}
		// Processa 
		int wiped = 0;
		scanf("%d", &N);
		int in[30] ;
		int qtd_in = 0;
		scanf("  "); scanf("%c",&c);
		in[qtd_in++] = c-'A';
		for(int j=1;j<N;j++){
			wiped = 0;
			last = c;
			scanf("%c",&c);
			if(last!='n' && comb[c-'A'][last-'A']!=-1){ // Combinam
		 		in[qtd_in-1] = comb[c-'A'][last-'A'];			
				c = comb[c-'A'][last-'A'] + 'A';			
			}else in[qtd_in++] = c-'A';
			for(int k=0;k<qtd_in && !wiped;k++) 
				if( opp[c-'A'][in[k]] != -1){
					qtd_in = 0; wiped = 1; c = 'n';
				}			
		}		
		printf("Case #%d: [",i+1);
		for(int j=0;j<qtd_in-1;j++) printf("%c, ",(char)(in[j]+'A'));
		if(qtd_in!=0) printf("%c]\n",char(in[qtd_in-1]+'A'));
		else printf("]\n");
		
	}
	return 0;
}
