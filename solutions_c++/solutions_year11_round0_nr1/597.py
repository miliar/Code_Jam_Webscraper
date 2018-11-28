#include <stdio.h>
#include <string.h>

const int MAXN = 128;

int which[MAXN];
int button[MAXN];

inline int abs(int n)
{
    return n > 0 ? n : -n;
}

int main(int argc, char *argv[])
{
    int tc;
    scanf("%d", &tc);
    for (int i = 1; i <= tc; ++i)
    {
        int n;
        scanf("%d", &n);
        for (int j = 0; j < n; ++j)
        {
            char robot[2];
            scanf("%s%d", robot, &button[j]);
            if (robot[0] == 'B')
            {
                which[j] = 1;
            }
            else
            {
                which[j] = 0;
            }
            button[j] -= 1;
        }
        int pos[2] = {0, 0};
        int time = 0;
        int avail[2] = {0, 0};
        for (int j = 0; j < n; ++j)
        {
            int robot = which[j];
            int need = abs(button[j] - pos[robot]);
            if (need <= avail[robot])
            {
                time += 1;
                avail[robot ^ 1] += 1;
            }
            else
            {
                time += need - avail[robot] + 1;
                avail[robot ^ 1] += need - avail[robot] + 1;
            }
            avail[robot] = 0;
            pos[robot] = button[j];
        }
        printf("Case #%d: %d\n", i, time);
    }
    return 0;
}
