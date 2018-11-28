#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int moves[100][2];

int max(int a, int b) {
    return a > b ? a : b;
}

int main(void) {
    int nC;

    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        int nMoves;
        scanf("%d", &nMoves);
        for (int i = 0; i < nMoves; ++i) {
            char robot;
            scanf(" %c %d\n", &robot, &moves[i][1]);
            moves[i][0] = robot == 'B' ? 0 : 1;
        }
        int pos[2][2];  // pos[0] is blue robot, pos[1] is orange robot
                        // [0] is position, [1] is time got there
        pos[0][0] = pos[1][0] = 1;
        pos[0][1] = pos[1][1] = 0;

        for (int i = 0; i < nMoves; ++i) {
            int robot = moves[i][0];
            int target_pos = moves[i][1];
            int time_needed = abs(pos[robot][0] - target_pos) + 1;

            pos[robot][0] = target_pos;
            pos[robot][1] += time_needed;
            if (pos[robot][1] <= pos[1 - robot][1])
                pos[robot][1] = pos[1 - robot][1] + 1;
            /*
            printf("Move %d completed at %d (%d)\n", i + 1, pos[robot][1],
                   time_needed);
            */
        }

        printf("Case #%d: %d\n", cC + 1, max(pos[0][1], pos[1][1]));
    }
}
