#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>
#include<iostream>
#include<algorithm>

using namespace std;

#define FOR(_i, _times) for(int _i = 1; _i <= (_times); _i++)
#define FORV(_i, _times) for(int _i = 0; _i < (_times); _i++)
#define FORR(_i, _st, _ed) for(int _i = (_st); _i >= (_ed); _i--)
#define FORE(_i, _st, _ed) for(int _i = (_st); _i <= (_ed); _i++)

int T, a1, a2, b1, b2;
map<pair<int, int>, char> dp;

char OPT(int a, int b)
{
    if(a > b) return OPT(b, a);
    if(a == b) return 'P';
    if(a == 1) return 'N';
    if(dp[make_pair(a, b)] == 0)
    {
        for(int k = 1; a - b * k > 0; k++)
        {
            if(OPT(a - b * k, b) == 'P')
            {
                dp[make_pair(a, b)] = 'N';
                return 'N';
            }
        }
        for(int k = 1; b - a * k > 0; k++)
        {
            if(OPT(a, b - a * k) == 'P')
            {
                dp[make_pair(a, b)] = 'N';
                return 'N';
            }
        }
        dp[make_pair(a, b)] = 'P';
    }
    return dp[make_pair(a, b)];
}

int main()
{
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    scanf("%d", &T);
    FOR(ttt, T)
    {
        int counter = 0;
        scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
        FORE(i, a1, a2)
        {
            FORE(j, b1, b2)
            {
                if(OPT(i, j) == 'N')
                {
                    counter++;
                }
            }
        }
        printf("Case #%d: %d\n", ttt, counter);
    }
}
