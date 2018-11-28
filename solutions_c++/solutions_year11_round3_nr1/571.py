#include <iostream>
#include <cstdio>

using namespace std;


char map[100][100];
int nbLin, nbCol, nbTest;



/**void initMap(void)
{
    for (int lin = 0; lin <= nbLin+1; lin++)
    {
        map[lin][0] = '.';
        map[lin][nbCol+1] = '.';
    }

    for (int col = 0; col <= nbCol+1; col++)
    {
        map[0][col] = '.';
        map[nbLin+1] = '.';
    }
}**/












bool apply(int col, int lin)
{
    if (col <= nbCol-2 && lin <= nbLin-2 && map[lin][col] == '#' && map[lin][col+1] == '#' && map[lin+1][col] == '#' && map[lin+1][col+1] == '#')
    {
        map[lin][col] = '/';
        map[lin][col+1] = '\\';
        map[lin+1][col] = '\\';
        map[lin+1][col+1] = '/';

        return true;
    }


    else if (map[lin][col] == '#')
        return false;

    else
        return true;
}




int main()
{
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);


    scanf("%d", &nbTest);
    bool continuer;


    for (int test = 1; test <= nbTest; test++)
    {
        continuer = true;
        scanf("%d %d", &nbLin, &nbCol);
        getchar();
        for (int lin = 0; lin < nbLin; lin++)
        {
            scanf("%s", map[lin]);
            getchar();
        }


        //initMap();
        for (int col = 0; col < nbCol && continuer; col++)
        {
            for (int lin = 0; lin < nbLin && continuer; lin++)
            {
                continuer = apply(col, lin);

            }
        }


        printf("Case #%d:\n", test);
        if (!continuer)
            printf("Impossible\n");
        else
        {
            for (int lin = 0; lin < nbLin; lin++)
            {
                for (int col = 0; col < nbCol; col++)
                    putchar(map[lin][col]);
                putchar('\n');
            }
        }





    }

    return 0;
}
