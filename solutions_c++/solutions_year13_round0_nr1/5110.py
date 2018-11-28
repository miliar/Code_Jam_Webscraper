#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <numeric>
#include <functional>
#include <utility>
#include <bitset>
#include <iostream>
#include <cmath>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <stdint.h>
#include <cstdarg>
#include <cstdio>
#include <fcntl.h>

using namespace std;

char s[1000];

int win[][4] = {{0, 1, 2, 3},
                {4, 5, 6, 7},
                {8, 9, 10, 11},
                {12, 13, 14, 15},
                {0, 4, 8, 12},
                {1, 5, 9, 13},
                {2, 6, 10, 14},
                {3, 7, 11, 15},
                {0, 5, 10, 15},
                {3, 6, 9, 12}};
                

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int _;
    scanf("%d\n", & _);
    for (int __ = 1; __ <= _; ++ __)
    {
        scanf("%s\n", s);
        scanf("%s\n", s + 4);
        scanf("%s\n", s + 8);
        scanf("%s\n", s + 12);
        int res = 0;
        for (int i = 0; i < 10; ++ i)
        {
            bool flag = 1;
            for (int j = 0; j < 4; ++ j)
                flag = flag && (s[win[i][j]] == 'X' || s[win[i][j]] == 'T');
            if (flag)
                res = 1;
        }
        for (int i = 0; i < 10; ++ i)
        {
            bool flag = 1;
            for (int j = 0; j < 4; ++ j)
                flag = flag && (s[win[i][j]] == 'O' || s[win[i][j]] == 'T');
            if (flag)
                res = -1;
        }
        if (res == 0)
            for (int i = 0; i < 16; ++ i)
                if (s[i] == '.')
                    res = 2;
        if (res == 0)
            printf("Case #%d: Draw\n", __);
        else if (res == 1)
            printf("Case #%d: X won\n", __);
        else if (res == 2)
            printf("Case #%d: Game has not completed\n", __);
        else
            printf("Case #%d: O won\n", __);
    }
    fclose(stdout);
}



