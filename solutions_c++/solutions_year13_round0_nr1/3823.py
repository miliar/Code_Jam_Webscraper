#include <cstdio>
#include <cstdlib>

#define tab table

using namespace std;

int table[4][4];
char sym;
int t,cf,sum;
bool x,o;

int colum_sum(int a)
{
    return tab[a][0]+tab[a][1]+tab[a][2]+tab[a][3];
}

int row_sum(int a)
{
    return tab[0][a]+tab[1][a]+tab[2][a]+tab[3][a];
}

int main()
{
    freopen("A-small-attempt0.in","r+",stdin);
    freopen("A-small-attempt0.out","w+",stdout);

    int count;
    scanf("%d\n",&count);
    for(int i=1;i<=count;i++)
    {
        t=0;cf=0;
        do
        {
            x=false;o=false;
            scanf("%c",&sym);
            switch(sym)
                {
                    case '.':
                        table[t/4][t%4] = 0;
                        cf++;
                        t++;
                    break;
                    case 'T':
                        table[t/4][t%4] = 500;
                        t++;
                    break;
                    case 'O':
                        table[t/4][t%4] = 10;
                        t++;
                    break;
                    case 'X':
                        table[t/4][t%4] = 60;
                        t++;
                    break;

                }
        }while(t<16);
        if(cf>12)
            {
                printf("Case #%d: Game has not completed\n",i);
                continue;
            }

        for(int g=0;g<4;g++)
            {
                if((colum_sum(g)==680)||(colum_sum(g)==240)||(row_sum(g)==680)||(row_sum(g)==240))
                    {
                        x=true;
                        break;
                    }
                if((colum_sum(g)==40)||(colum_sum(g)==530)||(row_sum(g)==40)||(row_sum(g)==530))
                    {
                        o=true;
                        break;
                    }
            }
        if((x)||(tab[0][0]+tab[1][1]+tab[2][2]+tab[3][3]==680)||(tab[0][0]+tab[1][1]+tab[2][2]+tab[3][3]==240)||
           (tab[0][3]+tab[1][2]+tab[2][1]+tab[3][0]==680)||(tab[0][3]+tab[1][2]+tab[2][1]+tab[3][0]==240))
        printf("Case #%d: X won\n",i);
        else
        if((o)||(tab[0][0]+tab[1][1]+tab[2][2]+tab[3][3]==40)||(tab[0][0]+tab[1][1]+tab[2][2]+tab[3][3]==530)||
           (tab[0][3]+tab[1][2]+tab[2][1]+tab[3][0]==40)||(tab[0][3]+tab[1][2]+tab[2][1]+tab[3][0]==530))
        printf("Case #%d: O won\n",i);
        else
        if(cf==0)
        printf("Case #%d: Draw\n",i);
        else
        printf("Case #%d: Game has not completed\n",i);
    }
    return 0;

}
