#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxN 50005
#define oo 50000
int T,t,N,K,i,j,Count,Ans;
char s[MaxN],s1[MaxN];
int A[20];
bool Used[20];
FILE *In=fopen("D-small.in","r");
FILE *Out=fopen("D-small.out","w");

void solve(int num)
{
    if (num==K)
    {
        int i;
        for(i=0;i<strlen(s);i++)
            s1[i/K*K+A[i%K]]=s[i];
        Count=0;
        for(i=0;i<strlen(s);i++)
            if (i==0 || s1[i]!=s1[i-1]) Count++;
        Ans<?=Count;
        return;
    }
    for(int i=0;i<K;i++)
        if (!Used[i])
        {
            Used[i]=1;
            A[num]=i;
            solve(num+1);
            Used[i]=0;
        }
}

int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        fscanf(In,"%d",&K);
        fscanf(In,"%s",&s);
        Ans=oo;
        solve(0);
        fprintf(Out,"Case #%d: %d\n",t,Ans);
    }
    return 0;
}
