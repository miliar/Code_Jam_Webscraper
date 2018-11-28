#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXk 6
#define MAXs 1010
#define INF 0x3f3f3f3f

int calc(char S[], int ssize){
  int i,val=0;
  char last = '\0';

  for(i=0 ; i<ssize ; i++)
    if(S[i]!=last){
      last=S[i];
      val++;
    }

  return val;
}

int main(){
  int nt,nt0;
  int perm[MAXk];
  int k,ssize, num,min;
  char S[MAXs],Saux[MAXs];
  int i,j;

  scanf(" %d", &nt0);
  for(nt=1 ; nt<=nt0 ; nt++){
    scanf(" %d", &k);
    scanf(" %s", S);
    ssize = strlen(S);

    num = ssize/k; min = INF;
    for(i=0 ; i<k ; i++) perm[i]=i;

    do{
      for(j=0 ; j<num ; j++)
	for(i=0 ; i<k ; i++)
	  Saux[i+k*j]=S[perm[i]+k*j];

      min <?= calc(Saux,ssize);
    } while(next_permutation(perm, perm+k));

    printf("Case #%d: %d\n", nt, min);
  }

  return 0;
}
