#include <stdio.h>
#include <iostream>
#define MAXZ 8

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int comp (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}


int main (void)
{
    int T,n,i,j;
    int v1[MAXZ], v2[MAXZ];
    long int soma;
    
    scanf("%d",&T);
    
    for (i=1; i<=T; i++)
    {
        scanf("%d",&n);
        
        for(j=0;j<n;j++)
        {
         scanf("%d ",&v1[j]);                
        }
                
        for(j=0;j<n;j++)
        {
         scanf("%d ",&v2[j]);                
        }
         
         qsort (v1, n, sizeof(int), compare);
         qsort (v2, n, sizeof(int), comp);
       
         soma = 0;
         for(j=0; j<n; j++)
         soma += v1[j]*v2[j];
         
         printf("Case #%d: %d\n",i,soma);
    }
}
