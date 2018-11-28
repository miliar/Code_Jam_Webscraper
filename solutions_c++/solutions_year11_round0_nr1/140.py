#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 128;

int cas;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        int Ox = 1, Bx = 1, ans = 0, freeO = 0, freeB = 0;
        int ch, x, n, tmp;
        for (scanf("%d",&n); n--; )
        {
            for (ch = 0; ch!='O' && ch!='B'; ) ch = getchar();
            scanf("%d",&x);
            if (ch == 'O')
            {
                tmp = max(abs(x-Ox)-freeO,0)+1;
                ans += tmp;
                freeO = 0;
                freeB += tmp;
                Ox = x;
            }
            else
            {
                tmp = max(abs(x-Bx)-freeB,0)+1;
                ans += tmp;
                freeB = 0;
                freeO += tmp;
                Bx = x;
            }
        }
        printf("Case #%d: %d\n",run,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
