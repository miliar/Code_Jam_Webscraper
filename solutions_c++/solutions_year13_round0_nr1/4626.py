#include <iostream>
#include <cstdio>
using namespace std;
char map[6][6];
bool judgeRow(int x,int y)
{
    bool flag  = true;
    for(int i =1;i<=4;i++)
    {
        if(map[x][y] != map[x][i] && map[x][i] != 'T')
            flag  = false;
    }
     return flag;
}
bool judgexie_1(int x,int y)
{
    if(x!= y)
        return false;
    bool flag =true;
    for(int i =1;i <= 4;i++)
    {
        if(map[i][i] != map[x][y] &&map[i][i] != 'T')
            flag = false;
    }
    return flag;
}
bool judgexie_2(int x,int y)
{
    if(y == 4)
    {
        int ffff = 1;
    }
    if(x !=  (5-y))
        return false;
    bool flag = true;
    for(int i =1;i <= 4;i++)
    {
        if(map[i][5-i] != map[x][y] && map[i][5-i] != 'T')
            flag   = false;
    }
    return flag;
}
bool judgeCol(int x,int y)
{
    bool flag  = true;
    for(int i = 1;i <= 4;i++)
    {
        if(map[i][y] != map[x][y] && map[i][y] != 'T')
            flag  = false;
    }
    return flag;
}
bool judge(int x,int y)
{
    if( map[x][y] != 'T'&&judgeRow(x,y) || judgeCol(x,y) || judgexie_1(x,y) || judgexie_2(x,y))
    {
        printf("%c won\n",map[x][y]);
        return true ;
    }
}
bool del()
{
    bool flag  = false;
    for(int i = 1;i <= 4;i++)
    {
        for(int j = 1;j <= 4;j++)
        {
            if(map[i][j] != '.')
               if(judge(i,j))
                    return true;
        }
    }
    return false;
}
int main()
{
    //freopen("in.in", "r",stdin);
   // freopen("out.txt" , "w" ,stdout);
    int ncase,tmp =1;
    scanf("%d",&ncase);
    while(ncase--)
    {
        bool kong  = false;
        for(int i =1;i<=4;i++)
            for(int j =1;j<=4;j++)
               {
                   cin>>map[i][j];
                   if(map[i][j] == '.')
                        kong  = true;
               }
        printf("Case #%d: ",tmp++);
        if(del() == false)
        {
            if(kong  == true)
            {
                printf("Game has not completed\n");
            }
            else
                printf("Draw\n");
        }
    }
    return 0;
}
