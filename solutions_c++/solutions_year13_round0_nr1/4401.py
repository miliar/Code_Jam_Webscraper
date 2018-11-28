#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x) * (x))
using namespace std;

int task, n, full;
string st[5];

int cal(char ch)
{
    for (int i = 0; i <= 3; i++)
    {
        //cout << st[i] << endl;
        int x = 1, y = 1;
        for (int j = 0; j <= 3; j++)
        {
            if (st[i][j] != 'T' && st[i][j] != ch) x = 0;
            if (st[j][i] != 'T' && st[j][i] != ch) y = 0;
            if (st[i][j] == '.') full = 0;
        }
        if (x || y) return 1;
    }
    int t1 = 1, t2 = 1;
    for (int i = 0; i <= 3; i++)
    {
        if (st[i][i] != 'T' && st[i][i] != ch) t1 = 0;
        if (st[i][3 - i] != 'T' && st[i][3 - i] != ch) t2 = 0;
    }
    return t1 || t2;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> task;
    for (int ta = 1; ta <= task; ta++)
    {
        full = 1;
        for (int i = 0; i < 4; i++)
            cin >> st[i];
        printf("Case #%d: ", ta);
        if (cal('X')) printf("X won\n");
        else if (cal('O')) printf("O won\n");
        else if (full) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
