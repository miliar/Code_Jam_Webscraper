#include<stdio.h>
int main()
{
    FILE *fp,*fp1;
    int t,n=0,count=0;
    fp=fopen("gr.out","w");
    fp1=fopen("gr.in","r");
    fscanf(fp1,"%d",&t);
    for(int i=0;i<t;i++)
    {
                     fscanf(fp1,"%d",&n);
                     for(int j=0;j<n;j++)
                     {
                                      int k;
                                      fscanf(fp1,"%d",&k);
                                      if((j+1)!=k)
                                        count++;
                     }
                     fprintf(fp,"Case #%d:\t %d\n",i+1,count);
                     count=0;
    }
    return 0;
}
