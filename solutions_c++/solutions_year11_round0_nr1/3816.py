#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;
int abs(int x)
{
    return x < 0 ? -x : x;
}
int main()
{
    int n, t, v;
    char ch;
    freopen("data.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    scanf("%d", &t);
    for(int j = 1;j <= t;j++)
    {
        scanf("%d", &n);
        vector<pair<char, int> > pos;
        for(int i = 0;i < n;i++)
        {
            scanf(" %c%d", &ch, &v);
            pos.push_back(make_pair(ch, v));
        }
        int lastO = 0, lastB = 0;
        int reachO = 1, reachB = 1;
        for(int i = 0;i < n;i++)
        {
            if(pos[i].first == 'O')
            {
                lastO += abs(reachO - pos[i].second) + 1;
                reachO = pos[i].second;
                lastO = max(lastB + 1, lastO);
            }
            else
            {
                lastB += abs(reachB - pos[i].second) + 1;
                reachB = pos[i].second;
                lastB = max(lastB, lastO + 1);
            }
        }
        printf("Case #%d: %d\n",j, max(lastB, lastO));
    }
    return 0;
}
