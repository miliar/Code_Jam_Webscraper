#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
#include <iostream>

using namespace std;

map<pair<char, char>, char> com, opp;
char str[200];
char stac[200];

int main()
{
   // freopen("data.in", "r", stdin);
   // freopen("data.out", "w", stdout);

    int T, C, D, N;
    scanf("%d", &T);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        com.clear(), opp.clear();
        scanf("%d", &C);
        for(int i = 0; i < C; i++)
        {
            scanf("%s", str);
            com[make_pair(str[0], str[1])] = str[2];
            com[make_pair(str[1], str[0])] = str[2];
        }
        scanf("%d", &D);
        for(int i = 0; i < D; i++)
        {
            scanf("%s", str);
            opp[make_pair(str[0], str[1])] = 0;
            opp[make_pair(str[1], str[0])] = 0;
        }
        scanf("%d%s", &N, str);
        int top = 0;
        // stac[top++] = str[0];
        for(int i = 0; i < N; i++)
        {
            stac[top++] = str[i];
            if(top > 1)
            {
                if(com.find(make_pair(stac[top-1], stac[top-2])) != com.end())
                {
                    top -= 2;
                    stac[top++] = com[make_pair(stac[top], stac[top+1])];
                }
                else
                {
                    for(int j = 0; j < top - 1; j++)
                    {
                        if(opp.find(make_pair(stac[j], stac[top-1])) != opp.end())
                        {
                            top = 0;
                        }
                    }
                }
            }
        }
        printf("Case #%d: [", tcase);
        for(int i = 0; i < top; i++)
        {
            printf("%c%s", stac[i], i == top - 1 ? "": ", ");
        }
        printf("]\n");
    }

    return 0;
}

