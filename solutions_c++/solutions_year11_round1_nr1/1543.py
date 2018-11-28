#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>
#include<cassert>
#define dbge( x ) cout << #x << " : " <<  x << endl;
using namespace std;


int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        int n, pd, pg;
        scanf("%d %d %d", &n, &pd, &pg);
        int pdn = pd / __gcd(pd, 100);
        int pdd = 100 / __gcd(pd, 100);
        int b = 0;
        if(pdd  <= n)
        {
            if(pg >= pdn && 100 >= pdd && pg - pdn <= 100 - pdd)
                b = 1;
        }

        printf("Case #%d: ", t);
        if(b)
            printf("Possible\n");
        else
            printf("Broken\n");

    }
    return 0;
}

