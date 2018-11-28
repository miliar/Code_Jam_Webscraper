#include <iostream>
#include <stdio.h>

using namespace std;

char s[10][10];

int main()
{
    int n;
    cin >> n;
    for (int _ = 1; _ <= n; ++_) {
        gets(s[0]);
        gets(s[0]);
        gets(s[1]);
        gets(s[2]);
        gets(s[3]);
        // puts(s[0]);
        // puts(s[1]);
        // puts(s[2]);
        // puts(s[3]);

        bool draw = true;
        bool winX = false;
        bool winO = false;

        for (int i = 0; i < 4; ++i) {
            bool winx = true;
            bool wino = true;
            for (int j = 0; j < 4; ++j)
                switch (s[i][j]) {
                case '.':
                    winx = false;
                    wino = false;
                    draw = false;
                    break;
                case 'O':
                    winx = false;
                    break;
                case 'X':
                    wino = false;
                    break;
                }
            winX |= winx;
            winO |= wino;
            // printf("X: %d, O: %d\n", winX, winO);
        }

        for (int j = 0; j < 4; ++j) {
            bool winx = true;
            bool wino = true;
            for (int i = 0; i < 4; ++i)
                switch (s[i][j]) {
                case '.':
                    winx = false;
                    wino = false;
                    draw = false;
                    break;
                case 'O':
                    winx = false;
                    break;
                case 'X':
                    wino = false;
                    break;
                }
            winX |= winx;
            winO |= wino;
            // printf("X: %d, O: %d\n", winX, winO);
        }

        {
            bool winx = true;
            bool wino = true;
            for (int i = 0; i < 4; ++i)
                switch (s[i][i]) {
                case '.':
                    winx = false;
                    wino = false;
                    draw = false;
                    break;
                case 'O':
                    winx = false;
                    break;
                case 'X':
                    wino = false;
                    break;
                }
            winX |= winx;
            winO |= wino;
            // printf("X: %d, O: %d\n", winX, winO);
        }

        {
            bool winx = true;
            bool wino = true;
            for (int i = 0; i < 4; ++i)
                switch (s[i][3-i]) {
                case '.':
                    winx = false;
                    wino = false;
                    draw = false;
                    break;
                case 'O':
                    winx = false;
                    break;
                case 'X':
                    wino = false;
                    break;
                }
            winX |= winx;
            winO |= wino;
            // printf("X: %d, O: %d\n", winX, winO);
        }


        const char *str;
        if (winX)
            str = "X won";
        else if (winO)
            str = "O won";
        else if (draw)
            str = "Draw";
        else
            str = "Game has not completed";

        printf("Case #%d: %s\n", _, str);
    }
}
