#include <cassert>
#include <cstdio>
using namespace std;

char field[4][4];
bool x, o;
void update(int sx, int sy, int dx, int dy)
{
    bool nx = true, no = true;
    for(int i = 0; i < 4; i++)
    {
        char ch = field[sx + i * dx][sy + i * dy];
        if(ch == '.') nx = no = false;
        else if(ch == 'X') no = false;
        else if(ch == 'O') nx = false;
    }
    if(nx) x = true;
    if(no) o = true;
}
int main()
{
    int T; scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++)
    {
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf(" %c", &field[i][j]);

        bool ended = true;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                if(field[i][j] == '.')
                    ended = false;

        x = false; o = false;
        update(0, 0, 1, 1);
        update(0, 3, 1, -1);
        for(int i = 0; i < 4; i++)
        {
            update(i, 0, 0, 1);
            update(0, i, 1, 0);
        }
        assert(!x || !o);

        printf("Case #%d: ", tt);
        if(x) printf("X won\n");
        else if(o) printf("O won\n");
        else if(ended) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
