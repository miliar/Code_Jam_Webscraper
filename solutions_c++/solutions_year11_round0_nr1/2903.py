#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

int pos[110];
char rob[110];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int test, cas=1;
    scanf("%d", &test);
    while(test--)
    {
        int i, j, k, n;
        scanf("%d", &n);
        for(i=0;i<n;i++)
        {
            scanf(" %c %d", &rob[i], &pos[i]);
        }
        int tot=0, o=1, b=1, otot=0, btot=0;
        for(i=0;i<n;i++)
        {
            if(rob[i]=='O')
            {
                int dist = abs(pos[i]-o);
                if(dist<=otot)
                {
                    tot++;
                    otot=0;
                    btot++;
                    o = pos[i];
                }
                else
                {
                    tot += (dist-otot)+1;
                    btot += (dist-otot)+1;
                    otot=0;
                    o = pos[i];
                }
            }
            else
            {
                int dist = abs(pos[i]-b);
                if(dist<=btot)
                {
                    tot++;
                    btot=0;
                    otot++;
                    b = pos[i];
                }
                else
                {
                    tot += (dist-btot)+1;
                    otot += (dist-btot)+1;
                    btot = 0;
                    b = pos[i];
                }
            }
        }
        printf("Case #%d: %d\n", cas++, tot);
    }


    return 0;
}
