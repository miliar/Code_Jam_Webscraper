#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define fij(i, j, k) for(i = j;i <= k;++i)
const int Maxn = 105;
struct node
{
    int first, second;
    inline void pair(int a, int b) { first = a, second = b;} 
}queue[Maxn];
int T, n, S, P, ar[Maxn], tp, ans;

inline bool cmp(node a, node b)
{
    return ((a.second < b.second) || (a.second == b.second && a.first < b.first));
}

int main()
{
    int i, p, cnt = 0;
    for(scanf("%d", &T);T--;)
    {
        printf("Case #%d: ",++cnt);
        ans = tp = 0;
        scanf("%d%d%d", &n, &S, &P);
        fij(i, 1, n) 
        scanf("%d", &ar[i]);
        fij(i, 1, n)
        {
            if(ar[i] > 1) 
            {
                if(ar[i] % 3 == 0)
                    queue[++tp].pair(ar[i] / 3 - 1, ar[i] / 3);
                else if(ar[i] % 3 == 1)
                    queue[++tp].pair(ar[i] / 3 - 1, ar[i] / 3 + 1);
                else 
                    queue[++tp].pair(ar[i] / 3, ar[i] / 3 + 1);
                queue[tp].first += 2;
            }
            else queue[++tp].pair(0,ar[i]);
        }
        sort(queue+1,queue+1+tp, cmp);
        for(p = 1, i = 0;;)
        {
            if(i == S || p > tp) break;
            if(queue[p].first >= P) 
            { ++ans;++i;} 
            ++p;
        }
        for(;;) 
        {
            if(p > tp) break;
            if(queue[p].second >= P) 
                ++ans;
            ++p;
            
        }
        printf("%d\n",ans);
    }
    return 0;
}
