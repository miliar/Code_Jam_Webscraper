#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;

int cas, Pd, Pg, D, G;
LL N;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        cin>>N>>Pd>>Pg;
        //scanf("%d%d%d",&N,&Pd,&Pg);
        printf("Case #%d: ",run);
        if (Pg == 100)
        {
            if (Pd<100)
            {
                puts("Broken");
                continue;
            }
            else
            {
                puts("Possible");
                continue;
            }
        }
        if (Pg == 0)
        {
            if (Pd>0)
            {
                puts("Broken");
                continue;
            }
            else
            {
                puts("Possible");
                continue;
            }
        }
        else
        {
            D = 100;
            if (Pd%2==0) D/=2;
            if (Pd%4==0) D/=2;
            if (Pd%5==0) D/=5;
            if (Pd%25==0) D/=5;
            if (D<=N)
            {
                puts("Possible");
                continue;
            }
            else
            {
                puts("Broken");
                continue;
            }
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
