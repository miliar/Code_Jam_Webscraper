#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char map[10][10];
int t;
bool full()
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(map[i][j]=='.')
                return false;
    return true;
}
bool check(char ch)
{
    bool flag;
    for(int i=0;i<4;i++)
    {
        flag=true;
        for(int j=0;j<4;j++)
            if(map[i][j]!='T' && map[i][j]!=ch)
            {
                flag=false;
                break;
            }
        if(flag) return true;
    }
    for(int i=0;i<4;i++)
    {
        flag=true;
        for(int j=0;j<4;j++)
            if(map[j][i]!='T' && map[j][i]!=ch)
            {
                flag=false;
                break;
            }
        if(flag) return true;
    }

    flag=true;
    for(int i=0;i<4;i++)
        if(map[i][i]!='T' && map[i][i]!=ch)
        {
            flag=false;
            break;
        }
    if(flag) return true;

    flag=true;
    for(int i=0;i<4;i++)
        if(map[i][3-i]!='T' && map[i][3-i]!=ch)
        {
            flag=false;
            break;
        }
    return flag;

}
int main()
{
   // freopen("D:\\AAA.in","r",stdin);
   // freopen("D:\\aaA.out","w",stdout);
    scanf("%d",&t);
    for(int cas=1; t--; cas++)
    {
        for(int i=0; i<4; i++)
            scanf("%s",map[i]);
        if(check('O'))
        {
            printf("Case #%d: O won\n",cas);
        }
        else if(check('X'))
        {
            printf("Case #%d: X won\n",cas);
        }
        else if(full())
        {
            printf("Case #%d: Draw\n",cas);
        }
        else
        {
            printf("Case #%d: Game has not completed\n",cas);
        }


    }
}
