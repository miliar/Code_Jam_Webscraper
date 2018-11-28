
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    int n,t,i,j,p,sum;
    FILE * fin,* fout;
    fin=fopen("D-large.in","r");
    fout=fopen("4.txt","w");
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;i++)
    {
        sum=0;
        fscanf(fin,"%d",&n);
        for (j=1;j<=n;j++)
        {
            fscanf(fin,"%d",&p);
            if (p!=j) sum++;
            }
        fprintf(fout,"Case #%d: %d.000000\n",i,sum);
        }
    fclose(fin);
    fclose(fout);
    return 0;
    }
    
    
    
    
