
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main()
{
    FILE * fp1,* fp2;
    fp1=fopen("1.txt","w");
    fp2=fopen("A-large.in","r");
    int n,m,i,j,t1,t2,time,p1,p2,pos;
    int ou[200],bi[200],a[200],b[200];
    char c;
    char sta[200];
    fscanf(fp2,"%d",&n);
    for (i=1;i<=n;i++)
    {
        t1=t2=0;
        fscanf(fp2,"%d",&m);
        ou[0]=bi[0]=1;
        for (j=1;j<=m;j++)
        {
            fscanf(fp2,"%c",&c);
            fscanf(fp2,"%c %d",&sta[j],&pos);
            if (sta[j]=='O')
            {
                       t1++;
                       ou[t1]=pos;
                       }
            else
            {
                       t2++;
                       bi[t2]=pos;
                       }      
            }
        time=0;
        for (j=1;j<=t1;j++) a[j]=abs(ou[j]-ou[j-1]);
        for (j=1;j<=t2;j++) b[j]=abs(bi[j]-bi[j-1]);
        p1=p2=1;
        for (j=1;j<=m;j++)
        {
            if (sta[j]=='O')
            {
                                time=time+a[p1]+1;
                                if (b[p2]>a[p1]) b[p2]=b[p2]-a[p1]-1;
                                else b[p2]=0;
                                p1++;
                                }
            else
            {
                time=time+b[p2]+1;
                if (a[p1]>b[p2]) a[p1]=a[p1]-b[p2]-1;
                else a[p1]=0;
                p2++;
                }
            }
        fprintf(fp1,"Case #%d: %d\n",i,time);
        }
    fclose(fp1);
    return 0;
    }



