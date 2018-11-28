#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

typedef struct node
{
    int time;
    int type;
} NODE, *PNODE;

typedef vector<NODE> vn;

int cmp(NODE a, NODE b)
{
    if (a.time == b.time)
        return b.type < a.type;
    return a.time < b.time;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        int t[2] = {0};
        scanf("%d", &t[1]);

        int n[2] = {0};
        scanf("%d%d", &n[0], &n[1]);

        vn event;
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < n[j]; k++)
                for (int l = 0; l < 2; l++)
                {
                    int h, m;
                    scanf("%d:%d", &h, &m);

                    NODE tmp;
                    tmp.time = h * 60 + m + t[l];
                    tmp.type = l * 2 + j;
                    event.push_back(tmp);
                }

        sort(event.begin(), event.end(), cmp);

        int cura = 0, curb = 0, maxa = -1, maxb = -1;
        for (vn::iterator j = event.begin(); j != event.end(); j++)
        {
            if (j->type == 0)
                cura++;
            else if (j->type == 1)
                curb++;
            else if (j->type == 2)
                curb--;
            else if (j->type == 3)
                cura--;
            if (cura > maxa) maxa = cura;
            if (curb > maxb) maxb = curb;
        }

        printf("Case #%d: %d %d\n", i + 1, maxa, maxb);
    }
 
    return 0;
}