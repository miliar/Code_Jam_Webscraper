#include<stdio.h>
#include<stdlib.h>
int a[1100],b[1100];
int compare(const void *x,const void *y)
{
    return (*(int*)x-*(int*)y);
}
main()
{
    FILE *fin=fopen("D-large.in","r");
    FILE *fout=fopen("goro.txt","w");
    int t,i,l,n,count=0;
    fscanf(fin,"%d",&t);
    for(l=0;l<t;l++)
    {
        count=0;
        fscanf(fin,"%d",&n);
        for(i=0;i<n;i++)
        {
            fscanf(fin,"%d",&a[i]);
            b[i]=a[i];
        }
        qsort(b,n,sizeof(int),compare);
        for(i=0;i<n;i++) if(a[i]==b[i]) count++;
        fprintf(fout,"Case #%d: %.6lf\n",l+1,(double)(n-count));
    }
}
