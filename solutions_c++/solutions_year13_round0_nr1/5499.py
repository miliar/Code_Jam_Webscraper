#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char map[5][5];
int main()
{
   // freopen("in.txt","r",stdin);
  //  freopen("a.txt","w",stdout);
    int t;
    char a;
    int cas=0;
    int tt;
    scanf("%d\n",&t);
    while(t--)
    {
        printf("Case #%d: ",++cas);
        tt=0;
        int ans=0;
        int num1;
        int num2;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf("%c",&map[i][j]);
                if(map[i][j]=='.')
                {
                    tt++;
                }
            }
            getchar();
        }
        getchar();
        for(int i=0; i<4; i++)
        {
            num1=0;
            num2=0;
            for(int j=0; j<4; j++)
            {
                if(map[i][j]=='X'||map[i][j]=='T') num1++;
                if(map[i][j]=='T'||map[i][j]=='X') num2++;
            }
            if(num1==4)
            {
                a='X';
                ans=1;
                break;
            }
            if(num2==4)
            {
                a='O';
                ans=1;
                break;
            }
        }
        if(!ans)
        {
            for(int j=0; j<4; j++)
            {
                num1=0;
                num2=0;
                for(int i=0; i<4; i++)
                {
                    if(map[i][j]=='X'||map[i][j]=='T') num1++;
                    if(map[i][j]=='T'||map[i][j]=='O') num2++;
                }
                if(num1==4)
                {
                    ans=1;
                    a='X';
                    break;
                }
                else if(num2==4)
                {
                    ans=1;
                    a='O';
                    break;
                }
            }
        }
        if(!ans)
        {
            num1=0;
            num2=0;
            for(int i=0; i<4; i++)
            {
                if(map[i][i]=='X'||map[i][i]=='T') num1++;
                if(map[i][i]=='O'||map[i][i]=='T') num2++;
            }
            if(num1==4)
            {
                ans=1;
                a='X';
            }
            else if(num2==4)
            {
                ans=1;
                a='O';
            }
        }
        if(!ans)
        {
            num1=0;
            num2=0;
            int a=0;
            int b=3;
            for(int i=0; i<4; i++)
            {
                if(map[a+i][b-i]=='X'||map[a+i][b-i]=='T') num1++;
                if(map[a+i][b-i]=='O'||map[a+i][b-i]=='T') num2++;
            }
            if(num1==4)
            {
                ans=1;
                a='X';
            }
            else if(num2==4)
            {
                ans=1;
                a='O';
            }
        }
        if(ans)
        {
            printf("%c won\n",a);
        }
        else
        {
            if(tt) printf("Game has not completed\n");
            else printf("Draw\n");
        }
    }
    return 0;
}
