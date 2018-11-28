#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
char str[4][4];
bool check(int x,int y)
{
    char now=str[x][y];
    if(now=='.')
        return false;
    int i,cnt;
    cnt=1;
    //down;
    for(i=x+1;i<4;i++)
    {
        if(str[i][y]!=now&&str[i][y]!='T')
            break;
        cnt++;
    }
    for(i=x-1;i>=0;i--)
    {
        if(str[i][y]!=now&&str[i][y]!='T')
            break;
        cnt++;
    }
    if(cnt==4)
        return true;
    cnt = 1;
    //up
    for(i=y+1;i<4;i++)
    {
        if(str[x][i]!=now&&str[x][i]!='T')
            break;
        cnt++;
    }
    for(i=y-1;i>=0;i--)
    {
        if(str[x][i]!=now&&str[x][i]!='T')
            break;
        cnt++;
    }
    if(cnt==4)
        return true;
    return false;
}
int main()
{
    int T;
    freopen("A-small-attempt2.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    cin>>T;
    int ncase=0;
    while(T--)
    {
        int i,j,cnt;
        cnt=0;
        for(i=0;i<4;i++)
        {
            scanf("%s",str[i]);
            for(j=0;j<4;j++)
            {
                if(str[i][j]=='.')
                    cnt++;
            }
        }
        printf("Case #%d: ",++ncase);
        bool flagX = false;
        bool flagO = false;

        if(str[0][0]!='.'&&str[1][1]!='.'&&str[2][2]!='.'&&str[3][3]!='.')
        {
            if((str[0][0]==str[1][1]||str[0][0]=='T'||str[1][1]=='T')&&
                (str[1][1]==str[2][2]||str[1][1]=='T'||str[2][2]=='T')&&
                (str[2][2]==str[3][3]||str[2][2]=='T'||str[3][3]=='T'))
                {
                    if(str[0][0]!='T')
                        printf("%c won\n",str[0][0]);
                    else if(str[1][1]!='T')
                        printf("%c won\n",str[1][2]);
                    continue;
                }
        }
        if(str[0][3]!='.'&&str[1][2]!='.'&&str[2][1]!='.'&&str[3][0]!='.')
        {

            if((str[0][3]==str[1][2]||str[0][3]=='T'||str[1][2]=='T')&&
                (str[1][2]==str[2][1]||str[1][2]=='T'||str[2][1]=='T')&&
                (str[2][1]==str[3][0]||str[2][1]=='T'||str[3][0]=='T'))
                {
                    if(str[0][3]!='T')
                        printf("%c won\n",str[0][3]);
                    else if(str[1][2]!='T')
                        printf("%c won\n",str[1][2]);
                    continue;
                }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(check(i,j))
                {
                    if(str[i][j]=='X')
                    {
                        flagX = true;
                            break;
                    }
                    else if(str[i][j]=='O')
                    {
                        flagO = true;
                        break;
                    }
                }
            }
        }
        if(flagX==true)
        {
            printf("X won\n");
        }
        else if(flagO==true)
        {
            printf("O won\n");
        }
        else if(cnt!=0)
        {
            printf("Game has not completed\n");
        }
        else
            printf("Draw\n");
    }
    return 0;
}
