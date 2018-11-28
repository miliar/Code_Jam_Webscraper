#pragma comment(linker, "/STACK:134217728")

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define sqr(a) ((a)*(a))
#define det2(a,b,c,d) ((a)*(d) - (b)*(c))

    char s[51000];

int main()
{
    int i, j, k, n, p[20];
    int TST, cas;
    
    scanf( "%d", &TST );
    for ( cas = 1 ; cas <= TST ; cas++ )
    {
        scanf( "%d%s", &k, &s);
        for (i = 0 ; i < k; i++ )
            p[i] = i;
        n = strlen(s);
        int res = n+10;
        do
        {
            int la = -1, cnt = 0;
            for ( i = 0 ; i < n ; i+=k )
            {
                for ( j = 0 ; j < k ; j++ )
                {
                    cnt += (la != s[p[j] + i]);
                    la = s[p[j] + i];
                }
            }
            res = min(res, cnt);
        } while( next_permutation(p, p+k) );
        printf( "Case #%d: %d\n", cas, res );
    }


    return 0;
}
