#include <iostream>
#include <map>
#include <string>

const int L = 4;

std::string M[L];

void test(int x, int y, int dx, int dy, char& V) {
    std::map<char, int> cnt; 
    cnt['X'] = cnt['O'] = cnt['.'] = cnt['T'] = 0;
    for (int i = 0; i < L; i ++)
        cnt[M[x + dx * i][y + dy * i]] ++;
    if (cnt['X'] + cnt['T'] == L) {
        V = 'X';
    } else if (cnt['O'] + cnt['T'] == L) {
        V = 'O';
    }
}

int main() {
    int _;
    std::cin >> _;
    for (int nc = 1; nc <= _; nc ++) {
        bool finished = true;
        for (int i = 0; i < L; i ++) {
            std::cin >> M[i];
            for (int j = 0; j < L; j ++)
                if (M[i][j] == '.') finished = false;
        }
        char V = ' ';
        for (int i = 0; i < L; i ++) {
            test(0, i, 1, 0, V);
            test(i, 0, 0, 1, V);
        }
        test(0, 0, 1, 1, V);
        test(0, L-1, 1, -1, V);
        std::string ans;
        if (V != ' ') {
            ans = "  won";
            ans[0] = V;
        } else if (finished) {
            ans = "Draw";
        } else {
            ans = "Game has not completed";
        }
        std::cout << "Case #" << nc << ": " << ans << std::endl;
    }
}
