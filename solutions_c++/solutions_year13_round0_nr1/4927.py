#include <iostream>
#include <string>

using namespace std;

bool _test_for(string t[4], char c) {
    string r = "";
    for(int i=0;i<4;i++) r+=c;
    for(int i=0;i<4;i++) if(t[i] == r) return true;
    for(int i=0;i<4;i++) {
        string p = "";
        for(int j=0;j<4;j++) p+=t[j][i];
        if(p == r) return true;
    }
    string a="", b="";
    for(int i=0;i<4;i++) {
        a+=t[i][i];
        b+=t[i][3-i];
    }
    if(a == r || b == r) return true;
    return false;
}

bool is_x_won(string t[4]) {
    return _test_for(t, 'X');
}

bool is_o_won(string t[4]) {
    return _test_for(t, 'O');
}

bool game_complete(string t[4]) {
    for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(t[i][j] == '.') return false;
    return true;
}

string do_one() {
    string a[4];
    cin >> a[0] >> a[1] >> a[2] >> a[3];
    int tr=-1, tc;
    for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(a[i][j] == 'T') { tr = i; tc = j; }
    if(tr != -1) a[tr][tc] = 'X';
    if(is_x_won(a)) return "X won";
    if(tr != -1) a[tr][tc] = 'O';
    if(is_o_won(a)) return "O won";
    if(tr != -1) a[tr][tc] = 'T';
    if(game_complete(a)) return "Draw";
    return "Game has not completed";
}

int main() {
    int T;
    cin >> T;
    for(int i=1;i<=T;i++) cout << "Case #" << i << ": " << do_one() << endl;
    return 0;
}

