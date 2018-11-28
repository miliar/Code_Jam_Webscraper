#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int T, N, S, P, t[100];

int solve()
{
    int result = 0;
    for(int i = 0; i < N; i++)
    {
        int tr = t[i]/3;
        int re = t[i]%3;
        //normal
        if(re == 0 && tr >= P){result++; continue;}
        if(re == 1 && tr+1 >= P){result++; continue;}
        if(re == 2 && tr+1 >= P){result++; continue;}

        //surp
        if(S == 0){continue;}
        if(re == 0 && tr+1 >= P && tr-1 >= 0){result++; S--; continue;}
        if(re == 2 && tr+2 >= P){result++; S--; continue;}
    }

    return result;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &T);

    for(int c = 1; c <= T; c++)
    {
        scanf("%d %d %d", &N, &S, &P);
        for(int i = 0; i < N; i++)
        {
            scanf("%d", t+i);
        }

        printf("Case #%d: %d\n", c, solve());
    }
}