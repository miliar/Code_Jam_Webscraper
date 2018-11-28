#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)

int main()
{
    int t;
    cin >> t;
    string str[4];
    
    rep(caseno, t) {
        bool x_won = false, o_won = false;
        cin >> str[0] >> str[1] >> str[2] >> str[3];
        
        rep(i, 4) {
            int x = 0, o = 0, t = 0;
            rep(j, 4) switch (str[i][j]) {
                case 'X': ++x; break;
                case 'O': ++o; break;
                case 'T': ++t; break;
            }
            if (x + t == 4) x_won = true;
            if (o + t == 4) o_won = true;
        }
        
        rep(i, 4) {
            int x = 0, o = 0, t = 0;
            rep(j, 4) switch (str[j][i]) {
                case 'X': ++x; break;
                case 'O': ++o; break;
                case 'T': ++t; break;
            }
            if (x + t == 4) x_won = true;
            if (o + t == 4) o_won = true;
        }
        
        int x1 = 0, x2 = 0, o1 = 0, o2 = 0, t1 = 0, t2 = 0;
        rep(i, 4) {
            switch (str[i][i]) {
                case 'X': ++x1; break;
                case 'O': ++o1; break;
                case 'T': ++t1; break;
            }
            switch (str[i][3-i]) {
                case 'X': ++x2; break;
                case 'O': ++o2; break;
                case 'T': ++t2; break;
            }
        }
        if (x1 + t1 == 4 || x2 + t2 == 4) x_won = true;
        if (o1 + t1 == 4 || o2 + t2 == 4) o_won = true;
        
        cout << "Case #" << caseno + 1 << ": ";
        if (x_won && o_won) {
            cout << "ERROR" << endl;
        } else if (x_won) {
            cout << "X won" << endl;
        } else if (o_won) {
            cout << "O won" << endl;
        } else {
            bool filled = true;
            rep(i, 4) rep(j, 4) if (str[i][j] == '.') filled = false;
            cout << (filled ? "Draw" : "Game has not completed") << endl;
        }
    }
}
