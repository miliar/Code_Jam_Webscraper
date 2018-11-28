#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

typedef vector<int> vi;

char a[4][4];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    string tmp;
    int t;
    cin >> t;
    for (int cnt = 1; cnt <= t; ++cnt)
    {
        bool was_point = false;
        for (int i = 0; i < 4; ++i)
        {
            cin >> tmp;
            for (int j = 0; j < 4; ++j)
            {
                a[i][j] = tmp[j];
                if (tmp[j] == '.')
                    was_point = true;
            }
        }

        bool x_win = false;
        bool o_win = false;
        for (int i = 0; i < 4; ++i)
        {
            bool flag_o = true;
            bool flag_x = true;
            for (int j = 0; j < 4; ++j)
            {
                if (a[i][j] == '.' || a[i][j] == 'X')
                    flag_o = false;
                if (a[i][j] == '.' || a[i][j] == 'O')
                    flag_x = false;
            }
            x_win |= flag_x;
            o_win |= flag_o;
        }

        for (int j = 0; j < 4; ++j)
        {
            bool flag_o = true;
            bool flag_x = true;
            for (int i = 0; i < 4; ++i)
            {
                if (a[i][j] == '.' || a[i][j] == 'X')
                    flag_o = false;
                if (a[i][j] == '.' || a[i][j] == 'O')
                    flag_x = false;
            }
            x_win |= flag_x;
            o_win |= flag_o;
        }

        bool flag_o = true;
        bool flag_x = true;
        for (int i = 0; i < 4; ++i)
        {
            if (a[i][i] == '.' || a[i][i] == 'X')
                flag_o = false;
            if (a[i][i] == '.' || a[i][i] == 'O')
                flag_x = false;
        }
        x_win |= flag_x;
        o_win |= flag_o;

        flag_o = true;
        flag_x = true;
        for (int i = 0; i < 4; ++i)
        {
            if (a[i][3 - i] == '.' || a[i][3 - i] == 'X')
                flag_o = false;
            if (a[i][3 - i] == '.' || a[i][3 - i] == 'O')
                flag_x = false;
        }
        x_win |= flag_x;
        o_win |= flag_o;

        printf("Case #%d: ", cnt);
        if (x_win)
        {
            printf("X won\n");
            continue;
        }
        if (o_win)
        {
            printf("O won\n");
            continue;
        }
        if (was_point)
        {
            printf("Game has not completed\n");
        }
        else
        {
            printf("Draw\n");
        }
    }
    return 0;
}