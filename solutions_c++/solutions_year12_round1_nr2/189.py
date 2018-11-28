#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct level
{
    int b, tindex;
    bool operator < (const level& a) const
    {
        return b > a.b;
    }
};

const int MAXN = 1010;
char complete[MAXN][2];
int require[MAXN][2];
level l[MAXN];

int main()
{
    int T, N, ans, nowStar, target;
    scanf("%d", &T);

    for(int t = 1; T--; t++)
    {
        scanf("%d", &N);
        ans = nowStar = 0, target = N<<1;

        memset(complete, 0, sizeof(complete));
        for(int i = 0; i < N; i++)
        {
            scanf("%d%d", &require[i][0], &require[i][1]);
            l[i].b = require[i][1], l[i].tindex = i;
        }

        sort(l, l+N);

        while(nowStar != target)
        {
            bool flag = false;
            for(int j = 0; j < N; j++) //attack 2-star
                if(complete[j][1] == 0 && nowStar >= require[j][1])
                {
                    nowStar += (2 - complete[j][0]);
                    complete[j][0] = complete[j][1] = 1;
                    flag = true;
                    ++ans;
                    break;
                }
    
            if(flag) continue;
            for(int j = 0; j < N; j++) //attack 1-star
            {
                int now = l[j].tindex;
                if(complete[now][0] == 0 && nowStar >= require[now][0])
                {
                    complete[now][0] = 1;
                    flag = true;
                    ++nowStar;
                    ++ans;
                    break;
                }
            }

            if(!flag) break;
        }

        if(nowStar==target) printf("Case #%d: %d\n", t, ans);
        else                printf("Case #%d: Too Bad\n", t);
    }
    return 0;
}
