#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
char map[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
void chg(char c)
{
    if (c == ' ')
        printf(" ");
    else
        printf("%c",map[c - 'a']);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,n,s,p;
    int t[105];
    int ans;
    scanf("%d",&T);
    for (int ca = 1; ca <= T; ca++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for (int i = 1; i <= n; ++i)
            scanf("%d",&t[i]);
        ans = 0;
        for (int i = 1; i <= n; ++i)
        {
            if (t[i] >= 3*p - 2)
                ans++;
            else if (p > 1 && t[i] >= 3*p - 4)
            {
                if (s > 0)
                {
                    s--;ans++;
                }
            }
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}

