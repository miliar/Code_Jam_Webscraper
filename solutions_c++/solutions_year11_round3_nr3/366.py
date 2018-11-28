#include<iostream>
#include<cstdio>

using namespace std;

typedef long long ll;

int n, l, h;
int t[100];

int main()
{
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        printf("Case #%d: ", Ti);
        scanf("%d %d %d", &n, &l, &h);
        for(int i = 0; i < n; ++i)
            scanf("%d", t+i);
        for(int i = l; i <= h; ++i)
        {
            int ok = 1;
            for(int j = 0; j < n; ++j)
                if(t[j] % i && i % t[j])
                {
                    ok = 0;
                    break;
                }
            if(ok)
            {
                printf("%d\n", i);
                goto kraj;
            }
        }
        printf("NO\n");
kraj:;
    }
    return 0;
}
