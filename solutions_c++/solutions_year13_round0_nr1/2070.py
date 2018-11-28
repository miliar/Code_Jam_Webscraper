#include <fstream>
#include <iostream>
using namespace std;

ifstream inf("Input.txt");
ofstream outf("Output.txt");

int main() {
    int T;
    inf >> T;
    for (int tc = 1; tc <= T; tc++) {
        outf << "Case #" << tc << ": ";
        string field[4];
        int game_status = 2;
        for (int i = 0; i < 4; i++) {
            inf >> field[i];
            int o_cnt = 0, x_cnt = 0,
                p_cnt = 0, t_cnt = 0;
            for (int j = 0; j < 4; j++)
                if (field[i][j] == 'X') ++x_cnt;
                else if (field[i][j] == 'O') ++o_cnt;
                else if (field[i][j] == 'T') ++t_cnt;
                else ++p_cnt;
            if (game_status >= 2) {
                if (o_cnt + t_cnt == 4) game_status = 0;
                else if (x_cnt + t_cnt == 4) game_status = 1;
                else if (p_cnt > 0) game_status = 3;
            }
        }
        for (int i = 0; i < 4; i++) {
            int o_cnt = 0, x_cnt = 0,
                p_cnt = 0, t_cnt = 0;
            for (int j = 0; j < 4; j++)
                if (field[j][i] == 'X') ++x_cnt;
                else if (field[j][i] == 'O') ++o_cnt;
                else if (field[j][i] == 'T') ++t_cnt;
                else ++p_cnt;
            if (game_status >= 2) {
                if (o_cnt + t_cnt == 4) game_status = 0;
                else if (x_cnt + t_cnt == 4) game_status = 1;
                else if (p_cnt > 0) game_status = 3;
            }
        }
            int o_cnt = 0, x_cnt = 0,
                p_cnt = 0, t_cnt = 0;
            for (int j = 0; j < 4; j++)
                if (field[j][j] == 'X') ++x_cnt;
                else if (field[j][j] == 'O') ++o_cnt;
                else if (field[j][j] == 'T') ++t_cnt;
                else ++p_cnt;
            if (game_status >= 2) {
                if (o_cnt + t_cnt == 4) game_status = 0;
                else if (x_cnt + t_cnt == 4) game_status = 1;
                else if (p_cnt > 0) game_status = 3;
            }
                o_cnt = 0; x_cnt = 0,
                p_cnt = 0; t_cnt = 0;
            for (int j = 0; j < 4; j++)
                if (field[3-j][j] == 'X') ++x_cnt;
                else if (field[3-j][j] == 'O') ++o_cnt;
                else if (field[3-j][j] == 'T') ++t_cnt;
                else ++p_cnt;
            if (game_status >= 2) {
                if (o_cnt + t_cnt == 4) game_status = 0;
                else if (x_cnt + t_cnt == 4) game_status = 1;
                else if (p_cnt > 0) game_status = 3;
            }
        if (game_status == 0) outf << "O won";
        else if (game_status == 1) outf << "X won";
        else if (game_status == 2) outf << "Draw";
        else outf << "Game has not completed";
        outf.put('\n');
    }
}
