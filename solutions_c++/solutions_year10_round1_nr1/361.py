#include<iostream>
#include<string>

using namespace std;

int main() {
    int T, n, k;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> n >> k;

        string s[50];
        for(int i = 0; i < n; i++) {
            cin >> s[i];
            string t = "";
            for(int p = n - 1, q = n - 1; p >= 0; p--) {
                if(s[i][p] != '.') {
                    if(p != q) {
                        s[i][q] = s[i][p];
                        s[i][p] = '.';
                    }
                    q--;
                }
            }
        }
        /*
        cout << endl;
        for(int i = 0; i < n; i++) cout << s[i] << endl;
        */

        bool R = false, B = false;
        static int a[50][50][4];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(s[i][j] == '.') a[i][j][0] = a[i][j][1] = a[i][j][2] = a[i][j][3] = 0;
                else {
                    a[i][j][0] = a[i][j][1] = a[i][j][2] = a[i][j][3] = 1;
                    if(j > 0 and s[i][j] == s[i][j-1])  a[i][j][0] = a[i][j-1][0] + 1;
                    if(i > 0 and j > 0 and s[i][j] == s[i-1][j-1]) a[i][j][1] = a[i-1][j-1][1] + 1;
                    if(i > 0 and s[i][j] == s[i-1][j]) a[i][j][2] = a[i-1][j][2] + 1;
                    if(i > 0 and j < n - 1 and s[i][j] == s[i-1][j+1]) a[i][j][3] = a[i-1][j+1][3] + 1;
                }
                if(a[i][j][0] >= k or a[i][j][1] >= k or a[i][j][2] >= k or a[i][j][3] >= k) {
                    ((s[i][j] == 'R')?R:B) = true;
                }
            }
        }

        cout << "Case #" << t << ": ";
        if(R and B) cout << "Both\n";
        else if(R) cout << "Red\n";
        else if(B) cout << "Blue\n";
        else cout << "Neither\n";
    }
}

