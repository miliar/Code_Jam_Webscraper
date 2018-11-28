#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <cstdlib>
#define MAXN 60
using namespace std;
char map[MAXN][MAXN];
int tt, n, m, flag;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &tt);
    for(int t=1; t<=tt; t++)
    {
        printf("Case #%d:\n", t);
        scanf("%d%d", &n, &m);
        int count=0, cunt=0;
        flag=0;
        for(int i=0; i<n; i++)
        {
            scanf("%s", map[i]);
            for(int j=0; j<m; j++)
                if(map[i][j]=='#')
                {
                    cunt++;
                    count++;
                }
            if(cunt%2!=0) {flag=1;}
        }
        if(flag==1 || count%4!=0) {printf("Impossible\n");continue;}
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(map[i][j]=='#')
                {
                    map[i][j]=map[i+1][j+1]='/';
                    map[i+1][j]=map[i][j+1]='\\';
                }
            }
        }
        for(int i=0; i<n; i++)
        {
            printf("%s\n", map[i]);
        }
    }
    return 0;
}
