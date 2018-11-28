/*
 * summary:
 *
 */

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string.h>
#define INF (1<<30)
#define MAX 0
#define EPS 0
using namespace std;

int seq[200];
struct node
{
    int i, dis;
    node(int _i, int _dis){i = _i; dis = _dis;}
};
vector<node> O, B;

int main()
{
//    freopen("data.in", "r", stdin);
//    freopen("data.out", "w", stdout);

    int T, N;
    scanf("%d", &T);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        O.clear(), B.clear();
        scanf("%d", &N);
        int preO = 1, preB = 1, t;
        char co[5];
        for(int i = 0; i < N; i++)
        {
            scanf("%s%d", co, &t);
            if(co[0] == 'O')
                O.push_back(node(i, abs(t - preO))), preO = t;
            else 
                B.push_back(node(i, abs(t - preB))), preB = t;
        }
        O.push_back(node(N, 0)), B.push_back(node(N, 0));
        int pO = 0, pB = 0, disO = O[pO].dis, disB = B[pB].dis;
        int ans = 0;
        while(pO < O.size() - 1 || pB < B.size() - 1)
        {
            if(O[pO].i < B[pB].i)
            {
                ans += (disO + 1);
                disB = disB - disO - 1 < 0 ? 0 : disB - disO - 1;
                disO = O[++pO].dis;
            }
            else
            {
                ans += (disB + 1);
                disO = disO - disB - 1 < 0 ? 0 : disO - disB - 1;
                disB = B[++pB].dis;
            }
        }
        printf("Case #%d: %d\n", tcase, ans);
    }

    return 0;
}
