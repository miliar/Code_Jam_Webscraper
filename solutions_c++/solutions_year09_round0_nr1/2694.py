#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
#define TAM 32
using namespace std;
vector<char> adj[TAM];
char s[6000][TAM], v[1024];

void insere(int tam){
     int i, abriu = 0, j = 0;
     for(i = 0; i < tam; i++){
           if(v[i] == '(') abriu = 1;
           else if(v[i] == ')'){ 
                abriu = 0;
                j++;
           }
           else{
                adj[j].push_back(v[i]);
                if(abriu == 0)j++; 
           }
     }
}

int main(){
    int i, tam, j, k, fim, l, foi, cont;
    int a, b, c;
	scanf("%d%d%d", &a, &b, &c);
	for(i = 0; i < b; i++){
		scanf(" %s", s[i]);
	}
	for(i = 0; i < c; i++){
		scanf(" %s", v);
		for(j = 0; j < TAM; j++){
          adj[j].clear();
        }
		insere(strlen(v));
		cont = 0;
        for(j = 0; j < b; j++){
              for(k = 0; k < a; k++){
                    fim = adj[k].size();
                    foi = 0;
                    for(l = 0; l < fim; l++){
                          if(s[j][k] == adj[k][l]){ 
                                     foi = 1;
                                     break;           
                          }
                    }
                    if(foi == 0) break;
              }
              if(foi == 1) cont++;
        }
        printf("Case #%d: %d\n", i+1, cont);      
    }
	return 0;
}

