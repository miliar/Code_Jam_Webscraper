#include <cstdio>
#include <vector>
#include <string>
using namespace std;

struct game
{
    int tr, tc;
    vector <string> board;

    bool is_drawn()
    {
        int cnt = 0;

        for (int i=0; i<4; ++i)
            for (int j=0; j<4; ++j)
                if (board[i][j] != '0')
                    cnt++;

        if (cnt == 16)
            return true;
    }

    bool is_won(int cur)
    {
        int outcome = -1;
        // cur: 2 - x, 1 - o
        // returns 2 - x won, 1 - o won

        // row check
        board[tr][tc] = cur + '0';

        //for (int i=0; i<4; ++i)
        //    printf("%s\n", board[i].c_str());

        for (int i=0; i<4; ++i)
        {
            int cnt = 0;
            for (int j=0; j<4; ++j)
                if (board[i][j] == cur + '0')
                    cnt++;
            if (cnt == 4)
                return true;
        }

        // col check

        for (int i=0; i<4; ++i)
        {
            int cnt = 0;
            for (int j=0; j<4; ++j)
                if (board[j][i] == cur + '0')
                    cnt++;
            if (cnt == 4)
                return true;
        }

        // west-east diagonal check
        int cnt = 0;
        for (int i=0; i<4; ++i)
            if (board[i][i] == cur + '0')
                    cnt++;
        if (cnt == 4)
            return true;

        // east-west diagonal check
        cnt = 0;
        for (int i=0; i<4; ++i)
            if (board[i][3-i] == cur + '0')
                    cnt++;
        if (cnt == 4)
            return true;

        return false;
    }

    game(vector <string> S)
    {
        for (int i=0; i<4; ++i)
        {
            for (int j=0; j<4; ++j)
            {
                if (S[i][j] == 'T')
                {
                    tr = i, tc = j, S[i][j] = '.';
                }

                if (S[i][j] == 'X')
                {
                    S[i][j] = '2';
                }
                else if (S[i][j] == 'O')
                {
                    S[i][j] = '1';
                }
                else
                {
                    S[i][j] = '0';
                }
            }
        }
        board = S;
    }


};

int main()
{
    freopen("a.in", "r", stdin);
    freopen("asmall.out", "w", stdout);

    int tests;

    scanf("%d", &tests);
    for (int case_no = 1; case_no <= tests; ++case_no)
    {
        printf("Case #%d: ", case_no);

        char game_row[8];
        vector <string> game_state;

        for (int i=0; i<4; ++i)
        {
            scanf("%s", game_row);
            game_state.push_back(game_row);
        }

        game cur_game(game_state);

        bool ok = false;

        for (int i=2; i>=1; --i)
        {
            if (cur_game.is_won(i) == true)
            {
                printf("%c won\n", "XO"[2-i]);
                ok = true;
            }
        }

        if (!ok)
        {
            if (cur_game.is_drawn())
                printf("Draw\n");
            else
                printf("Game has not completed\n");
        }
    }
}
