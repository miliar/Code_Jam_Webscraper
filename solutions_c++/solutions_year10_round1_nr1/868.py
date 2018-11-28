#include <iostream>
#include <vector>
#include <string>
#include <stack>

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for (int i = a; i < b; i++)

using namespace std;

void rotate (vector<vector<char> > & board, int n);
bool check (vector<vector<char> > board, char t, int k);

int main() {
    int t, n, k;
    vector<vector<char> > board;
    bool red, blue;
    string ans;

    cin >> t;
    REP(z,t) {
        cin >> n >> k;

        board.clear(); board.resize(n);
        REP(i,n) {
            board[i].resize(n);
            REP(j,n) cin >> board[i][j];
        }

        rotate (board, n);

        red = false;
        blue = false;
        red = check (board, 'R', k);
        blue = check (board, 'B', k);

        if (red && blue) ans = "Both";
        else if (red) ans = "Red";
        else if (blue) ans = "Blue";
        else ans = "Neither";
        cout << "Case #" << z+1 << ": " << ans << endl;
    }

    return 0;
}

void rotate (vector<vector<char> > &board, int n) {
    char t;
    stack<char> cols;
    int ind;

    REP(i,n) {
        REP(j,n) {
            if (board[i][j] == '.') continue;
            else cols.push (board[i][j]);
            board[i][j] = '.';
        }
        ind = n-1;
        while (!cols.empty()) {
            board[i][ind] = cols.top();
            cols.pop();
            ind--;
        }
    }
}

bool check (vector<vector<char> > board, char t, int k) {
    bool on;
    int kcount;
    string st1, st2;
    int n = board.size();

    // Horizontal
    REP(i,n) {
        kcount = 0;
        REP(j,n) {
            if (board[i][j] == t) {
                on = true;
                kcount++;

                if (kcount == k)
                    return true;
            }
            else {
                on = false;
                kcount = 0;
            }
        }
    }

    // Vertical
    REP(j,n) {
        kcount = 0;
        REP(i,n) {
            if (board[i][j] == t) {
                on = true;
                kcount++;

                if (kcount == k)
                    return true;
            }
            else {
                on = false;
                kcount = 0;
            }
        }
    }

    // Leading Diagonal
    int z, sz;
    REP(i,n) {
        st1 = ""; st2 = "";
        FOR(j,i,n) {
            z = j - i;
            st1 += board[j][z];
            st2 += board[z][j];
        }
        kcount = 0; sz = st1.length();
        REP(j,sz) {
            if (st1[j] == t) {
                kcount++;
                if (kcount == k)
                    return true;
            }
            else {
                kcount = 0;
            }
        }

        kcount = 0; sz = st2.length();
        REP(j,sz) {
            if (st2[j] == t) {
                kcount++;
                if (kcount == k)
                    return true;
            }
            else {
                kcount = 0;
            }
        }
    }

    // Other Diagonal
    int j;
    REP(i,n) {
        st1 = ""; st2 = "";
        for (j = i, z = 0; j >= 0 && z <= i; j--, z++) {
            st1 += board[j][z];
            st2 += board[n-z-1][n-j-1];
        }

        kcount = 0; sz = st1.length();
        REP(j,sz) {
            if (st1[j] == t) {
                kcount++;
                if (kcount == k)
                    return true;
            }
            else {
                kcount = 0;
            }
        }

        kcount = 0; sz = st2.length();
        REP(j,sz) {
            if (st2[j] == t) {
                kcount++;
                if (kcount == k)
                    return true;
            }
            else {
                kcount = 0;
            }
        }
    }

    return false;
}
