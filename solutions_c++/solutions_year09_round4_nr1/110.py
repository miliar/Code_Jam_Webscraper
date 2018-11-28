#include <iostream>
#include <vector>

using namespace std;

int rows;
vector<string> m;

int go(int cur) {
    //for(int i=0; i<m.size(); i++) cout << m[i] << endl;
    //cout <<endl;
    if (cur == m.size()) return 0;
    for(int r=cur; r<m.size(); r++) {
        bool good = true;
        for(int c=cur+1; c<m.size(); c++) if (m[r][c] != '0') good = false;

        if (good) {
            int ans = r - cur;
            for(int r1=r; r1>=cur+1; r1--) swap(m[r1], m[r1-1]);
            return ans + go(cur+1);
        }
    }

    return -1;
}

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        cin >> rows; m.resize(rows);
        for(int i=0; i<rows; i++) cin >> m[i];

        cout << "Case #" <<(c+1) << ": ";
        int ans = go(0);
        cout << ans<<endl;
    }
}
