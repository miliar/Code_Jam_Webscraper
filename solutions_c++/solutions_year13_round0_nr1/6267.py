#include<stdio.h>

char ch[6][6] = {"0000"};
int judge1()
{
    int i = 0;
    int j = 0;
    int x_t = 0;
    int o_t = 0;
    int k_t = 0;
    int t_t = 0;
    int flag = 1;
    for(i = 0; i < 4; i++)
        {
            o_t = 0,t_t = 0,x_t = 0;

            for(j = 0; j < 4; j++)
            {
            if(ch[i][j] == 'O')
                o_t++;
            if(ch[i][j] == 'X')
                x_t++;
            if(ch[i][j] == '.')
                k_t++;
            if(ch[i][j] == 'T')
                t_t++;
            //printf("%c",ch[i][j]);
            }
            //printf("\n%d %d  %d %d \n",x_t,o_t,k_t,t_t);
        if(o_t + t_t == 4)
            {
                flag = 0;
                return 1;
                break;
            }
        else if(4 == x_t + t_t)
        {
            flag = 0;
            return 2;
            break;
        }
        }
        if(k_t)
        {
            flag = 0;
            return 0;
        }
        if(flag)
            return 3;
}

int judge2()
{
    int i = 0;
    int j = 0;
    int x_t = 0;
    int o_t = 0;
    int k_t = 0;
    int t_t = 0;
    for(j = 0; j < 4; j++)
    {
        o_t = 0,t_t = 0,x_t = 0;
        for(i = 0; i < 4; i++)
            {
            if(ch[i][j] == 'O')
                o_t++;
            if(ch[i][j] == 'X')
                x_t++;
            if(ch[i][j] == '.')
                k_t++;
            if(ch[i][j] == 'T')
                t_t++;
            }
        if(o_t + t_t== 4)
            {
                return 1;
                break;
            }
        else if(x_t + t_t == 4)
        {
            return 2;
            break;
        }
        }
    return -100;
}

int judge3()
{
    int x_t = 0;
    int o_t = 0;
    int k_t = 0;
    int t_t = 0;
    int i = 0;
    for(i = 0; i < 4; i++)
        {
            if(ch[i][i] == 'O')
                o_t++;
            if(ch[i][i] == 'X')
                x_t++;
            if(ch[i][i] == 'T')
                t_t++;
        }
        if(o_t + t_t == 4)
            return 1;
        else if(x_t + t_t == 4)
            return 2;
    else return -100;
             //printf("o = %d  x = %d  t %d \n",o_t,x_t,t_t);
}

int judge4()
{
    int i = 0;
    int j = 0;
    int x_t = 0;
    int o_t = 0;
    int t_t = 0;
    for(i = 3,j = 0; j < 4;)
    {
        if(ch[j][i] == 'X')
            x_t++;
        if(ch[j][i] == 'O')
            o_t++;
        if(ch[j][i] == 'T')
            t_t++;

            j++;
            i--;
    }
    if(x_t + t_t == 4)
        return 2;
    else if(o_t + t_t == 4)
        return 1;
    else return -100;

        //printf("o = %d  x = %d  %d \n",o_t,x_t,t_t);
}

void print(int k)
{
    if(k == 1)
        printf(" O won\n");
    else if(k == 2)
        printf(" X won\n");
    else if(k == 3)
        printf(" Draw\n");
    else
        printf(" Game has not completed\n");

}
int main()
{
    //freopen("1.txt","r",stdin);
    //freopen("2.txt","w",stdout);
    int T;
    int w= 0;
    scanf("%d",&T);
    for(w = 1; w <= T; w++)
    {
        int i = 0;
        int j = 0;
        for(i = 0; i < 4; i++)
                //for(j = 1; j < 5; j++)
                    scanf("%s",ch[i]);

            int k = 100;
            printf("Case #%d:",w);
            k = judge4();
            //printf(" k== %d\n",k);
            if(k == 1||k == 2)
                print(k);
            else
            {
                k = judge3();
                if(k == 1 || k ==2)
                    print(k);
                else
                {
                    k = judge2();
                    if(k == 1 || k ==2)
                        print(k);
                    else
                    {
                        k = judge1();
                        print(k);
                    }
                }
            }

    }
    return 0;
}
