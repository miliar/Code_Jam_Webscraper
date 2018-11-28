
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    int t,n,i,j,p,min,sum,s;
    FILE * fin,* fout;
    fin=fopen("C-large.in","r");
    fout=fopen("3.txt","w");
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;i++)
    {
        fscanf(fin,"%d",&n);
        s=min=sum=0;
        for (j=1;j<=n;j++)
        {
            fscanf(fin,"%d",&p);
            if ((p<min)||(j==1)) min=p;
            sum^=p;
            s+=p;
            }
        if (!sum) fprintf(fout,"Case #%d: %d\n",i,s-min);
        else fprintf(fout,"Case #%d: NO\n",i);
        }
    fclose(fin);
    fclose(fout);
    return 0;
    }




