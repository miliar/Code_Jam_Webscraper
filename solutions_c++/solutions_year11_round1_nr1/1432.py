#include <stdio.h>
#include <stdlib.h>
#include <list>

using namespace std;


int main(){
  int t, i, n, pd, pg, base, base2;


  freopen("A-small.in", "r", stdin);
  freopen("A-small.out", "w", stdout);


  scanf("%d", &t);
  for(i=1; i <= t; i++){
    scanf("%d %d %d", &n, &pd, &pg);

    printf("Case #%d: ", i);
    
    if((pg == 100) && (pd != 100)){
      printf("Broken\n");
      continue;
    }
    if((pg == 0) && (pd != 0)){
      printf("Broken\n");
      continue;
    }
    
    base = 100;
    
    if(!(pd %2)){
      pd /= 2;
      base /= 2;
    }

    if(!(pd %2)){
      pd /= 2;
      base /= 2;
    }

    if(!(pd %5)){
      pd /= 5;
      base /= 5;
    }

    if(!(pd %5)){
      pd /= 5;
      base /= 5;
    }

    if(n < base){
      printf("Broken\n");
      continue;
    }


    base2 = 100;
    if(!(pg %2)){
      pg /= 2;
      base2 /= 2;
    }

    if(!(pg %2)){
      pg /= 2;
      base2 /= 2;
    }

    if(!(pg %5)){
      pg /= 5;
      base2 /= 5;
    }

    if(!(pg %5)){
      pg /= 5;
      base2 /= 5;
    }


    if(base <= base2)
      printf("Possible\n");
    else{
      printf("Broken\n");
    }
  }

  return 0;
}
