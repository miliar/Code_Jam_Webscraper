#include <iostream>
#include <cstdio>

using namespace std;

char grid[60][60];

int main(){

  int TT;
  scanf("%d", &TT);
  for(int T = 0; T < TT; T++){
    
    int y,x;
    char c;
    scanf("%d %d\n", &y, &x);
    for(int i =0; i<y; i++){
      for(int j=0; j<x; j++){
	scanf("%c", &grid[j][i]);
      }
      scanf("%c", &c);
    }
    
    bool eror = false;
    for(int i =0; i<y; i++){
      if(eror) break;
      for(int j=0; j<x; j++){
	if(eror) break;
	if(grid[j][i] == '#'){
	  if(j+1 < x && i+1 < y && grid[j+1][i] == '#' && grid[j][i+1] == '#' && grid[j+1][i+1] == '#'){
	    grid[j][i] = '/'; 
	    grid[j+1][i] = '\\'; 
	    grid[j][i+1] = '\\'; 
	    grid[j+1][i+1] = '/'; 
	  } else {
	    eror = true;
	    break;
	  }
	}
      }
    }
    printf("Case #%d:\n", T+1);
    if(eror){
      printf("Impossible\n");
    } else {
      for(int i =0; i<y; i++){
	for(int j=0; j<x; j++){
	  printf("%c", grid[j][i]);
	}
	printf("\n");
      }
    }
  }
  
  return 0;
}