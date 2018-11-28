#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
int cal(int caseN)
{
    int rows, columns;
    cin >> rows;
    cin >> columns;
    char array[rows + 1][columns + 1];
    for (int i = 0; i < rows; i++)
    {
        char buffer[columns + 100];
        scanf("%s", buffer);
        buffer[columns] = 0;
        memcpy(array[i], buffer, columns);
    }
    memset(array[rows], 0, sizeof(array[0]));

    bool impossible = false;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
        {
            if (array[i][j] == '#')
            {
                if (array[i][j + 1] == '#' && array[i + 1][j] == '#'
                    && array[i + 1][j + 1] == '#')
                {
                    array[i][j] = '/';
                    array[i][j + 1] = '\\';
                    array[i + 1][j] = '\\';
                    array[i + 1][j + 1] = '/';
                }
                else
                {
                    impossible = true;
                    break;
                }
            }
        }

    printf("Case #%d:\n", caseN);
    if (impossible)
    {
        printf("Impossible\n");
    }
    else
    {
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < columns; j++)
                printf("%c", array[i][j]);
            printf("\n");
        }
    }
    return 0;
}

int main()
{
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++)
    {
        cal(i);
    }
}
