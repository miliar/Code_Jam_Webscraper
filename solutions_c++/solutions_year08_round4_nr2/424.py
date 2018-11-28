#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int t, tt;
int n, m, a;

void input()
{
    scanf("%d %d %d", &n, &m, &a);
}    

int abs(int x)
{
    if (x < 0) return -x;
    return x;
}    

void solve()
{
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= m; j++)
        {
            for (int k = 0; k <= n; k++)
            {
                for (int kk = 0; kk <= m; kk++)
                {
                    if (abs(i * j - k * kk) == a)
                    {
                        printf("Case #%d: 0 0 %d %d %d %d\n", t, i, kk, k, j);
                        return;
                    }    
                }    
            }    
        }    
    }  
    printf("Case #%d: IMPOSSIBLE\n", t);  
}     

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &tt);
    for (t = 1; t <= tt; t++)
    {
        input();
        solve();
    }   
}    
