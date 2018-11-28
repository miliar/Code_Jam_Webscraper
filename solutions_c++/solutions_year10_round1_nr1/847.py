#include <iostream>
using namespace std;
char f[100][100];
char map[100][100];
bool Blue,Red;
int k,n;
void checkR(int a,int b)
{
    char sex='R';
    bool ok;
    int i,j;
    ok=false;
    for (i=1;i<=k;i++)
    {
        if (b+i-1<=n&&map[a][b+i-1]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Red=true;
        return;
    }
    for (i=1;i<=k;i++)
    {
        if (a-i+1>0&&map[a-i+1][b]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Red=true;
        return;
    }
    for (i=1;i<=k;i++)
    {
        if (a-i+1>0&&b+i-1<=n&&map[a-i+1][b+i-1]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Red=true;
        return;
    }
    for (i=1;i<=k;i++)
    {
        if (b-i+1>0&&a-i+1>0&&map[a-i+1][b-i+1]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Red=true;
        return;
    }


}
void checkB(int a,int b)
{
    char sex='B';
    bool ok;
    int i,j;
    ok=false;
    for (i=1;i<=k;i++)
    {
        if (b+i-1<=n&&map[a][b+i-1]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Blue=true;
        return;
    }
    for (i=1;i<=k;i++)
    {
        if (a-i+1>0&&map[a-i+1][b]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Blue=true;
        return;
    }
    for (i=1;i<=k;i++)
    {
        if (a-i+1>0&&b+i-1<=n&&map[a-i+1][b+i-1]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Blue=true;
        return;
    }
    for (i=1;i<=k;i++)
    {
        if (b-i+1>0&&a-i+1>0&&map[a-i+1][b-i+1]==sex) ok=true;
        else
        {
            ok=false;
            break;
        }
    }
    if (ok)
    {
        Blue=true;
        return;
    }


}
int main()
{
    freopen("C:/Users/FengJinwen/Desktop/A-large.in", "r", stdin);
    freopen("C:/Users/FengJinwen/Desktop/ans.txt", "w", stdout);
    int t,p,q,tp,s;
    int i,j,temp;
    scanf("%d",&t);
    for (p=1;p<=t;p++)
    {
        printf("Case #%d: ",p);
        Blue=false;
        Red=false;
        scanf("%d%d",&n,&k);
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=n;j++)
            {
                scanf("%c",&f[i][j]);
                if (f[i][j]=='\n') j--;
            }
        }
        for (i=1;i<=n;i++)
            for (j=1;j<=n;j++)
                map[i][j]=f[n-j+1][i];
        for (i=n;i>1;i--)
            for (j=1;j<=n;j++)
                if (map[i][j]=='.')
                {
                    q=i;tp==n;
                    while (map[q][j]=='.'&&tp>0)
                    {
                        for (s=q;s>0;s--)
                        {
                        map[s][j]=map[s-1][j];
                        tp--;
                        }
                    }

                }
        for (i=n;i>=1;i--)
            for (j=1;j<=n;j++)
            {
                if (map[i][j]=='R') checkR(i,j);
                else if (map[i][j]=='B') checkB(i,j);
            }
        if (Blue)
        {
            if (Red) printf("Both\n");
            else printf("Blue\n");
        }
        else
        {
            if (Red) printf("Red\n");
            else printf("Neither\n");
        }
    }
}
