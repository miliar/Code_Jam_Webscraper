#include <stdio.h>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

#define f first
#define s second

vector <pair <pair <int, int>, string> > T;
vector <pair <int, int> > V;
set <string> S;

int main(void)
{
    int N;
    int test, tests;
    char name[1024];
    
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
    {
        int i, x, y, posible = 0, min = 100000000;
        
        scanf("%d\n", &N);
        T.clear();
        for (i = 0; i < N; i++)
        {
            scanf("%s%d%d\n", name, &x, &y);
            T.push_back(make_pair(make_pair(x, y), name));
        }
        
        sort(T.begin(), T.end());
        
        int config, to = 1 << N;
        for (config = 1; config < to; config++)
        {
            S.clear(), V.clear();
            for (i = 0; i < N; i++)
                if (config & (1 << i))
                   S.insert(T[i].s), V.push_back(make_pair(T[i].f.f, T[i].f.s));
            if (S.size() <= 3)
            {
               int last = V[0].s, ok = 1;
               
               if (V[0].f != 1)
                  continue;
               
               for (i = 1; i < V.size() && ok; i++)
               {
                   if (V[i].f > last + 1)
                      ok = 0;
                   last = max(last, V[i].s);
               }
               if (last != 10000)
                  ok = 0;
               if (!ok)
                  continue;
               posible = 1;
               int cnt = 0;
               for (i = 0; i < N; i++)
                   if (config & (1 << i))
                      cnt++;

               if (cnt < min)
                  min = cnt;
            }
        }
        
        if (!posible)
           printf("Case #%d: IMPOSSIBLE\n", test);
        else printf("Case #%d: %d\n", test, min);
    }
    
    return 0;
}
