#include <iostream>
#include <vector>
#include <string>
using namespace std;

int iswin(vector<string> board, int p, int q, int dp, int dq, char col)
{
//    cout << p << ' ' << q << endl;
    char color = board[p][q];
    return color == '.' || color != col ? 0 : 1 + iswin(board, p+dp, q+dq, dp, dq, col);
}

int main()
{
    int t;
    cin >> t;
    for(int cnt=1;cnt<=t;cnt++) {
        int n, k;
        cin >> n >> k;
        vector<string> board(n, string(n, '.'));
        for(int i=0;i<n;i++) {
            cin >> board[i];
        }
        vector<string> board_r(n, string(n, '.'));
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                board_r[j][n-1-i] = board[i][j];
            }
        }
        for(int j=0;j<n;j++) {
            vector<char> vc;
            for(int i=0;i<n;i++) {
                if(board_r[i][j] != '.') {
                    vc.push_back(board_r[i][j]);
                }
            }
            for(int i=0;i<n-vc.size();i++) {
                board_r[i][j] = '.';
            }
            for(int i=0;i<vc.size();i++) {
                board_r[i+n-vc.size()][j] = vc[i];
            }
        }
        vector<string> board_n(n+2, string(n+2, '.'));
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                board_n[i+1][j+1] = board_r[i][j];
            }
        }
        bool b = false, r = false;
        for(int i=1;i<=n;i++) {
            for(int j=1;j<=n;j++) {
                if(iswin(board_n, i, j, 1, 0, board_n[i][j]) >= k ||
                   iswin(board_n, i, j, 0, 1, board_n[i][j]) >= k ||
                   iswin(board_n, i, j, 1, 1, board_n[i][j]) >= k ||
                   iswin(board_n, i, j, 1, -1, board_n[i][j])>= k ) {
                    if(board_n[i][j] == 'R')
                        r = true;
                    if(board_n[i][j] == 'B')
                        b = true;
                }
            }
        }
        cout << "Case #" << cnt << ": ";
        if(b && r)
            cout << "Both";
        else if(b && !r)
            cout << "Blue";
        else if(!b && r)
            cout << "Red";
        else if(!b && !r)
            cout << "Neither";
        else
            throw 1;
        cout << endl;
    }

    return 0;
}
