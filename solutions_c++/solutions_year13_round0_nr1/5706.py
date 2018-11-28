#include <cstdio>
char  ma[5][5];
inline void solve(int case_id)
{
    gets(ma[1]+1);
    gets(ma[2]+1);
    gets(ma[3]+1);
    gets(ma[4]+1);
    gets(ma[0]); // empty
    bool has_empty = false;
    char winner = 0;
    /* rows */
    for (int i = 1 ; i <= 4 ; ++i)
    {
        winner = 0;
        for (int j = 1 ; j <= 4; ++j)
            if (ma[i][j] != '.' && (ma[i][j] == 'T' || ma[i][j] == winner || !winner))
            {
                if (ma[i][j] != 'T')
                    winner = ma[i][j];
            }
            else
            {
                if (ma[i][j] == '.')
                    has_empty = true;
                winner = 0;
                break;
            }
        if (winner)
        {
            printf("Case #%d: %c won\n",case_id,winner);
            return ;
        }
    }
    /* cols */
    for (int j = 1 ; j <= 4 ; ++j)
    {
        winner = 0;
        for (int i = 1 ; i <= 4; ++i)
            if (ma[i][j] != '.' && (ma[i][j] == 'T' || ma[i][j] == winner || !winner))
            {
                if (ma[i][j] != 'T')
                    winner = ma[i][j];
            }
            else
            {
                if (ma[i][j] == '.')
                    has_empty = true;
                winner = 0;
                break;
            }
        if (winner)
        {
            printf("Case #%d: %c won\n",case_id,winner);
            return ;
        }
    }
    /* cross */
    winner = 0;
    for (int i = 1; i <= 4 ; ++i)
    {
        int j = i;
        if (ma[i][j] != '.' && (ma[i][j] == 'T' || ma[i][j] == winner || !winner))
        {
            if (ma[i][j] != 'T')
                winner = ma[i][j];
        }
        else
        {
            if (ma[i][j] == '.')
                has_empty = true;
            winner = 0;
            break;
        }
    }
    if (winner)
    {
        printf("Case #%d: %c won\n",case_id,winner);
        return ;
    }

    winner = 0;
    for (int i = 1; i <= 4 ; ++i)
    {
        int j = 5 - i;
        if (ma[i][j] != '.' && (ma[i][j] == 'T' || ma[i][j] == winner || !winner))
        {
            if (ma[i][j] != 'T')
                winner = ma[i][j];
        }
        else
        {
            if (ma[i][j] == '.')
                has_empty = true;
            winner = 0;
            break;
        }
    }
    if (winner)
    {
        printf("Case #%d: %c won\n",case_id,winner);
        return ;
    }
    printf("Case #%d: %s\n",case_id,has_empty?"Game has not completed":"Draw");
}
int main()
{
#ifdef OFFLINE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // OFFLINE
    int test_cases = 0;
    scanf("%d\n",&test_cases);
    for (int i = 1 ; i <= test_cases ; ++i)
        solve(i);
    return 0;
}
