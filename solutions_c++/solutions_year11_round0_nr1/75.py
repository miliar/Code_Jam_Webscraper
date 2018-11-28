#include <cstdio>
#include <cstdlib>
#include <vector>

#define BLUE 0
#define ORANGE 1

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        scanf("%d", &N);
        vector<int> robots(N);
        vector<int> buttons(N);
        for (int i = 0; i < N; ++i)
        {
            char ch;
            scanf(" %c%d", &ch, &buttons[i]);
            if (ch == 'B')
                robots[i] = BLUE;
            else
                robots[i] = ORANGE;
        }
        vector<int> goals[2];
        for (int robot = 0; robot < 2; ++robot)
            goals[robot].assign(N, 0);
        vector<int> goal(2, 1);
        for (int i = N - 1; i >= 0; --i)
        {
            goal[robots[i]] = buttons[i];
            for (int robot = 0; robot < 2; ++robot)
                goals[robot][i] = goal[robot];
        }
        vector<int> pos(2, 1);
        int time = 0;
        for (int i = 0; i < N; ++i)
        {
            int robot = robots[i];
            int consumed = abs(buttons[i] - pos[robot]) + 1;
            pos[robot] = buttons[i];
            if (abs(goals[robot ^ 1][i] - pos[robot ^ 1]) <= consumed)
                pos[robot ^ 1] = goals[robot ^ 1][i];
            else if (goals[robot ^ 1][i] >= pos[robot ^ 1])
                pos[robot ^ 1] += consumed;
            else
                pos[robot ^ 1] -= consumed;
            time += consumed;
        }
        printf("Case #%d: %d\n", testcase, time);
    }
    return 0;
}
