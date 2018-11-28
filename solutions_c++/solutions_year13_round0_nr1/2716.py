#include <cstdio>
#include <cstdlib>

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int cases ;
    char str[4][5];
    scanf("%d",&cases);

    for(int i = 1 ; i <= cases ; i++)
    {
        for(int j = 0 ; j < 4 ; j++)
        scanf("%s",str[j]);
        bool find = false ;
        bool GameEnd = true ;
        char won ;

        for(int j = 0 ; j < 4 ; j++)
        {

            if(str[0][j] =='.')
            {
                GameEnd = false ;
                continue ;
            }

            won = str[0][j];
            for(int k = 1 ; k < 4 ; k++)
            {
                if(won == 'T')
                {
                    won = str[k][j];
                }
                else
                {
                    if(str[k][j] =='.')
                    {
                        GameEnd = false ;
                        break ;
                    }
                    if(won == str[k][j] || str[k][j] == 'T')
                    {
                    }
                    else break ;
                }
                if(k == 3)
                {
                    find = true ;
                    goto FIND_FLAG ;
                }
            }
        }

        for(int j = 0 ; j < 4 ; j++)
        {
            if(str[j][0] =='.')
            {
                GameEnd = false ;
                continue ;
            }
            won = str[j][0];
          //  if(j == 0) printf("check %c\n",won);
            for(int k = 1 ; k < 4 ; k++)
            {
                if(won == 'T')
                {
                    won = str[j][k];
                }
                else
                {
                //    if(j == 0)  printf("check %c\n",str[j][k]);
                    if(str[j][k] =='.')
                    {
                        GameEnd = false ;
                        break ;
                    }

                    if(won == str[j][k] || str[j][k] == 'T')
                    {
                    }
                    else break ;
                }
                if(k == 3)
                {
                    find = true ;
                    goto FIND_FLAG ;
                }
            }
        }
        won = str[0][0];
        if(won == '.')
        {
            GameEnd = false ;
        }
        else
        {
            for(int j = 1 ; j < 4 ; j++)
            {
                if(won == 'T')
                {
                    won = str[j][j] ;
                }
                else
                {
                    if(str[j][j] =='.')
                    {
                        GameEnd = false ;
                        break ;
                    }
                    if(str[j][j] == won || str[j][j] =='T')
                    {
                    }
                    else break ;
                }

                if(j == 3)
                {
                    find = true ;
                    goto FIND_FLAG ;
                }
            }
        }


        won = str[0][3];
        //if(i == 4) printf("check %c\n",won);
        if(won == '.')
        {
            GameEnd = false ;
        }
        else
        {
            for(int j = 1 ; j < 4 ; j++)
            {
                if(won == 'T')
                {
                    won = str[j][3-j] ;
                }
                else
                {
                    if(str[j][3-j] =='.')
                    {
                        GameEnd = false ;
                        break ;
                    }

                    if(str[j][3-j] == won || str[j][3-j] =='T')
                    {
                    }
                    else break ;
                }

                if(j == 3)
                {
                    find = true ;
                    goto FIND_FLAG ;
                }
            }
        }


        FIND_FLAG:
        if(find)
        {
            printf("Case #%d: %c won\n",i,won);
        }
        else
        {
            if(!GameEnd) printf("Case #%d: Game has not completed\n",i);
            else printf("Case #%d: Draw\n",i);
        }
    }
    return 0 ;
}
