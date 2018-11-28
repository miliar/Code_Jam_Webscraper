#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

inline int checkV(const string& s)
{
    int O = 0, X = 0;
    for (int i = 0; i < 4; ++i)
    {
        switch (s[i])
        {
        case 'T' : ++O;
        case 'X' : ++X; break;
        case 'O' : ++O; break;
        }
    }
    if (X == 4)
        return 1;
    if (O == 4)
        return 2;
    return 0;
}

inline int checkH(const string s[], int h)
{
    int O = 0, X = 0;
    for (int i = 0; i < 4; ++i)
    {
        switch (s[i][h])
        {
        case 'T' : ++O;
        case 'X' : ++X; break;
        case 'O' : ++O; break;
        }
    }
    if (X == 4)
        return 1;
    if (O == 4)
        return 2;
    return 0;
}

inline int checkD(const string s[])
{
    int O = 0, X = 0;
    for (int i = 0; i < 4; ++i)
    {
        switch (s[i][i])
        {
        case 'T' : ++O;
        case 'X' : ++X; break;
        case 'O' : ++O; break;
        }
    }
    if (X == 4)
        return 1;
    if (O == 4)
        return 2;
    O = 0, X = 0;
    for (int i = 0; i < 4; ++i)
    {
        switch (s[i][3 - i])
        {
        case 'T' : ++O;
        case 'X' : ++X; break;
        case 'O' : ++O; break;
        }
    }
    if (X == 4)
        return 1;
    if (O == 4)
        return 2;
    return 0;
}

inline bool isDot(char c)
{
    return c == '.';
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n;

    scanf("%d", &n);

    string m[4];

    for (int i = 1; i <= n; ++i)
    {
        int win = 0;
        for (int j = 0; j < 4; ++j)
            cin >> m[j];
        for (int j = 0; j < 4 && !win; ++j)
            win = checkV(m[j]);
        if (win)
        {
            printf("Case #%i: %c won\n", i, win==1?'X':'O');
            continue;
        }
        for (int j = 0; j < 4 && !win; ++j)
            win = checkH(m, j);
        if (win)
        {
            printf("Case #%i: %c won\n", i, win==1?'X':'O');
            continue;
        }
        win = checkD(m);
        if (win)
        {
            printf("Case #%i: %c won\n", i, win==1?'X':'O');
            continue;
        }
        for (int j = 0; j < 4 && !win; ++j)
        {
            if (find_if(m[j].begin(), m[j].end(), isDot) != m[j].end())
                win = 1;
        }
        if (win)
            printf("Case #%i: Game has not completed\n", i);
        else
            printf("Case #%i: Draw\n", i);

    }
    
    return 0;
}