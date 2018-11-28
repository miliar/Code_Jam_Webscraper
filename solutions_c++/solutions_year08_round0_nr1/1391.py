#include<stdio.h>
#include<string.h>
#define Sm 128
#define Qm 1024
#define min(a,b) ((a)<(b)?(a):(b))
char S[Sm][Sm],Q[Qm][Sm];
int M[Qm][Sm],s,q;

void read()
{
    int i;

    scanf("%d ",&s);
    for(i=0;i<s;++i)
        gets(S[i]);
    scanf("%d ",&q);
    for(i=0;i<q;++i)
        gets(Q[i]);
}

int solve()
{
    int i,j,k,ans=q;

    memset(M[q],0,Sm*sizeof(int));

    for(i=q-1;i>=0;--i)
        for(j=0;j<s;++j)
            if(strcmp(Q[i],S[j]))
                M[i][j]=M[i+1][j];
            else
                for(M[i][j]=q,k=0;k<s;++k)
                    if(k!=j)
                        M[i][j]=min(M[i][j],1+M[i+1][k]);

    for(j=0;j<s;++j)
        ans=min(ans,M[0][j]);
    return ans;
}

int main()
{
    int n,i;

    freopen("universe.in","r",stdin);
    freopen("universe.out","w",stdout);

    scanf("%d",&n);
    for(i=1;i<=n;++i)
    {
        read();
        printf("Case #%d: %d\n",i,solve());
    }
    return 0;
}

