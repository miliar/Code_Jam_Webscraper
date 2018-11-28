
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    FILE * fin, * fout;
    fin=fopen("A-large.in","r");
    fout=fopen("1.out","w");
    int t,pd,pg,i,j,flag;
    long long n;
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;i++)
    {
        fscanf(fin,"%d %d %d",&n,&pd,&pg);
        flag=0;
        if (n<100)
        {
                  for (j=1;j<=n;j++)
                       if ((pd*j)%100==0)
                       {
                                         flag=1;
                                         break;
                                         }
                  }
        else flag=1;
        if ((pg==100)&&(pd!=100)&&(flag==1)) flag=0;
        if ((pg==0)&&(pd!=0)&&(flag==1)) flag=0;
        if (flag) fprintf(fout,"Case #%d: Possible\n",i);
        else fprintf(fout,"Case #%d: Broken\n",i);
        }
    fclose(fin);
    fclose(fout);
    return 0;
    }






