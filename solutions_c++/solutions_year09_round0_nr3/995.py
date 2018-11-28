#include<stdio.h>
#include<string.h>

char inp[510];

char pat[]="welcome to code jam";

int mod=10000;
int cache[20][510];

int ways(int i, int j)
{
    if(cache[i][j]!=-1)
        return cache[i][j];

    if(i==19)
        return cache[i][j]=1;
    if(inp[j]==0)
        return cache[i][j]=0;

    cache[i][j]=ways(i,j+1);
    if(inp[j]==pat[i])
        cache[i][j]+=ways(i+1,j+1);
    cache[i][j]%=mod;
    return cache[i][j];
}



int main()
{
    //freopen("C1.in","r",stdin);
    //freopen("C1.out","w",stdout);
    freopen("C2.in","r",stdin);
    freopen("C2.out","w",stdout);

    int n;
    scanf("%d",&n);
    gets(inp);
    for(int cs=1;cs<=n;cs++)
    {
        memset(cache,-1,sizeof(cache));
        gets(inp);
        int ans=ways(0,0);
        printf("Case #%d: %04d\n",cs,ans);
    }
    return 0;
}
