#include <cstdio>
#include <cstring>
#define MAX_T 1000
using namespace std;

int T;

int main(){
  scanf("%d",&T);

  for(int i=0;i<T;++i){
    char Table[5][5];    
    int DET=0;
    bool filled=true;
    for(int j=0;j<4;++j)
      scanf("%s",Table[j]);
    // X=>1 O=>5 T=>21 NULL=>0
    
    for(int j=0;j<4;++j)
      for(int k=0;k<4;++k)
	switch(Table[j][k]){
	case 'X':
	  Table[j][k]=1;
	  break;
	case 'O':
	  Table[j][k]=5;
	  break;
	case 'T':
	  Table[j][k]=21;
	  break;
	case '.':
	  Table[j][k]=0;
	  filled=false;
	  break;
	}
    
    for(int j=0;j<4;++j){

      if(DET==4||DET==20||DET==24||DET==36)break;
      DET=0;
      for(int k=0;k<4;++k){
	DET+=Table[j][k];
      }

    }
    for(int j=0;j<4;++j){

      if(DET==4||DET==20||DET==24||DET==36)break;
      DET=0;
      for(int k=0;k<4;++k){
	DET+=Table[k][j];
      }

    }

    for(int j=0;j<1;++j){

      if(DET==4||DET==20||DET==24||DET==36)break;
      DET=0;
      for(int k=0;k<4;++k){
	DET+=Table[k][k];
      }
      if(DET==4||DET==20||DET==24||DET==36)break;
      DET=0;
      for(int k=0;k<4;++k){
	DET+=Table[k][3-k];
      }

    }

    printf("Case #%d: ",i+1);
    switch(DET){
    case 4:
    case 24:
      printf("X won");
      break;
    case 20:
    case 36:
      printf("O won");
      break;
    default:
      filled?printf("Draw"):printf("Game has not completed");
    }
    printf("\n");

    
  }
  
  return 0;
}
