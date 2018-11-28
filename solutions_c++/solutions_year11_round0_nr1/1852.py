#include <stdio.h>
#include <vector>
#include <utility>

#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)
#define fi first
#define se second

using namespace std;

int zn(int pred, int id)
{
    if(pred < id)
        return 1;
    else if(pred == id)
        return 0;
    else
        return -1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int i = 0; i < test; i++)
    {
        int n;
        scanf("%d", &n);
        vector<pair<int, int> > O, B;
        for(int j = 0; j < n; j++)
        {
            char x[3];
            int but = 0;
            scanf("%1s", x);
            scanf("%d", &but);
            if(x[0] == 'O')
                O.pb(mp(but, j));
            else
                B.pb(mp(but, j));
        }
        int now_o = 1;
        int now_b = 1;
        int time = 0;
        int list_o = 0;
        int list_b = 0;
       // printf("start\n");
        while(list_o < (int)O.size() && list_b < (int)B.size())
        {
            if(now_o == O[list_o].fi && O[list_o].se < B[list_b].se)
            {
                time += 1;
               // printf("Push O %d - %d\n", O[list_o].fi, time);

                list_o++;
                now_b += zn(now_b, B[list_b].fi);
            }
            else if(now_b == B[list_b].fi && B[list_b].se < O[list_o].se)
            {
                time += 1;
               // printf("Push B %d, - %d\n", B[list_b].fi, time);

                list_b++;
                now_o += zn(now_o, O[list_o].fi);
            }
            else
            {
               // printf("go\n");
                now_b += zn(now_b, B[list_b].fi);
                now_o += zn(now_o, O[list_o].fi);
                time += 1;
            }
        }
        //printf("list_o = %d, list_b = %d, now_o = %d, now_b =%d\n", list_o, list_b, now_o, now_b);
        while(list_o < (int)O.size())
        {
            time += abs(now_o - O[list_o].fi) + 1;
            now_o = O[list_o].fi;
            list_o++;
        }
        while(list_b < (int)B.size())
        {
            time += abs(now_b - B[list_b].fi) + 1;
            now_b = B[list_b].fi;
            list_b ++;
        }
        printf("Case #%d: %d\n", i + 1, time);
    }
    return 0;
}
