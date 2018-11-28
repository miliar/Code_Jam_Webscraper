#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MaxN 10005
#define oo 1000000
int T,t,N,V,i;
int left[MaxN],right[MaxN],u,flag,Ans;
int A[MaxN],B[MaxN],C[MaxN];
bool change[MaxN];
FILE *In=fopen("A-large.in","r");
FILE *Out=fopen("A-large.out","w");

int get_B(int cur)
{
    if (B[cur]!=-1) return B[cur];
    if (A[cur]==1) B[cur]=get_B(left[cur])&get_B(right[cur]);
    else B[cur]=get_B(left[cur])|get_B(right[cur]);
    return B[cur];
}

int solve(int cur)
{
    if (C[cur]!=-1) return C[cur];
    C[cur]=oo;
    if (A[cur]==1)
    {
        if (B[cur]==1)
            C[cur]<?=(solve(left[cur]))<?(solve(right[cur]));
        else
        {
            if (!B[left[cur]] && !B[right[cur]])
            {
                if (change[cur])
                    C[cur]<?=(solve(left[cur])+1)<?(solve(right[cur])+1);
                else
                    C[cur]<?=solve(left[cur])+solve(right[cur]);
            }
            else
            {
                if (change[cur])
                    C[cur]<?=1;
                else
                {
                    if (B[left[cur]])
                        C[cur]<?=solve(right[cur]);
                    else
                        C[cur]<?=solve(left[cur]);
                }
            }
        }
    }
    else
    {
        if (B[cur]==0)
            C[cur]<?=(solve(left[cur]))<?(solve(right[cur]));
        else
        {
            if (B[left[cur]] && B[right[cur]])
            {
                if (change[cur])
                    C[cur]<?=(solve(left[cur])+1)<?(solve(right[cur])+1);
                else
                    C[cur]<?=solve(left[cur])+solve(right[cur]);
            }
            else
            {
                if (change[cur])
                    C[cur]<?=1;
                else
                {
                    if (B[left[cur]])
                        C[cur]<?=solve(left[cur]);
                    else
                        C[cur]<?=solve(right[cur]);                    
                }
            }
        }
    }
    return C[cur];
}

int main()
{
    fscanf(In,"%d",&T);
    for(t=1;t<=T;t++)
    {
        memset(A,0,sizeof(A));
        memset(B,-1,sizeof(B));
        memset(C,-1,sizeof(C));
        memset(change,0,sizeof(change));
        fscanf(In,"%d%d",&N,&V);
        for(i=1;i<=(N-1)/2;i++)
        {
            fscanf(In,"%d%d",&u,&flag);
            A[i]=u;
            left[i]=i*2;
            right[i]=i*2+1;
            change[i]=flag;
        }
        for(i=(N-1)/2+1;i<=N;i++)
        {
            fscanf(In,"%d",&u);
            B[i]=u;
            C[i]=oo;
        }
        get_B(1);
        if (B[1]==V) Ans=0;
        else Ans=solve(1);
        fprintf(Out,"Case #%d: ",t);
        if (Ans>=oo)
            fprintf(Out,"IMPOSSIBLE\n");
        else
            fprintf(Out,"%d\n",Ans);
    }
    return 0;
}
