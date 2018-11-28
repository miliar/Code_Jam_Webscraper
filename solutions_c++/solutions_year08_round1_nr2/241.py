
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

char *sep=" \r\n\t";

void chomp(char *s) {
  while(strlen(s)>0 && s[strlen(s)-1] < 32)
    s[strlen(s)-1] = 0;
}

int satisfy(int *malt, int p, int N, int M, int *tv, int **v1, int **v2) {
  int i,j,fm;

  if (p>=N) {

    // check all constraints

    fm = 0;
    for(i=0;i<M;i++) {
      for(j=0;j<tv[i];j++) {
	if (malt[v1[i][j]] == v2[i][j]) {
	  fm++;
	  break;
	} 
      }
    }
    if (fm==M) return 1; else return 0;
  }

  malt[p] = 0;
  if (satisfy(malt,p+1,N,M,tv,v1,v2)) return 1;
  malt[p] = 1;
  if (satisfy(malt,p+1,N,M,tv,v1,v2)) return 1;
  return 0;
}


int main(int argc, char **argv) {

  char s[512],*p;
  int i,j,k,C,N,M,T,r;

  int *v1[2000],*v2[2000],*malt,*tv;

  fgets(s,512,stdin); chomp(s); C=atoi(s);

  for(i=0;i<C;i++) {
    fgets(s,512,stdin); chomp(s); N=atoi(s);
    fgets(s,512,stdin); chomp(s); M=atoi(s);

    malt = new int[N];
    for(j=0;j<N;j++) malt[j]=0;

    tv = new int[M];
    for(j=0;j<M;j++) {
      fgets(s,512,stdin); chomp(s);
      p = strtok(s,sep);
      T = atoi(p);
      tv[j] = T;
      v1[j] = new int[T];
      v2[j] = new int[T];
      for(k=0;k<T;k++) {
	p=strtok(NULL,sep); v1[j][k]=atoi(p)-1;
	p=strtok(NULL,sep); v2[j][k]=atoi(p);
      }
    }

    r = satisfy(malt, 0, N, M, tv, v1, v2);
    printf("Case #%d:",i+1);
    if (!r)
      printf(" IMPOSSIBLE\n");
    else {
      for(j=0;j<N;j++) printf(" %d",malt[j]);
      printf("\n");
    }
      

    delete malt;
    delete tv;
    for(j=0;j<M;j++) { delete v1[j]; delete v2[j]; }

  }


  return 0;
}
