#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
#include <map>

using namespace std;

int main(){
  int teste, t=1, i, j, k, i1, i2, i3, j1, j2, j3;
  long long n,n0, A, B, C, D, M, x, y, prod, sum, fator;
  long long mapa[4][4];
  scanf("%d", &teste);
  while(teste--){
    scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x, &y, &M);
    //printf("n%lld A%lld B%lld C%lld D%lld x%lld y%lld M%lld\n", n, A, B, C, D, x, y, M);
    
    for(i=0; i<3; i++){
      for(j=0; j<3; j++){
	mapa[i][j]=0;
      }
    }
    n0=1;
    //printf("x[%lld] %lld y[%lld] %lld\n", x%3, x, y%3, y);
    mapa[x%3][y%3]++;
    while(n0++<n){
      x=(A*x+B)%M;
      y=(C*y+D)%M;
      //printf("x[%lld] %lld y[%lld] %lld\n", x%3, x, y%3, y);
      mapa[x%3][y%3]++;
    }
    /*
    printf("matriz\n");
    for(i=0; i<3; i++){
      for(j=0; j<3; j++){
	printf("mapa[%d][%d]=%lld\n", i, j, mapa[i][j]);
      }
    }
    */
    sum=0;
    for(i1=0; i1<3; i1++){
      for(j1=0; j1<3; j1++){
	for(i2=0; i2<3; i2++){
	  for(j2=0; j2<3; j2++){
	    for(i3=0; i3<3; i3++){
	      for(j3=0; j3<3; j3++){
		
		if((i1+i2+i3)%3==0
		   &&(j1+j2+j3)%3==0){
		  if(mapa[i1][j1]>0){
		    //printf("i1 %d j1 %d %lld\n", i1, j1, mapa[i1][j1]);
		    prod=mapa[i1][j1];
		    mapa[i1][j1]--;
		  }
		  else { 
		    break;
		  }
		  if(mapa[i2][j2]>0){
		    //printf("i2 %d j2 %d %lld\n", i2, j2, mapa[i2][j2]);
		    prod*=mapa[i2][j2];
		    mapa[i2][j2]--;
		  }
		  else {
		    mapa[i1][j1]++;
		    break;
		  }
		  if(mapa[i3][j3]>0){
		    //printf("i3 %d j3 %d %lld\n", i3, j3, mapa[i3][j3]);
		    prod*=mapa[i3][j3];
		    mapa[i3][j3]--;
		  }
		  else {
		    mapa[i1][j1]++;
		    mapa[i2][j2]++;
		    break;
		  }
		  //printf("i1 %d j1 %d %lld\n", i1, j1, mapa[i1][j1]);
		  //printf("i2 %d j2 %d %lld\n", i2, j2, mapa[i2][j2]);
		  //printf("i3 %d j3 %d %lld\n", i3, j3, mapa[i3][j3]);
		  //fator conta quantos conjuntos sao iguais e divide as repeticoes
		  /*if((i1==i2&&j1==j2)&&(i1==i3&&j1==j3)){
		    fator=6;
		  }
		  else if((i1==i2&&j1==j2)||(i2==i3&&j2==j3)||(i3==i1&&j3==j1)){
		    fator=2;
		  }
		  else fator=1;
		  sum+=prod/fator;
		  printf("sum %lld prod %lld fator %lld\n", sum, prod, fator);
		  */
		  //printf("sum %lld prod %lld\n", sum, prod);
		  sum+=prod;
		  mapa[i1][j1]++;
		  mapa[i2][j2]++;
		  mapa[i3][j3]++;		  
		}
     
	      }
	    }
	  }
	}
      }
    }
    printf("Case #%d: %lld\n", t++, sum/6);//todos os casos estao sendo contados 6 vezes
  }
  return 0;
}
