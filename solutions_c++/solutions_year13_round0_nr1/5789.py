#include <stdio.h>
#include <cstring>

int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("sum.out","w",stdout);
    int t;
    char a[5][5];
    scanf("%d",&t);
    char s[5];
    int ans=0,num=0;

    for(int p=1; p<=t; p++)
    {
        ans=num=0;
        memset(a,0,sizeof(a));
        bool flag=false;
        for(int i=1; i<=4; i++)
        {
            scanf(" %s",s);
            int len=strlen(s);
            for(int j=0; j<len; j++)
            {
                a[i][j+1]=s[j];
                if(s[j]=='.') flag=true;
            }
        }
        printf("Case #%d: ",p);
        char c;
        for(int i=1; i<=4; i++)
        {
            num=0;
            if(a[i][1]=='.') continue;
            for(int j=2; j<=4; j++)
            {
                if(a[i][j]=='.') break;
                if(a[i][j]==a[i][j-1]||a[i][j-1]=='T'||a[i][j]=='T')
                {
                    num++;
                    if(a[i][j]!='T') c=a[i][j];
                    if(a[i][j-1]!='T') c=a[i][j-1];
                }
            }
            if(num==3) break;
        }
        if(num==3)
        {
            printf("%c won\n",c);
            continue;
        }
        for(int j=1; j<=4; j++)
        {
            num=0;
            if(a[1][j]=='.') continue;
            for(int i=2; i<=4; i++)
            {
                if(a[i][j]=='.') break;
                if(a[i-1][j]==a[i][j]||a[i-1][j]=='T'||a[i][j]=='T')
                {
                    num++;
                    if(a[i][j]!='T') c=a[i][j];
                    if(a[i-1][j]!='T') c=a[i-1][j];
                }
            }
            if(num==3) break;
        }
        if(num==3)
        {
            printf("%c won\n",c);
            continue;
        }
        num=0;
        if(a[1][1]!='.')
        {
            for(int i=2; i<=4; i++)
            {
                if(a[i][i]=='.') break;
                if(a[i-1][i-1]==a[i][i]||a[i-1][i-1]=='T'||a[i][i]=='T')
                {
                    num++;
                    if(a[i][i]!='T') c=a[i][i];
                    if(a[i-1][i-1]!='T') c=a[i-1][i-1];
                }
            }
            if(num==3)
            {
                printf("%c won\n",c);
                continue;
            }
        }
        if(a[1][4]!='.')
        {
            num=0;
            for(int i=2; i<=4; i++)
            {
                if(a[i][4-i+1]=='.') break;
                if(a[i-1][4-i+2]==a[i][4-i+1]||a[i-1][4-i+2]=='T'||a[i][4-i+1]=='T')
                {
                    num++;
                    if(a[i][4-i+1]!='T') c=a[i][4-i+1];
                    if(a[i-1][4-i+2]!='T') c=a[i-1][4-i+2];
                }
            }
            if(num==3)
            {
                printf("%c won\n",c);
                continue;
            }
        }
        if(flag) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
