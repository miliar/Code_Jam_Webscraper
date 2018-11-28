#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long huge;

huge mdc(huge a, huge b)
{
    return(b == 0 ? a : mdc(b,a%b));
}

int main(void)
{
    int caso,C;

    for(scanf("%d",&C), caso = 1; caso <= C; caso++)
    {
        int N;
        scanf("%d",&N);
        huge v[N];

        for(int i = 0; i < N; i++)
            scanf("%lld",v+i);

        huge T,y;
        T = (N == 2) ? abs(v[0]-v[1]) : mdc(abs(v[0]-v[1]),mdc(abs(v[1]-v[2]),abs(v[0]-v[2])));
        y = T-(v[0]%T);
        if (y == T) y = 0;
        printf("Case #%d: %lld\n",caso,y);
    }

    return(0);
}

