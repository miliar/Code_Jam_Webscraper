#include <cstdio>

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T, X, O, op, chance;
    bool completed;
    char a[5][5];
    
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        for (int i = 0; i < 4; ++i) scanf("%s", a[i]);
        completed = true;
        X = O = 0;
        
        for (int i = 0; i < 4; ++i)
        {
            op = 0;
            if (a[i][op] == 'T') ++op;
            if (a[i][op] == 'X') chance = 0;
            else if (a[i][op] == 'O') chance = 1;
            else
            {
                completed = false;
                chance = -1;
            }
            
            for (int j = op + 1; j < 4; ++j)
                if (a[i][j] != a[i][op] && a[i][j] != 'T') chance = -1;
            if (chance == 0) X |= 1;
            else if (chance == 1) O |= 1;
            
            op = 0;
            if (a[op][i] == 'T') ++op;
            if (a[op][i] == 'X') chance = 0;
            else if (a[op][i] == 'O') chance = 1;
            else continue;
            
            for (int j = op + 1; j < 4; ++j)
                if (a[j][i] != a[op][i] && a[j][i] != 'T') chance = -1;
            if (chance == 0) X |= 1;
            else if (chance == 1) O |= 1;
        }
        
        op = 0;
        if (a[op][op] == 'T') ++op;
        if (a[op][op] == 'X') chance = 0;
        else if (a[op][op] == 'O') chance = 1;
        else chance = -1;
        
        for (int i = op + 1; i < 4; ++i)
            if (a[i][i] != a[op][op] && a[i][i] != 'T') chance = -1;
        if (chance == 0) X |= 1;
        else if (chance == 1) O |= 1;
        
        op = 0;
        if (a[op][3 - op] == 'T') ++op;
        if (a[op][3 - op] == 'X') chance = 0;
        else if (a[op][3 - op] == 'O') chance = 1;
        else chance = -1;
        
        for (int i = op + 1; i < 4; ++i)
            if (a[i][3 - i] != a[op][3 - op] && a[i][3 - i] != 'T') chance = -1;
        if (chance == 0) X |= 1;
        else if (chance == 1) O |= 1;
        
        printf("Case #%d: ", cas);
        if (X) printf("X won\n");
        else if (O) printf("O won\n");
        else if (completed) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
