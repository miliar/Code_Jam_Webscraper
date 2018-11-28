#include <iostream>
#include <stdio.h>

#define MAXN 1234
using namespace std;

int main (){

  int t, r, k, n, v[MAXN], ptr[MAXN], val[MAXN], cases = 1;
  scanf("%d", &t);
  while(t--){
    scanf("%d %d %d", &r, &k, &n);

    printf("Case #%d: ", cases++);

    int sum = 0;
    for(int i=0; i<n; i++){
      scanf("%d", &v[i]);
      sum += v[i];
    }
    //special case
    if(sum <= k){
      printf("%d\n", sum*r);
      continue;
    }

    int acc = 0;
    for(int i=0, j = 0; i<n; i++){
      while(acc + v[j] <= k){
	acc += v[j];
	j = (j+1)%n;
      }
      ptr[i] = j;
      val[i] = acc;
      acc -= v[i];
    }

    // printf("ptr\n");
    // for(int i=0; i<n; i++)
    //   printf("%d ", ptr[i]);
    // printf("\n");

    // printf("val\n");
    // for(int i=0; i<n; i++)
    //   printf("%d ", val[i]);
    // printf("\n");

    int add = 0, euro = 0;
    while(r--){
      euro += val[add];
      add = ptr[add];
    }
    printf("%d\n", euro);
  }

  return 0;
}
