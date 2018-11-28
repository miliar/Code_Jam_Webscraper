/*
ID   : mnlm1991
PROG : 
LANG : C++
*/

#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<iterator>
#include<algorithm>

using namespace std;

typedef long long LL;

char str[2][3][100] = 
{
    "ejp mysljylc kd kxveddknmc re jsicpdrysi", 
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
    "de kr kd eoya kw aej tysr re ujdr lkgc jv", 
    "our language is impossible to understand", 
    "there are twenty six factorial possibilities", 
    "so it is okay if you want to just give up"
};
char sw[128];
char s[1000000];
int main()
{
    freopen("A-small-attempt4.in", "r", stdin);
    freopen("A-small-attempt4.out", "w", stdout);
    memset(sw, 0, sizeof(sw));
    bool vis[128];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; str[0][i][j]; j++)
        {
            sw[str[0][i][j]] = str[1][i][j];
            vis[str[1][i][j]] = true;
        }
    }
    sw['z'] = 'q';
    sw['q'] = 'z';
    for (int i = 'a'; i <= 'z'; i++)
    {
        if (sw[i] == 0)
        //    printf("%c\n", i);
        if (!vis[i])
        {
        //    printf("111111%c\n", i);
        }
    }
    int T;
    while (scanf("%d", &T) != EOF)
    {
        getchar();
        int tc = 1;
        while (T--)
        {
            gets(s);
            printf("Case #%d: ", tc++);
            for (int i = 0; s[i]; i++)
            {
                putchar(sw[s[i]]);
            }
            printf("\n");
        }
    }
    return 0;
}
