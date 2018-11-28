#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 2100000000
#define eps 1e-8
#define lld long long

using namespace std;
int n, i, j;
char s[12][12];
int judge(char c)
{
    int a,b;
    for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
            if ((s[i][j] == c) || (s[i][j] == 'T'))
            {
                a =b =0;
                if (s[i][j] == c) a++;
                else b++;
                if (s[i + 1][j] == c) a++;
                else if (s[i + 1][j] == 'T') b++;
                if (s[i + 2][j] == c) a++;
                else if (s[i + 1][j] == 'T') b++;
                if (s[i + 3][j] == c) a++;
                else if (s[i + 3][j] == 'T') b++;
                if ((a==4) || (a==3&&b==1)) return 1;
                a =b =0;
                if (s[i][j] == c) a++;
                else b++;
                if (s[i][j + 1] == c) a++;
                else if (s[i][j + 1] == 'T') b++;
                if (s[i][j + 2] == c) a++;
                else if (s[i][j + 2] == 'T') b++;
                if (s[i][j + 3] == c) a++;
                else if (s[i][j + 3] == 'T') b++;
                if ((a==4) || (a==3&&b==1)) return 1;
                a =b =0;
                if (s[i][j] == c) a++;
                else b++;
                if (s[i + 1][j + 1] == c) a++;
                else if (s[i + 1][j + 1] == 'T') b++;
                if (s[i + 2][j + 2] == c) a++;
                else if (s[i + 2][j + 2] == 'T') b++;
                if (s[i + 3][j + 3] == c) a++;
                else if (s[i + 3][j + 3] == 'T') b++;
                if ((a==4) || (a==3&&b==1)) return 1;
            }
    for(i = 3; i < 4; i++)
        for(j = 0; j < 1; j++)
            if (s[i][j] == c || s[i][j] == 'T')
            {
                a =b =0;
                if (s[i][j] == c) a++;
                else b++;
                if (s[i - 1][j + 1] == c) a++;
                else if (s[i - 1][j + 1] == 'T') b++;
                if (s[i - 2][j + 2] == c) a++;
                else if (s[i - 2][j + 2] == 'T') b++;
                if (s[i - 3][j + 3] == c) a++;
                else if (s[i - 3][j + 3] == 'T') b++;
                if ((a==4) || (a==3&&b==1)) return 1;
            }
    return  0;
}
int main()
{
    int T, tot = 0;
//    freopen("a3.in","r",stdin);
//    freopen("a.out","w",stdout);
    cin>>T;
    while(T--)
    {
        int cnt = 0;
        memset(s,'s',sizeof(s));
        for(i = 0; i < 4; i++)
            scanf("%s", s[i]);
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                if (s[i][j] != '.') cnt++;
        printf("Case #%d: ", ++tot);
        int flag1 = judge('O');
        int flag2 = judge('X');
        if (flag1) puts("O won"); else
        if (flag2) puts("X won"); else
        if (cnt == 16) puts("Draw"); else
        if (!flag1 && !flag2) puts("Game has not completed");
    }
}
