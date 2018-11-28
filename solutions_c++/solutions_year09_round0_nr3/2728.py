#include <stdlib.h>
#include <stdio.h>

int main() {
    int t,i,j,k,vai, cc;
    char a[17];
    char aux;
    char b[2000];
    int x[2000][20];
    
    
    for(i = 1; i <= 19; i++)
          scanf("%c", &a[i]);
  //  for(i = 1; i <= 19; i++)
  //        printf("%d - >> %c\n", i,a[i]);          
    //scanf("%*c");
    scanf("%d", &t);
    //printf("\n\n::%d\n\n",t);
    scanf("%*c");
    vai = 1;
cc = 0;
    while(vai && t--) {
              cc++;
        for( j = 0; j <2000; j++) {
             for( k = 0 ; k <20 ; k++ ) {
                  x[j][k] = 0;
             }
        }
        i = 0;
        vai = scanf("%c", &aux);
        while(vai == 1 && aux != '\n') {
            b[i++] = aux;
            vai = scanf("%c", &aux);
        }
        //printf("\nlookk\n");
        //printf("  -- > " );
        for( k = 0; k <i; k++ ){
             x[k][0] = 1;
             //printf("%c", b[k]);
        }
        //printf("\n\n");                
        if ( b[0] == a[1] ) x[0][1] = 1;
        for( j = 1; j <= 19; j++ ) {
             for( k = 1; k <i; k++ ){
                  if (b[k] == a[j]) x[k][j] = x[k-1][j] + x[k][j-1];
                  else x[k][j] = x[k-1][j];
             }
        }/*
        for( j = 1; j <= 19; j++ ) {
             printf("%c -- > ", a[j]);
             for( k = 0; k <i; k++ ){
                  printf("%d", x[k][j]);
             }
             printf("\n");
        }  */      
        printf("Case #%d: ", cc);printf("%04d\n", x[i-1][19]);
    }
}
