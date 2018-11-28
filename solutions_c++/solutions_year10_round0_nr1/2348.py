#include <stdio.h>

int main(){
    int t, n, k, i;
    FILE *saida=fopen("saida.out","w");
    scanf("%d",&t);
    for( i=1 ; i<=t ; i++ ){
         scanf("%d %d",&n,&k);
         fprintf(saida,"Case #%d: ",i);
         if( ((k+1)%(1<<n))==0 )
             fprintf(saida,"ON\n");
         else
             fprintf(saida,"OFF\n");
    }
    fclose(saida);
    return 0;   
}
