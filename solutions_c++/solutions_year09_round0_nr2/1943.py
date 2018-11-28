#include <cstdio>

const int max_dim = 100;

int alt[max_dim][max_dim];
char let[max_dim][max_dim];
int H, W;
char letter;

int dir[4][2] = {{ -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 }};

inline bool is_valid(int y, int x)
{
    return y >= 0 && x >= 0 && y < H && x < W;
}

int sink_letter(int y, int x)
{
    if (let[y][x])
        return let[y][x];
    int best_ny = y;
    int best_nx = x;
    int best_a = alt[y][x];
    for (int d = 0 ; d < 4 ; d++)
        {
            int ny = y + dir[d][0];
            int nx = x + dir[d][1];
            if (!is_valid(ny, nx))
                continue;
            int a = alt[ny][nx];
            if (a >= best_a)
                continue;
            best_ny = ny;
            best_nx = nx;
            best_a = a;
        }
    if (best_ny == y && best_nx == x)
        return let[y][x] = letter++;

    return let[y][x] = sink_letter(best_ny, best_nx);
}

int main(void)
{
    int T;

    scanf("%d", &T);

    for (int t = 1 ; t <= T ; t++)
        {
            scanf("%d%d", &H, &W);
            for (int y = 0 ; y < H ; y++)
                for (int x = 0 ; x < W ; x++)
                    {
                        scanf("%d", &alt[y][x]);
                        let[y][x] = 0;
                    }
            printf("Case #%d:\n", t);
            letter = 'a';
            for (int y = 0 ; y < H ; y++)
                for (int x = 0 ; x < W ; x++)
                    printf("%c%c", sink_letter(y, x), x == (W - 1) ? '\n' : ' ');
        }

    return 0;
}
