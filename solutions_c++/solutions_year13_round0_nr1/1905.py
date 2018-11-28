#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <string>

using namespace std;

int check(string s[]) {
    int x, y, t;
    bool empty = false;
    for(int i = 0; i < 4; ++i) {
        x = y = t = 0;
        for(int j = 0; j < 4; ++j) {
            if(s[i][j] == 'X')
                ++x;
            else if(s[i][j] == 'O')
                ++y;
            else if(s[i][j] == 'T')
                ++t;
            else
                empty = true;
        }
        if(x + t == 4)
            return 1;
        else if(y + t == 4)
            return 2;
    }
    
    for(int i = 0; i < 4 ; ++i) {
        x = y = t = 0;
        for(int j = 0; j < 4; ++j) {
            if(s[j][i] == 'X')
                ++x;
            else if(s[j][i] == 'O')
                ++y;
            else if(s[j][i] == 'T')
                ++t;
        }
        if(x + t == 4)
            return 1;
        else if(y + t == 4)
            return 2;
    }
    
    x = y = t = 0;
    for(int i = 0; i < 4; ++i) {
        if(s[i][i] == 'X')
            ++x;
        else if(s[i][i] == 'O')
            ++y;
        else if(s[i][i] == 'T')
            ++t;
    }

    if(x + t == 4)
        return 1;
    else if(y + t == 4)
        return 2;
    
    x = y = t = 0;
    for(int i = 0; i < 4; ++i) {
        if(s[i][3 - i] == 'X')
            ++x;
        else if(s[i][3 - i] == 'O')
            ++y;
        else if(s[i][3 - i] == 'T')
            ++t;
    }
    
    if(x + t == 4)
        return 1;
    else if(y + t == 4)
        return 2;
    
    if(!empty)
        return 0;
    else
        return -1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    string s[4];
    for(int i = 0; i < T; ++i) {
        for(int i = 0; i < 4; ++i)
            cin >> s[i];
        cout << "Case #" << i + 1 << ": ";
        int res = check(s);
        if(res == 1)
            cout << "X won\n";
        else if(res == 2)
            cout << "O won\n";
        else if(res == 0)
            cout << "Draw\n";
        else
            cout << "Game has not completed\n";
    }
    
    return 0;
}

