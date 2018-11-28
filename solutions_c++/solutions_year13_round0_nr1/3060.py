#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

string RES[5] = {
    "",
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};

// 0 means can not be judged yet
// 1 means "X won"
// 2 means "O won"
int check(string str)
{
    if (str.find('.') != -1) return 0;
    if (str.find('O') == -1) return 1;
    if (str.find('X') == -1) return 2;
}

string work()
{
    string map[4], str;
    int res;
    
    for (int i = 0; i < 4; ++ i)
        cin >>map[i];
    
    for (int i = 0; i < 4; ++ i)
    {
        int res = check(map[i]);
        if (res > 0) return RES[res];
    }
    
    for (int i = 0; i < 4; ++ i)
    {
        str.clear();
        for (int j = 0; j < 4; ++ j)
            str += map[j][i];
        int res = check(str);
        if (res > 0) return RES[res];
    }
    
    str.clear();
    for (int i = 0; i < 4; ++ i)
        str += map[i][i];
    res = check(str);
    if (res > 0) return RES[res];

    str.clear();
    for (int i = 0; i < 4; ++ i)
        str += map[i][3 - i];
    res = check(str);
    if (res > 0) return RES[res];
    
    for (int i = 0; i < 4; ++ i)
        if (map[i].find('.') != -1) return RES[4];
    
    return RES[3];
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T; cin >>T;
    for (int t = 1; t <= T; ++ t)
        printf("Case #%d: %s\n", t, work().c_str());
}

