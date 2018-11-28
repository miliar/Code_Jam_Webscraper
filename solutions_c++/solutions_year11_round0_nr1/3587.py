#include <cstdio>
#include <cstdlib>

using namespace std;

inline int max(int a, int b)
{
    if (a > b)
        return a;
    return b;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int posRobot[2] = {1, 1};
    int id;
    int time[2] = {0, 0};
    int toGo;

    int N;
    char robotId;

    scanf("%d", &N);
    int nbTrucs;

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &nbTrucs);
        for (int j = 0; j < nbTrucs; j++)
        {
            getchar();
            scanf("%c", &robotId);

            if (robotId == 'O')
                id = 0;
            else
                id = 1;
            scanf("%d", &toGo);








            time[id] += abs(posRobot[id] - toGo);
            time[id] = max(time[id], time[(id+1)%2]) + 1;
            posRobot[id] = toGo;
        }

        printf("Case #%d: %d\n", i+1, max(time[0], time[1]));

        time[0] = 0;
        time[1] = 0;
        posRobot[0] = 1;
        posRobot[1] = 1;
    }


        return 0;
    }
