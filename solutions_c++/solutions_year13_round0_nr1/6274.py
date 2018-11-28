#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char a[4][4];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    scanf("%d",&t);

    int i,j;
    int flag,flag_x,flag_o,flag_t;
    int num_x,num_o,num_t;
    int cases;
    for(cases = 1; cases <= t; cases++)
    {
        //getchar();
        int flag = 1;
        for(i = 0; i < 4; i++)
        {
            for(j = 0; j <4 ;j++)
            {
                cin>>a[i][j];
                if(a[i][j] == '.')
                    flag = 0;
            }
        }

        flag_x = flag_o = 0;

        for(i = 0; i < 4; i++)
        {
            num_x = num_o = num_t = 0;
            for(j = 0; j < 4; j++)
            {
                if(a[i][j] == 'X') num_x++;
                else if(a[i][j] == 'O') num_o++;
                else if(a[i][j] == 'T') num_t++;
            }
            if(num_x == 3 && num_t == 1 || num_x == 4)
            {
                flag_x = 1;
                break;
            }
            else if(num_o == 3 && num_t == 1 ||num_o ==4)\
            {
                flag_o = 1;
                break;
            }
        }
        if(flag_x == flag_o && flag_x == 0)
        {
            for(j = 0; j < 4; j++)
            {
                num_x = num_o = num_t = 0;
                for(i = 0; i < 4; i++)
                {
                    if(a[i][j] == 'X') num_x++;
                    else if(a[i][j] == 'O') num_o++;
                    else if(a[i][j] == 'T') num_t++;
                }
                if(num_x == 3 && num_t == 1 || num_x == 4)
                {
                    flag_x = 1;
                    break;
                }
                else if(num_o == 3 && num_t == 1 ||num_o ==4)\
                {
                    flag_o = 1;
                    break;
                }
            }
        }
        if(flag_x == flag_o && flag_x == 0)
        {
            num_x = num_o = num_t = 0;
            for(i = 0; i < 4; i++)
            {
                if(a[i][i] == 'X')
                    num_x++;
                else if(a[i][i] == 'O')
                    num_o++;
                else if(a[i][i] == 'T')
                    num_t++;
            }

            if(num_x == 3 && num_t == 1 || num_x == 4)
            {
                flag_x = 1;
            }
            else if(num_o == 3 && num_t == 1 ||num_o ==4)
            {
                flag_o = 1;
            }
        }

        if(flag_x == flag_o && flag_x == 0)
        {
            num_x = num_o = num_t = 0;
            for(i = 0; i < 4; i++)
            {
                if(a[i][3-i] == 'X')
                    num_x++;
                else if(a[i][3-i] == 'O')
                    num_o++;
                else if(a[i][3-i] == 'T')
                    num_t++;
            }

            if(num_x == 3 && num_t == 1 || num_x == 4)
            {
                flag_x = 1;
            }
            else if(num_o == 3 && num_t == 1 ||num_o ==4)
            {
                flag_o = 1;
            }
        }



        if(flag_x == 1)
            printf("Case #%d: X won\n",cases);
        else if(flag_o == 1)
            printf("Case #%d: O won\n",cases);
        else if(flag == 0 && flag_x == 0 && flag_o == 0)
            printf("Case #%d: Game has not completed\n",cases);
        else if(flag == 1 && flag_x == 0 && flag_o == 0)
            printf("Case #%d: Draw\n",cases);

    }
    fclose(stdin);
    fclose(stdout);
}
