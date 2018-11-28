#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 10000

char s[MAX];
int arr[MAX];

main()
{
      int n,T,nc=1,k,t,min,indice,rec,c;
      char aux[MAX];
      FILE *in = fopen("D-small-attempt0.in","r");
      FILE *out = fopen("D-small.out","w");
      //FILE *in = fopen("C-large.in","r");
      //FILE *out = fopen("C-large.out","w");
      fscanf(in,"%d",&T);
      while(T--)
      {
             fscanf(in,"%d %s",&k,s);
             t = strlen(s);
             min = t;
             for(int i=0;i<k;i++) arr[i] = i;
             do
             {
                    strcpy(aux,s); 
                    for(int i=0;i<t;i++)
                            aux[i] = s[(i/k)*k+arr[i%k]];
                    indice=c=0;
                    while(indice<t)
                    {
                                   for(rec=indice;rec<t&&aux[rec]==aux[indice];rec++);
                                   c++;
                                   indice = rec;
                    }
                    min <?= c;
                    //for(int i=0;i<k;i++) printf("%d ",arr[i]);   
                    //printf("%s\n",aux);                       
             } while(next_permutation(arr,arr+k));
             fprintf(out,"Case #%d: %d\n",nc++,min);
      }
      fclose(out);
      system("PAUSE");
      return 0;
}
