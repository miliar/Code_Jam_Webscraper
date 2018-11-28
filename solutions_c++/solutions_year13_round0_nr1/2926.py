#include <string>
#include <iostream>
using namespace std;

#define for_(i, a, b) for (int i = a; i < b; ++i)


int main(void) {
    int t;
    cin >> t;

    for_(T, 1, t+1) {
        string board[4];
        for_(i, 0, 4)
            cin >> board[i];

        bool completed = true;
        char winner = (char) 0;

        for_(i, 0, 4) for_(j, 0, 4) {
            char at = board[i][j];
            if (at == 'T' || at == '.') {
                completed &= (at != '.');
                continue;
            }

            for_(di, -1, 2) for_(dj, -1, 2) {
                if (!di & !dj) continue;

                int count = 0;
                for (int ni = i, nj = j;
                     count < 4 && ni >= 0 && ni < 4 && nj >= 0 && nj < 4;
                     ni += di, nj += dj, ++count) {

                    char n_at = board[ni][nj];
                    if (n_at != at && n_at != 'T')
                        break;
                }

                if (count == 4) {
                    winner = at;
                    goto out;
                }
            }
        }

        out:
        cout << "Case #" << T << ": ";
        if (winner)
            cout << winner << " won";
        else if (completed)
            cout << "Draw";
        else
            cout << "Game has not completed";
        cout << endl;
    }
}
