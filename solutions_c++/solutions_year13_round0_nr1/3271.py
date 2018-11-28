/**
 * Copyright (c) 2013 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2013-04-13
 */
#include <cstdio>

using namespace std;

char g[4][4];

bool check(char x)
{
        int cnt1, cnt2;

        for (int i = 0; i < 4; ++i) {
                cnt1 = cnt2 = 0;
                for (int j = 0; j < 4; ++j) {
                        if (g[i][j] == x)
                                ++cnt1;
                        if (g[i][j] == 'T')
                                ++cnt2;
                }
                if (cnt1 >= 3 && cnt1 + cnt2 == 4)
                        return true;
        }

        for (int j = 0; j < 4; ++j) {
                cnt1 = cnt2 = 0;
                for (int i = 0; i < 4; ++i) {
                        if (g[i][j] == x)
                                ++cnt1;
                        if (g[i][j] == 'T')
                                ++cnt2;
                }
                if (cnt1 >= 3 && cnt1 + cnt2 == 4)
                        return true;
        }

        cnt1 = cnt2 = 0;
        for (int i = 0; i < 4; ++i) {
                if (g[i][i] == x)
                        ++cnt1;
                if (g[i][i] == 'T')
                        ++cnt2;
        }
        if (cnt1 >= 3 && cnt1 + cnt2 == 4)
                return true;

        cnt1 = cnt2 = 0;
        for (int i = 0; i < 4; ++i) {
                if (g[i][4-i-1] == x)
                        ++cnt1;
                if (g[i][4-i-1] == 'T')
                        ++cnt2;
        }
        if (cnt1 >= 3 && cnt1 + cnt2 == 4)
                return true;

        return  false;
}

bool full()
{
        for (int i = 0; i < 4; ++i)
                for (int j = 0; j < 4; ++j)
                        if (g[i][j] == '.')
                                return false;

        return true;
}

int main()
{
        //freopen("A-large.in", "r", stdin);
        //freopen("A-large.out", "w", stdout);

        int T, cas = 0;

        scanf("%d", &T);

        while (T--) {
                for (int i = 0; i < 4; ++i)
                        scanf("%s", g[i]);

                if (check('X')) {
                        printf("Case #%d: X won\n", ++cas);
                } else if (check('O')) {
                        printf("Case #%d: O won\n", ++cas);
                } else if (!full()) {
                        printf("Case #%d: Game has not completed\n", ++cas);
                } else {
                        printf("Case #%d: Draw\n", ++cas);
                }
        }

        return 0;
}
