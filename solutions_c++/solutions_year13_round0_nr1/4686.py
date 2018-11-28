#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

char map[9][9];
/// 1 for X, -1 for O, 0 for
int check(vector<int> a)
{
    int cotX = 0, cotO = 0, cotT = 0;
    for(int i = 0; i < a.size(); ++ i)
    {
        if(a[i] == 'X') cotX ++;
        if(a[i] == 'O') cotO ++;
        if(a[i] == 'T') cotT ++;
    }
    if(cotX == 4 || (cotX == 3 && cotT == 1)) return 1;
    if(cotO == 4 || (cotO == 3 && cotT == 1)) return -1;
    return 0;
}
int check2()
{
    int ans = -11;
    for(int i = 1; i <= 4; ++ i)
    {
        vector<int> a;
        for(int j = 1; j <= 4; ++ j) a.push_back(map[i][j]);
        int r = check(a);
        if(r != 0) return r;
    }
    for(int j = 1; j <= 4; ++ j)
    {
        vector<int> a;
        for(int i = 1; i <= 4; ++ i) a.push_back(map[i][j]);
        int r = check(a);
        if(r != 0) return r;
    }
    vector<int>a;
    for(int i = 1; i <= 4; ++ i) a.push_back(map[i][i]);
    int r = check(a);
    if(r != 0) return r;

    a.clear();
    for(int i = 1; i <= 4; ++ i) a.push_back(map[i][4 + 1 - i]);
    r = check(a);
    if(r != 0) return r;

    return 0;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, cot = 1;
    scanf("%d", &T);
    while(T --)
    {
        for(int i = 1; i <= 4; ++ i) scanf("%s", map[i] + 1);
        int r = check2();
        printf("Case #%d: ", cot ++);
        if(r == 1)
        {
            puts("X won");
        }
        else if(r == -1) puts("O won");
        else
        {
            bool space = 0;
            for(int i = 1; i <= 4; ++ i) for(int j = 1; j <= 4; ++ j)
            {
                if(map[i][j] == '.') space = 1;
            }
            if(space) puts("Game has not completed");
            else puts("Draw");
        }


    }
    return 0;
}
