#define maxar 124800
#define maxver 5000
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include<stdlib.h>
#include<map>

using namespace std;


int won(char p);

char matriz[4][4];


int main () {
	int casos =0, x, o,complete=0;
	scanf("%d",&casos);
	getchar();
	for(int caso=1;caso<=casos;caso++){
	  complete=1;
	  for(int i=0;i<4;i++){
	    for(int j=0;j<4;j++){
	      matriz[i][j]=getchar();
	      if(matriz[i][j]=='.')complete=0;
	    }
	    getchar();
	  }
	  getchar();
	  x=won('X');
	  o=won('O');
	  if(x&&o) printf("Case #%d: Draw", caso);
	  else if(x) printf("Case #%d: X won", caso);	  
	  else if(o) printf("Case #%d: O won", caso);
	  else if(!complete) printf("Case #%d: Game has not completed", caso);
	  else printf("Case #%d: Draw", caso);
	  printf("\n");
	}
return 0;
}

int won(char p){
  int i,j;
  for(i=0;i<4;i++){
    for(j=0;j<4;j++){
      if(matriz[i][j]!=p&&matriz[i][j]!='T')break;
      else if(j==3) return 1;
    }
  }
  for(i=0;i<4;i++){
    for(j=0;j<4;j++){
      if(matriz[j][i]!=p&&matriz[j][i]!='T')break;
      else if(j==3) return 1;
    }
  }  
  for(i=0;i<4;i++){
    if(matriz[i][i]!=p&&matriz[i][i]!='T')break;
    else if(i==3) return 1;    
  }
  for(i=0;i<4;i++){
    if(matriz[i][3-i]!=p&&matriz[i][3-i]!='T')break;
    else if(i==3) return 1;    
  }
  return 0;
}

		
	
	
	
	

	
