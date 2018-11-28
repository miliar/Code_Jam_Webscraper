#include <iostream>
#include <stdio.h>
using namespace std;
#define maxn 4
int tem,tem2;
char map[ maxn ][ maxn ];
int checkrow(int cas)
{
    int cntx = 0 , cnty = 0 , cnt = 0 ;
    for( int i = 0 ; i < 4 ; i++ )
    {
        for( int j = 0 ; j < 4 ; j++ )
        {
            if(map[ i ][ j ] == '.')
            {
                cnt++;
                break;
            }
            if((map[ i ][ j ] == 'X' ||map[ i ][ j ] == 'T') && cnty <= 1)
            {
                cntx++;
                if(cntx==4)
                {
                    printf("Case #%d: X won\n",cas);
                    return 1;
                }
                continue;
            }
            if((map[ i ][ j ] == 'O' ||map[ i ][ j ] == 'T') && cntx <= 1)
            {
                cnty++;
                if(cnty == 4)
                {
                    printf("Case #%d: O won\n",cas);
                    return 1;
                }
                continue;
            }
            break;
        }
        cntx = cnty = 0 ;
    }
    if(cnt) return 2;
    return 3;
}
int checkcul(int cas)
{
    int cntx = 0 , cnty = 0 , cnt = 0 ;
    for( int j = 0 ; j < 4 ; j++ )
    {
        for( int i = 0 ; i < 4 ; i++ )
        {
            if(map[ i ][ j ] == '.')
            {
                cnt++;
                break;
            }
            if((map[ i ][ j ] == 'X' ||map[ i ][ j ] == 'T') && cnty <= 1)
            {
                cntx++;
                if(cntx==4)
                {
                    printf("Case #%d: X won\n",cas);
                    return 1;
                }
                continue;
            }
            if((map[ i ][ j ] == 'O' ||map[ i ][ j ] == 'T') && cntx <= 1)
            {
                cnty++;
                if(cnty == 4)
                {
                    printf("Case #%d: O won\n",cas);
                    return 1;
                }
                continue;
            }
            break;
        }
        cntx = cnty = 0 ;
    }
    if(cnt) return 2;
    return 3;
}
bool checkX(int cas)
{
    int x=0,y=0,cnt=0;
    for(int i = 0 ; i < 4 ; i++)
    {
        if(map[i][i]=='X') x++;
        if(map[i][i]=='O') y++;
        if(map[i][i]=='.')
        {
            cnt++;
            break ;
        }
        if(map[i][i]=='T') x++,y++;
        if(x==4)
        {
            printf("Case #%d: X won\n",cas);
            return 1;
        }
        if(y==4)
        {
            printf("Case #%d: O won\n",cas);
            return 1;
        }
    }
    x=0,y=0;
    for(int i = 0 ; i < 4 ; i++)
    {
        if(map[i][3-i]=='X') x++;
        if(map[i][3-i]=='O') y++;
        if(map[i][3-i]=='.')
        {
            cnt++;
            break ;
        }
        if(map[i][3-i]=='T') x++,y++;
        if(x==4)
        {
            printf("Case #%d: X won\n",cas);
            return 1;
        }
        if(y==4)
        {
            printf("Case #%d: O won\n",cas);
            return 1;
        }
    }
    if(cnt||tem==2||tem2==2)
    {
        printf("Case #%d: Game has not completed\n",cas);
    }
    else
    {
        printf("Case #%d: Draw\n",cas);
    }
    return 0;
}
int main()
{
 //   freopen("A-small-attempt7.in","r",stdin);

   //freopen("out.txt","w",stdout);
   // freopen("in.txt","r",stdin);
    int t ,cnt = 0;
    scanf("%d", &t );
    const int tt=t;
    while( cnt!=tt )
    {
        cnt++;
        for( int i = 0 ; i < 4 ; i++ )
            scanf("%s" , map[ i ] ) ;
        //getchar();
        tem=checkrow(cnt);
        if(tem == 1) ;
        else
        {
            tem2 = checkcul(cnt);
            if(tem2 == 1) ;
            else
            {
                checkX(cnt);
            }
        }
    }
    return 0;
}

