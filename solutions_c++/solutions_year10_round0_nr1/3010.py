#include<stdio.h>

int pow2(int n)
{
    int i,s=1;
    for (i=0;i<n;i++) s=s*2;
    return s;
}

int main()
{
    int i,T,N,K;
    FILE *fp;
    fp=fopen("a.in","r");
    fscanf(fp,"%d",&T);
    for (i=1;i<=T;i++){
        fscanf(fp,"%d%d",&N,&K);
        if ((K+1)%pow2(N)==0) printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
    fclose(fp);
    return 0;
}
