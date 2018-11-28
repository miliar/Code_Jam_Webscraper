#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

int pO, pB, nowO, nowB, n, N, t, temp, ans;
char c;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &N);
    for(int T = 1;T <= N;T++)
    {
        scanf("%d%c", &n, &c);
        nowO = 1;
        nowB = 1;
        pB = 0;
        pO = 0;
        for(int i = 1;i <= n;i++)
        {
            if(i!=n) scanf("%c %d ", &c, &t);
            else scanf("%c %d\n", &c, &t);
            if(c == 'O')
            {
                temp = nowO-t>0?nowO-t:t-nowO;
                if(temp+pO+1 <= pB+1)
                {
                    pO = pB+1;
                }
                else
                {
                    pO = temp+pO+1;
                }
                ans = pO;
                nowO = t;
            }
            else if(c == 'B')
            {
                temp = nowB-t>0?nowB-t:t-nowB;
                if(temp+pB+1 <= pO+1)
                {
                    pB = pO+1;
                }
                else
                {
                    pB = temp+pB+1;
                }
                ans = pB;
                nowB = t;
            }
        }
        printf("Case #%d: %d\n",T, ans);
    }
    return 0;
}
