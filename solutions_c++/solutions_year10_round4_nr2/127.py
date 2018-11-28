#include <cstdio>
#include <cstring>

using namespace std;

int P;

int ms[16];

int ps[16][2048];

int table[2048][12][12];

int calc(int loc, int level, int miss)
{
    if(!level)
    {
        if(ms[loc] < miss)
            return -1;
        else
            return 0;
    }
    else 
    {
        int& v = table[loc][level][miss];
        if(v)
            return v - 2;

        v = -1;

        int mid = loc + (1 << (level - 1));
        
        int l = calc(loc, level - 1, miss + 1);
        int r = calc(mid, level - 1, miss + 1);

        if(l != -1 && r != -1)
            v = l + r;

        l = calc(loc, level - 1, miss);
        r = calc(mid, level - 1, miss);

        if(l != -1 && r != -1)
        {
            int n = (1 << level);
            int t = l + r + ps[level][loc / n];
    //        printf("!%d %d %d\n", level, loc / n, ps[level][loc / n]);
            if(v == -1 || v > t)
                v = t;
        }
            
        int ret = v;
        v += 2;

        return ret;                
    }
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        memset(table, 0, sizeof(table));
        printf("Case #%d: ", t);

        scanf("%d", &P);
        for(int i = 0; i < (1 << P); i++)
            scanf("%d", ms + i);

        for(int i = 1; i <= P; i++)
            for(int j = 0; j < (1 << (P - i)); j++)
                scanf("%d", &ps[i][j]);
        printf("%d\n", calc(0, P, 0));
    }
    return 0;
}
