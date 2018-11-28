#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

void solve()
{
    int N;
    int seq[110];
    
    scanf("%d", &N);
     
    for (int i = 0; i < N; i++)
    {
        char c;
        int m;
        getchar();
        scanf("%c %d", &c, &m);
        if (c == 'O')seq[i] = m;
        else seq[i] = -m;
    }
     
    int preom = 1, prebm = 1;
    int preoans = 0, prebans = 0;
    int ans = 0;
     
    for (int i = 0; i < N; i++)
    {
        int m = abs(seq[i]);
        
        
        if (i == 0)
        {
            ans = ans + m - 1 + 1;
        }
        else if (seq[i] * seq[i - 1] > 0)
        {
            ans = ans + abs(abs(seq[i]) - abs(seq[i - 1])) + 1;
        }
        else
        {
            if (seq[i] > 0)
            {
                ans = ans + 1;
                int tmp = preoans + abs(m - preom) + 1;
                if (tmp > ans)ans = tmp;
            }
            else
            {
                ans = ans + 1;
                int tmp = prebans + abs(m - prebm) + 1;
                if (tmp > ans)ans = tmp;
            }
        }
        if (seq[i] > 0)preom = m, preoans = ans;
        else prebm = m, prebans = ans;
    }
    printf("%d\n", ans);
}
 
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
