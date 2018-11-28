#include<cstdio>
char mp[50][52];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    gets(mp[0]);
    for (int cas=1;cas<=t;cas++)
    {
        printf("Case #%d:\n",cas);
        int r,c;
        scanf("%d%d",&r,&c);
        gets(mp[0]);
        for (int i=0;i<r;i++)
            gets(mp[i]);
        bool flag=true;
        for (int i=0;i<r;i++)
            for (int j=0;j<c;j++)
                if (mp[i][j]=='#')
                    if (i<r-1 && j<c-1 && mp[i][j+1]=='#' && mp[i+1][j]=='#' && mp[i+1][j+1]=='#')
                    {
                        mp[i][j]=mp[i+1][j+1]='/';
                        mp[i+1][j]=mp[i][j+1]='\\';
                    }
                    else
                        flag=false;
        if (!flag)
            puts("Impossible");
        else
            for (int i=0;i<r;i++)
                puts(mp[i]);
    }
}
