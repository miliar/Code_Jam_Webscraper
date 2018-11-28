#include <stdio.h>
#include <iostream>
using namespace std;

#define fori(a,b) for(a=0; (a)<(b); a++ )
#define MAX 102

int H,W;
int ALT[MAX][MAX];
char BAS[MAX][MAX];

void flow( int i, int j, char *let ) {
  if( BAS[i][j] != '@' ) *let = BAS[i][j];
  else {
    int min=ALT[i][j],ni=0,nj=0;
    if( (i-1)>-1 &&  ALT[i-1][j]<min ){
      min = ALT[i-1][j];
      ni=i-1; nj=j;
    }
    if( (j-1)>-1 && ALT[i][j-1]<min ) {
      min = ALT[i][j-1];
      ni=i; nj=j-1;
    }
    if( (j+1)<W && ALT[i][j+1]<min ) {
      min = ALT[i][j+1];
      ni=i; nj=j+1;
    }
    if( (i+1)<H && ALT[i+1][j]<min ) {
      min = ALT[i+1][j];
      ni=i+1; nj=j;
    }
    if( min<ALT[i][j] )
      flow( ni, nj, let );
    BAS[i][j] = *let;
  }
}

int main() {
  int i,j,N,T=1;

  scanf("%d",&N);
  while( N-- ) {
    scanf("%d %d",&H,&W);

    fori(i,H) fori(j,W) {
      scanf("%d",&ALT[i][j]);
      BAS[i][j] = '@';
    }
    char let='a',tmp;
    fori(i,H) fori(j,W) {
      tmp = let;  
      flow( i, j, &tmp );
      if( tmp==let )
        let++;
    }
    printf("Case #%d:\n",T++);
    fori(i,H) {
      fori(j,W) {
        if( j ) printf(" %c",BAS[i][j]);
	else printf("%c",BAS[i][j]);
      }
      puts("");
    }
  }

  return 0;
}
