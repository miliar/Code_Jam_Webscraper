#include <string>
#include <vector>
#include <set>
#include <algorithm>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main()
{
  FILE* fin = fopen("small.in","r");
  FILE* fout = fopen("small.out","w"); 

  int board[] = {1, 2, 4, 5, 10, 20, 25, 50};

  int t;
  fscanf(fin, "%d\n", &t);
  for(int j = 0; j < t; j++){
    unsigned int n;
    int pd, pg;
    fscanf(fin, "%u %d %d\n",&n, &pd, &pg);
    printf("n = %u\n",n);
    bool p = false;
    if(pg == 100 || pg == 0){
      if(pd == pg)
	p = true;
      else
	p = false;
    }else{

      if(n >= 100){
	p=true;
	goto result;
      }

      for(int i = 0; i < 8; i++){	
	if(n >= board[i]){
	  if(pd%(100/board[i]) == 0){
	    p = true;
	    goto result;
	  }
	}else{
	  goto result;
	}
      }
      
    }   
    
    result:
    if(p)
      fprintf(fout, "Case #%d: Possible\n", j+1);
    else
      fprintf(fout, "Case #%d: Broken\n", j+1);
  }

  fclose(fin);
  fclose(fout);

  return 0;
}
