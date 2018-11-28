#include <stdio.h>

char r[4][4];

int main() {
    int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		for (int i = 0; i < 4; i++) {
            scanf("\n");
            for (int j = 0; j < 4; j++)
                scanf("%c", &r[i][j]);
		}

		char winner = '.';
		bool draw = true;
		for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (r[i][j] == '.')
                    draw = false;

        for (int i = 0; i < 4; i++) {
            int x = 0;
            int o = 0;
            for (int j = 0; j < 4; j++)
                if (r[i][j] == 'X')
                    x++;
                else if (r[i][j] == 'O')
                    o++;
                else if (r[i][j] == 'T') {
                    x++;
                    o++;
                }
            if (x == 4)
                winner = 'X';
            else if (o == 4)
                winner = 'O';
        }

        for (int i = 0; i < 4; i++) {
            int x = 0;
            int o = 0;
            for (int j = 0; j < 4; j++)
                if (r[j][i] == 'X')
                    x++;
                else if (r[j][i] == 'O')
                    o++;
                else if (r[j][i] == 'T') {
                    x++;
                    o++;
                }
            if (x == 4)
                winner = 'X';
            else if (o == 4)
                winner = 'O';
        }

        int x = 0;
        int o = 0;
        for (int i = 0; i < 4; i++) {
            x += r[i][i] == 'X';
            o += r[i][i] == 'O';
            if (r[i][i] == 'T') {
                x++;
                o++;
            }
        }
            if (x == 4)
                winner = 'X';
            else if (o == 4)
                winner = 'O';

        x = 0;
        o = 0;

        for (int i = 0; i < 4; i++) {
            x += r[i][3 - i] == 'X';
            o += r[i][3 - i] == 'O';
            if (r[i][3 - i] == 'T') {
                x++;
                o++;
            }
        }
            if (x == 4)
                winner = 'X';
            else if (o == 4)
                winner = 'O';

        printf("Case #%d: ", i);
        if (winner != '.')
            printf("%c won\n", winner);
        else if (draw)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
	}
}
