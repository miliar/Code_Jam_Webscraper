#include<stdio.h>
#include<iostream>
using namespace std;
FILE *fpin=fopen("D-large.in","r");
FILE *fpout=fopen("d.out","w");
int main()
{
    int i,j,n,k,l,o,p;
    double m;
    int a[1005];
    bool b[1005];
    fscanf(fpin,"%d",&p);
    for(o=1;o<=p;o++)
    {
       fprintf(fpout,"Case #%d: ",o);
       fscanf(fpin,"%d",&n);
       m=0;
       for(i=1;i<=n;i++)
        {
           fscanf(fpin,"%d",&a[i]);
           if(a[i]!=i) m+=1;
        }
        fprintf(fpout,"%.6lf\n",m);
    }
    fclose(fpin);
    fclose(fpout);
}
