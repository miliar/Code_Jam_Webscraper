#include<iostream>
#include<cstdio>

using namespace std;

int n, m;
char t[50][51];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; ++i)
            scanf("%s", t[i]);
        for(int i = 0; i < n - 1; ++i)
            for(int j = 0; j < m - 1; ++j)
                if(t[i][j] == '#' && t[i][j+1] == '#' && t[i+1][j] == '#' && t[i+1][j+1] == '#')
                {
                    t[i][j] = t[i+1][j+1] = '/';
                    t[i][j+1] = t[i+1][j] = '\\';
                }
        
        int ok = 1;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
                if(t[i][j] == '#')
                {
                    ok = 0;
                    break;
                }
        
        printf("Case #%d:\n", Ti);
        if(ok)
            for(int i = 0; i < n; ++i)
                puts(t[i]);
        else
            puts("Impossible");
    }
    return 0;
}
