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

int main()
{
    //freopen("data.in", "r", stdin);
    //freopen("data.out", "w", stdout);

    int T, N;
    scanf("%d", &T);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        int C, mini = 10000000, sum = 0, ans = 0;
        scanf("%d", &N);
        for(int i = 0; i < N; i++)
        {
            scanf("%d", &C);
            ans += C;
            sum ^= C;
            mini = min(mini, C);
        }
        printf("Case #%d: ", tcase);
        if(sum)
            printf("NO\n");
        else
            printf("%d\n", ans - mini);
    }

    return 0;
}

