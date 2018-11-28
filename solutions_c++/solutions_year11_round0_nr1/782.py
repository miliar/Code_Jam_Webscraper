#include <stdio.h>

typedef struct _robot_t {
    char c;
    int d;
} robot_t;

robot_t robot[200];

int abs(int a)
{
    if (a > 0) return a;
    return -a;
}

int main()
{
    int ca;
    scanf("%d", &ca);
    for (int tc = 1; tc <= ca; tc++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            char c;
            int d;
            scanf(" %c %d", &robot[i].c, &robot[i].d);
        }

        int O = 1;
        int per_O = 0;

        int B = 1;
        int per_B = 0;
        int res = 0;
        for (int i = 0; i < n; i++)
        {
            int t;
            if (robot[i].c == 'B')
            {
                t = (abs(robot[i].d - B) - per_O);
                if (t < 0) t = 0;
                t ++;

                per_B += t;
                per_O = 0;
                B = robot[i].d;
            }
            else
            {
                t = (abs(robot[i].d - O) - per_B);
                if (t < 0) t = 0;
                t ++;

                per_O += t;
                per_B = 0;
                O = robot[i].d;
            }
            res += t;
        }
        printf("Case #%d: %d\n", tc, res);
    }
    return 0;
}

