#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

#define MOJO 128

int C,M,N;
char b[MOJO][MOJO];

int dfs(int r, int c)
{
    if (r >= M) return(0);
    if (c >= N) return(dfs(r+1,0));
    if (b[r][c] != '.') return(dfs(r,c+1));

    if (r-1 >= 0 && b[r-1][c] == '.') return(dfs(r,c+1));

    char s[MOJO][MOJO];
    int i,x;
    memcpy(s,b,sizeof(s));

    if (r-1 >= 0)
    {
        if (c-1 >= 0) b[r-1][c-1] = '*';
        if (c+1 < N) b[r-1][c+1] = '*';
    }
    x = 0;
    for(i = r; i < M && b[i][c] == '.'; i++)
    {
        b[i][c] = '*';
        x++;
        if (c-1 >= 0) b[i][c-1] = '*';
        if (c+1 < N) b[i][c+1] = '*';
    }
    if (i < M)
    {
        if (c-1 >= 0) b[i][c-1] = '*';
        if (c+1 < N) b[i][c+1] = '*';
    }
    int v1 = x+dfs(r,c+2);
    memcpy(b,s,sizeof(b));
    int v2 = dfs(r,c+1);

    return(max(v1,v2));
}

int main(void)
{
    int caso;

    for(caso = 1, scanf("%d",&C); caso <= C; caso++)
    {
        scanf("%d %d",&M,&N);

        for(int i = 0; i < M; i++)
            scanf("%s",b[i]);

        printf("Case #%d: %d\n",caso,dfs(0,0));
    }

    return(0);
}

