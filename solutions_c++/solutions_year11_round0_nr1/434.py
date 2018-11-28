// vim:set ts=8 sw=4 et smarttab:
// Qualification Round 2011

#include <cstdio>
#include <cstdlib>
#include <cassert>

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int n;
        scanf("%d", &n);
        int position[2], move_time[2];
        position[0] = position[1] = 1;
        move_time[0] = move_time[1] = 0;
        int time = 0;
        for (int i = 0; i < n; ++i)
        {
            char temp[2];
            int robot, other_robot, button;
            scanf("%s%d", temp, &button);
            if (temp[0] == 'O')
                robot = 0, other_robot = 1;
            else if (temp[0] == 'B')
                robot = 1, other_robot = 0;
            else
                assert(0);
            int move_time_needed = abs(position[robot] - button);
            if (move_time_needed > move_time[robot])
            {
                int t = move_time_needed - move_time[robot];
                time += t;
                move_time[other_robot] += t;
            }
            position[robot] = button;
            move_time[robot] = 0;
            time += 1;
            move_time[other_robot] += 1;
        }
        printf("Case #%d: %d\n", tc, time);
    }
}
