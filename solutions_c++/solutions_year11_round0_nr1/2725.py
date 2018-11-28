#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
using namespace std;
int t, n, que[200][2], now[2], next[2], cur, ans, pos[2];
int get_next(int pos, int id)
{
    for(int i = pos; i < n; i++)
        if (que[i][0] == id) return i;
    return -1;
}
bool move(int id)
{
    int from = pos[id], to = que[next[id]][1];
    if (from == to) return false;
    if (to > from) pos[id]++;
    else pos[id]--;
    return true;
}
int main()
{
    freopen("A.txt", "w", stdout);
    scanf("%d", &t);
    for(int cnt = 1; cnt <= t; cnt++)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            char str[3]; int x;
            scanf("%s%d", str, &x);
            que[i][0] = (str[0] == 'O');
            que[i][1] = x;
        }
        ans = cur = 0; pos[0] = pos[1] = 1;
        next[0] = get_next(cur, 0); next[1] = get_next(cur, 1);
        while(next[0] != -1 || next[1] != -1)
        {
            int tmpcur = cur;
            for(int i = 0; i < 2; i++)
                if (next[i] != -1)
                {
                    if (!move(i) && que[cur][0] == i)
                    {
                        tmpcur++;
                        next[i] = get_next(tmpcur, i);
                    }
                }
            cur = tmpcur;
            ans++;
        }
        printf("Case #%d: %d\n", cnt, ans);
    }
    return 0;
}
