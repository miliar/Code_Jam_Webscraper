#include <cstdio>
#include <cstring>

using namespace std;

typedef struct {
    char x;
    char o;
} Line;

// Columns 0...3, Rows 4...7, diagonals 8, 9
Line line[10];
int num_chars;

void inc(int i, int j, char c)
{
    switch (c)
    {
        case 'X':
            num_chars++;
            line[i].x++;
            line[4+j].x++;
            if (i == j)
                line[8].x++;
            else if (i + j == 3)
                line[9].x++;
            break;

        case 'O':
            num_chars++;
            line[i].o++;
            line[4+j].o++;
            if (i == j)
                line[8].o++;
            else if (i + j == 3)
                line[9].o++;
            break;
        case 'T':
            num_chars++;
            line[i].x++;
            line[4+j].x++;
            if (i == j)
                line[8].x++;
            else if (i + j == 3)
                line[9].x++;
            line[i].o++;
            line[4+j].o++;
            if (i == j)
                line[8].o++;
            else if (i + j == 3)
                line[9].o++;
            break;
        case '.':
            break;
        default:
            break;
    }
}

int main()
{
    int k, i, j, T;
    char c;
    scanf("%d", &k);
    for (T = 0; T < k; T++)
    {
        memset(line, 0, sizeof(line));
        num_chars = 0;
        scanf("%c", &c);
        for (i = 0; i < 4; i++)
        {
            for (j = 0; j < 4; j++)
            {
                scanf("%c", &c);
                if ((c == 'O') || (c == 'X') || (c == 'T'))
                    inc(i, j, c);
            }
            scanf("%c", &c);
        }

        for (i = 0; i < 10; i++)
        {
            // printf("Line %d, x = %d, o = %d\n", i, line[i].x, line[i].o);
            if (line[i].x == 4)
            {
                printf("Case #%d: X won\n", T + 1);
                break;
            }
            else if (line[i].o == 4)
            {
                printf("Case #%d: O won\n", T + 1);
                break;
            }
        }

        if ((num_chars == 16) && (i == 10))
            printf("Case #%d: Draw\n", T + 1);
        else if (i == 10)
        {
            printf("Case #%d: Game has not completed\n", T + 1);
        }

    }
    return 0;
}
