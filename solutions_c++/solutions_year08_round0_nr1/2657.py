#include <stdio.h>
#include <string.h>
#include <memory.h>

int N,S,Q;
char engine[100][101];
char query[1000][101];
int dp[1000][100];

int Count, MaxCount;

void dfs(int i, int j)
{
    int k;
    if(i==Q)
    {
        if(Count<MaxCount)
            MaxCount=Count;
        return;
    }
    if(strcmp(query[i], engine[j])==0) return;
    for(k=0; k<S; k++)
    {
        if(k!=j) Count++;
        dfs(i+1, k);
        if(k!=j) Count--;
    }
}

int dfs1(int i, int j)
{
    int k, m, n;
    if(dp[i][j]!=-1) return dp[i][j];
    if(i==Q) return 0;
    m=Q;
    for(k=0; k<S; k++)
    {
        if(strcmp(query[i], engine[k])==0) continue;
        n=dfs1(i+1, k);
        if(k!=j) n++;
        if(n<m) m=n;
    }
    dp[i][j]=m;
    return m;
}

int main()
{
    int i,j,k;

    FILE* fp1 = freopen("A-small-attempt1.in", "r", stdin);
    FILE* fp2 = freopen("A-Out.txt", "w", stdout);

    scanf("%d\n", &N);
    for(i=1; i<=N; i++)
    {
        scanf("%d\n", &S);
        for(j=0; j<S; j++) gets(engine[j]);
        scanf("%d\n", &Q);
        for(j=0; j<Q; j++) gets(query[j]);

        Count=0; MaxCount=Q;
        //for(k=0; k<S; k++)
        //    dfs1(0, k);

        memset(dp, -1, sizeof(dp));
        for(k=0; k<S; k++)
        {
            Count=dfs1(0, k);
            if(Count<MaxCount)
                MaxCount=Count;
        }

        printf("Case #%d: %d\n", i, MaxCount);
    }

    fclose(fp1);
    fclose(fp2);

    return 0;
}
