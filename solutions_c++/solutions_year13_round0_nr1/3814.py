#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool has_empty(const string s[])
{
    int i, j;

    for(i=0;i<4;i++) {
        for(j=0;j<4;j++) {
            if (s[i][j] == '.') {
                return true;
            }
        }
    }
    return false;
}

bool win(const string s[], char c)
{
    int i, j, cnt;

    // hor
    for(i=0;i<4;i++) {
        cnt = 0;
        for(j=0;j<4;j++) {
            if ((s[i][j] == c) || (s[i][j] == 'T')) {
                cnt++;
            }
        }
        if (cnt == 4) {
            return true;
        }
    }

    // ver
    for(i=0;i<4;i++) {
        cnt = 0;
        for(j=0;j<4;j++) {
            if ((s[j][i] == c) || (s[j][i] == 'T')) {
                cnt++;
            }
        }
        if (cnt == 4) {
            return true;
        }
    }

    //dia
    cnt = 0;
    for(i=0;i<4;i++) {
        if ((s[i][i] == c) || (s[i][i] == 'T')) {
            cnt++;
        }
    }
    if (cnt == 4) {
        return true;
    }
    
    //dia
    cnt = 0;
    for(i=0;i<4;i++) {
        if ((s[i][3-i] == c) || (s[i][3-i] == 'T')) {
            cnt++;
        }
    }
    if (cnt == 4) {
        return true;
    }
    
    return false;
}

int
main(void)
{
    int T;
    int N, M;
    int t, i, j;
    int height[100][100];
    int v[100], h[100];
    string vs[4];

    cin >> T;

    for(t=1;t<=T;t++) {
        for (i=0;i<4;i++) {
            cin >> vs[i];
        }

        if (win(vs, 'X')) {
            cout << "Case #" << t << ": " << "X won"  << endl;
        } else if (win(vs, 'O')) {
            cout << "Case #" << t << ": " << "O won"  << endl;
        } else if (has_empty(vs)) {
            cout << "Case #" << t << ": " << "Game has not completed"  << endl;
        } else {
            cout << "Case #" << t << ": " << "Draw"  << endl;
        }

    }
    
    return 0;
}
