#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

using namespace std;

#define TAM 256

int n;
char mapa[TAM][TAM];

int valido(int i,int j){
  if(i < 0 || i>= n) return 0;
  if(j < 0 || j>= n) return 0;
  return 1;
}

int main(){

  int nt,k;
  int t = 1;
  scanf("%d",&nt);
  while(nt--){

    scanf("%d %d",&n,&k);
    int blue,red;
    blue = red = 0;

    for(int i = 0;i<n;i++)
      for(int j = 0;j<n;j++)
	scanf(" %c",&mapa[i][j]);

    for(int j = n-1;j>=0;j--)
      for(int i = 0;i<n;i++){
	int m = j;
	while(valido(i,m+1) && mapa[i][m+1] == '.'){
	  mapa[i][m+1] = mapa[i][m];
	  mapa[i][m] = '.';
	  m++;
	}
      }
    //for(int i =0;i<n;i++){
    // for(int j=0;j<n;j++) printf("%c",mapa[i][j]);
    // printf("\n");
    //}

    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++){
	if(mapa[i][j] == 'R' || mapa[i][j] == 'B'){
	  int aux = j;
	  int p = 1;
	  while(valido(i,aux+1) && p<=k && mapa[i][aux+1] == mapa[i][j]){
	    p++;
	    aux++;
	  }

	  if(p >= k){
	    if(mapa[i][j] == 'R') red = 1;
	    else blue = 1;
	  }
	  
	  aux = i;
	  p = 1;
	  while(valido(aux+1,j) && p<=k && mapa[aux+1][j] == mapa[i][j]){
	    p++;
	    aux++;
	  }

	  if(p >= k){
	    if(mapa[i][j] == 'R') red = 1;
	    else blue = 1;
	  }

	  aux = 1;
	  p = 1;
	  while(valido(i+aux,j+aux) && p<=k && mapa[i+aux][j+aux] == mapa[i][j]){
	    p++;
	    aux++;
	  }

	  if(p >= k){
	    if(mapa[i][j] == 'R') red = 1;
	    else blue = 1;
	  }

	  aux = 1;
	  p = 1;
	  while(valido(i+aux,j-aux) && p<=k && mapa[i+aux][j-aux] == mapa[i][j]){
	    p++;
	    aux++;
	  }
	  if(p >= k){
	    if(mapa[i][j] == 'R') red = 1;
	    else blue = 1;
	  }	  
	}
      }

    printf("Case #%d: ",t++);
    if(blue == 1 && red == 1) printf("Both\n");
    else if (blue == 0 && red == 0) printf("Neither\n");
    else if(blue == 1) printf("Blue\n");
    else printf("Red\n");
  }
  return 0;

}
