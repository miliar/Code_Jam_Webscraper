/*
ID: frank44
PROG: C
LANG: C++
 */

#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
    freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, p, q;
    scanf("%d", &t);

    int Q[105];
    bool ok[105];
    for (int x=1; x<=t; x++)
    {
        scanf("%d %d", &p, &q);

        for (int i=0; i<q; i++)
            scanf("%d", &Q[i]);

        sort(Q, Q+q);

        int best = 1000000000;

        do
        {
            int count = 0;
            fill(ok, ok+105, 1);

            for (int i=0; i<q; i++)
            {
                ok[ Q[i] ] = false;
                for (int j=Q[i]+1; j<=p && ok[j]; j++) count++;
                for (int j=Q[i]-1; j>=1 && ok[j]; j--) count++;
            }
            //printf("count = %d\n", count);
            best = min(best, count);

        } while ( next_permutation(Q, Q+q) );

        printf("Case #%d: %d\n", x, best);
    }
}
