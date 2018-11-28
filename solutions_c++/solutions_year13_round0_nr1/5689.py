#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define N 16
char map[N][N];
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int n;
    scanf("%d",&n);
    for(int kase=1;kase<=n;kase++)
    {
        printf("Case #%d: ",kase);
        int flag=0;
        int tt=0,tx,ty;
        for(int i=0;i<4;i++)
        {
            scanf("%s",map[i]);
        }
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(map[i][j]=='T')
                {
                    tt++;
                }
        int nx=0,no=0;
        tx=-1,ty=-1;
        for(int i=0;i<4;i++)
        {
            nx=0,no=0;
            for(int j=0;j<4;j++)
            {
                if(map[i][j]=='T')
                {
                    tx=i,ty=j;
                }
                else if(map[i][j]=='X')
                    nx++;
                else if(map[i][j]=='O')
                    no++;
            }
            if((nx==4) || (tx == i && nx==3))
            {
                flag=1;
                break;
            }
            else if((no==4) || (tx == i && no==3))
            {
                flag=2;
                break;
            }
            if(flag)
                break;
        }
        if(flag == 0)
        {
            for(int j=0;j<4;j++)
            {
                nx=0,no=0;
                for(int i=0;i<4;i++)
                {
                    if(map[i][j]=='X')
                        nx++;
                    else if(map[i][j]=='O')
                        no++;
                }
                if((nx==4) || (ty == j && nx==3))
                {
                    flag=1;
                    break;
                }
                else if((no==4) || (ty == j && no==3))
                {
                    flag=2;
                    break;
                }
                if(flag)
                    break;
            }
        }
        if(flag == 0)
        {
            nx=0,no=0;
            for(int i=0;i<4;i++)
            {
                if(map[i][i]=='X')
                    nx++;
                else if(map[i][i]=='O')
                    no++;
            }
            if(nx==4||(tx == ty && nx==3))
            {
                flag=1;
            }
            else if(no==4||(tx == ty && no==3))
            {
                flag=2;
            }
        }
        if(flag == 0)
        {
            nx=0,no=0;
            for(int i=3;i>=0;i--)
            {
                if(map[3-i][i]=='X')
                    nx++;
                else if(map[3-i][i]=='O')
                    no++;
            }
            if(nx==4|| (tx + ty == 3 && nx==3))
            {
                flag=1;
            }
            else if(no==4||(tx + ty == 3 && no==3))
            {
                flag=2;
            }
        }
        if(flag == 0)
        {
            int fin=0;
            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    if(map[i][j]=='.')
                    {
                        fin=1;
                        break;
                    }
            if(fin==0)
                printf("Draw\n");
            else
                printf("Game has not completed\n");
        }
        else if(flag == 1)
            printf("X won\n");
        else if(flag == 2)
            printf("O won\n");
    }
    return 0;
}
