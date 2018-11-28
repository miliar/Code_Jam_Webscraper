#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

char mp[10][10];

int main()
{
    /*freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);*/
    int run_case;
    scanf("%d", &run_case);
    for (int r = 1; r <= run_case; r ++)
    {
        bool full = true, xwin = false, owin = false;
        map<char, int> cnt;
        for (int i = 0; i < 4; ++ i)
        {
            scanf("%s", mp[i]);
            cnt.clear();
            for (int j = 0; j < 4; ++ j)
            {
                if (mp[i][j] == '.') full = false;
                cnt[mp[i][j]] ++;
            }
            if (cnt['X'] + cnt['T'] == 4)
                xwin = true;
            if (cnt['O'] + cnt['T'] == 4)
                owin = true;
        }
        for (int j = 0; j < 4; ++ j)
        {
            cnt.clear();
            for (int i = 0; i < 4; ++ i)
                cnt[mp[i][j]] ++;
            if (cnt['X'] + cnt['T'] == 4)
                xwin = true;
            if (cnt['O'] + cnt['T'] == 4)
                owin = true;
        }
        cnt.clear();
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j)
                if (i == j)
                    cnt[mp[i][j]] ++;
        if (cnt['X'] + cnt['T'] == 4)
                xwin = true;
            if (cnt['O'] + cnt['T'] == 4)
                owin = true;
        cnt.clear();
        for (int i = 0; i < 4; ++ i)
            for (int j = 0; j < 4; ++ j)
                if (i + j == 3)
                    cnt[mp[i][j]] ++;
        if (cnt['X'] + cnt['T'] == 4)
                xwin = true;
            if (cnt['O'] + cnt['T'] == 4)
                owin = true;
        printf("Case #%d: ", r);
        if (xwin)
            printf("X won\n");
        else
            if (owin)
                printf("O won\n");
            else
                if (full)
                    printf("Draw\n");
                else
                    printf("Game has not completed\n");
    }
    return 0;
}
