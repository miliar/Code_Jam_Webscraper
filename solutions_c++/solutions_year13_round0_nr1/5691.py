#include <cstdio>
int main()
{
    freopen("i.txt","r",stdin);
    freopen("Ou.txt","w",stdout);
    char s[5][5];
    int t,u= 0;
    scanf("%d",&t);
    while(t --)
    {
        int flag = 0;
        for(int i = 0;i < 4;i ++)
            {
                scanf("%s",s[i]);
                for(int j = 0;j < 4;j ++)
                    if(s[i][j] == '.')
                    flag = 1;
            }

            int ss = 0;
            for(int i = 0;i < 4;i ++)
            {
                for(int j = 0;j < 4;j ++)
                if(s[i][j] == '.')
                {
                    ss ++;
                    break;
                }
            }
            if(s[0][0] == '.'||s[1][1] == '.'||s[2][2] == '.' || s[3][3] == '.')
                ss ++;
            if(s[3][0] == '.'||s[2][1] == '.'||s[1][2] == '.' || s[0][3] == '.')
                ss ++;
            if(ss == 6)
            {
                printf("Case #%d: Game has not completed\n",++u);
                continue;
            }
            for(int i = 0;i < 4;i ++)
            {
                if((s[i][0] == 'O' || s[i][0] == 'T') && (s[i][1] == 'O' || s[i][1] == 'T') && (s[i][2] == 'O' || s[i][2] == 'T') && (s[i][3] == 'O' || s[i][3] == 'T'))
                    flag = 2;
            }
            for(int i = 0;i < 4;i ++)
            {
                if((s[0][i] == 'O' || s[0][i] == 'T') && (s[1][i] == 'O' || s[1][i] == 'T') && (s[2][i] == 'O' || s[2][i] == 'T') && (s[3][i] == 'O' || s[3][i] == 'T'))
                    flag = 2;
            }
            //printf("%d\n",flag);
            if((s[0][0] == 'T'||s[0][0] == 'O') && (s[1][1] == 'T'||s[1][1] == 'O') && (s[2][2] == 'T'||s[2][2] == 'O') && (s[3][3] == 'T'||s[3][3] == 'O'))
                flag = 2;
            if((s[3][0] == 'T'||s[3][0] == 'O') && (s[2][1] == 'T'||s[2][1] == 'O') && (s[1][2] == 'T'||s[1][2] == 'O') && (s[0][3] == 'T'||s[0][3] == 'O'))
                flag = 2;
            for(int i = 0;i < 4;i ++)
            {
                if((s[i][0] == 'X' || s[i][0] == 'T') && (s[i][1] == 'X' || s[i][1] == 'T') && (s[i][2] == 'X' || s[i][2] == 'T') && (s[i][3] == 'X' || s[i][3] == 'T'))
                    flag = 3;
            }
            // printf("%d\n",flag);
            for(int i = 0;i < 4;i ++)
            {
                if((s[0][i] == 'X' || s[0][i] == 'T') && (s[1][i] == 'X' || s[1][i] == 'T') && (s[2][i] == 'X' || s[2][i] == 'T') && (s[3][i] == 'X' || s[3][i] == 'T'))
                    flag = 3;
            }
             //printf("%d\n",flag);
            if((s[0][0] == 'T'||s[0][0] == 'X') && (s[1][1] == 'T'||s[1][1] == 'X') && (s[2][2] == 'T'||s[2][2] == 'X') && (s[3][3] == 'T'||s[3][3] == 'X'))
                flag = 3;
               //  printf("%d\n",flag);
            if((s[3][0] == 'T'||s[3][0] == 'X') && (s[2][1] == 'T'||s[2][1] == 'X') && (s[1][2] == 'T'||s[1][2] == 'X') && (s[0][3] == 'T'||s[0][3] == 'X'))
                flag = 3;
                 //printf("%d\n",flag);
            if(flag == 2)
                printf("Case #%d: O won\n",++u);
            else if(flag == 3)
                printf("Case #%d: X won\n",++u);
            else
                printf("Case #%d: Draw\n",++u);

    }
    return 0;
}
