#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

int app[257];
char map[257][257];
char opl[257],opr[257];
char cur[257];
char buf[257];
int T,C,D,n,top;

bool refresh()
{
    if (top <= 1) return false;
    if (map[cur[top-1]][cur[top-2]])
    {
        --app[cur[top-1]];
        --app[cur[top-2]];
        cur[top-2] = map[cur[top-1]][cur[top-2]];
        ++app[cur[top-2]];
        top -= 1;
        return true;
    }
    return false;
}

void explose()
{
    for (int i = 0;i < D;++i)
        if (app[opl[i]] && app[opr[i]])
        {
            memset(app,0,sizeof(app));
            top = 0;
            break;
        }
}

int main()
{
    int nowCase = 0;
    scanf("%d",&T);
    while (T--)
    {
        top = 0;
        memset(map,0,sizeof(map));
        memset(app,0,sizeof(app));
        scanf("%d",&C);
        for (int i = 0;i < C;++i)
        {
            scanf("%s",buf);
            map[buf[0]][buf[1]] = map[buf[1]][buf[0]] = buf[2];
        }
        scanf("%d",&D);
        for (int i = 0;i < D;++i)
        {
            scanf("%s",buf);
            opl[i] = buf[0];
            opr[i] = buf[1];
        }
        scanf("%d",&n);
        scanf("%s",buf);
        for (int i = 0;i < n;++i)
        {
            cur[top++] = buf[i];
            ++app[buf[i]];
            while (refresh());
            explose();
        }
        cout << "Case #" << ++nowCase << ": ";
        printf("[");
        for (int i = 0;i < top-1;++i)
            printf("%c, ",cur[i]);
        if (top) printf("%c]\n",cur[top-1]); else printf("]\n");
    }

}
