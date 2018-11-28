#include <stdio.h>
#include <stdlib.h>

int mdc( int a, int b ){
    if( b==0 )
        return a;
    else
        return mdc(b,a%b);    
}

int main(){
    int t, n, v[10];
    int i, j, k;
    FILE * saida = fopen("warn.out","w");
    scanf("%d",&t);
    for( i=1 ; i<=t ; i++ ){
         scanf("%d",&n);
         for( j=1 ; j<=n ; j++ )
              scanf("%d",&v[j]);
         if( n==2 )
             v[3]=v[2];
         k=mdc(abs(v[1]-v[2]),abs(v[2]-v[3]));
         fprintf(saida,"Case #%d: %d\n",i,(k-v[1]%k)%k);
    }
    fclose(saida);
    return 0;   
}
