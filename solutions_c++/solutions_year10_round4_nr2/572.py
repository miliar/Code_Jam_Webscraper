#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

void splitCost(vector<int> &src, vector<int> &dst1, vector<int> &dst2){
    dst1.clear();
    dst2.clear();
    int mid = src.size() / 2;
    for (int i=0; i<src.size(); i++)
        if (i < mid)
            dst1.push_back(src[i]);
        else
            dst2.push_back(src[i]);
}

int totalCost(int P, int mis[], vector<int> cost[]){
    int ans = 0, misTemp[1024];
    vector<int> cost1[12], cost2[12];
    int n = 1<<P;

    if (P==0){
        int buy = (mis[0] == 0 || mis[1] == 0);
        return buy * cost[0][0];
    }

    bool takeFinal = false;
    for (int i=0; i<2*n; i++)
        if (mis[i] == 0)
            takeFinal = true;
/*
    fprintf(stderr, "%d\n", P);
    for (int i=0; i<2*n; i++)
        fprintf(stderr, "%d ", mis[i]);
    fprintf(stderr, "\n");
*/
    for (int i=0; i<P; i++)
        splitCost(cost[i], cost1[i], cost2[i]);

    memcpy(misTemp, mis, 4*2*n);
    ans = totalCost(P-1, misTemp, cost1) + totalCost(P-1, misTemp + n, cost2) + cost[P][0];

    //fprintf(stderr, "%d\n", ans);

    if (!takeFinal){
        memcpy(misTemp, mis, 4*2*n);
        for (int i=0; i<2*n; i++)
            misTemp[i]--;
        int v2 = totalCost(P-1, misTemp, cost1) + totalCost(P-1, misTemp + n, cost2);
        if (v2 < ans)
            ans = v2;
    }
    if (ans < 0)
        fprintf(stderr, "%d %d\n", P, ans);
    return ans;
}

void solve(int tst)
{
    int P, n, mis[1024];
    printf("Case #%d: ", tst);
    scanf("%d", &P);
    n = 1<<P;
    for (int i=0; i<n; i++)
        scanf("%d", mis + i);
    vector<int> cost[12];
    for (int i=0; i<P; i++){
        for (int j=0; j<(1<<(P-i-1)); j++){
            int a;
            scanf("%d", &a);
            cost[i].push_back(a);
        }
        fprintf(stderr, "%d %d %d\n", i, P-1, cost[i].size());
    }
    printf("%d\n", totalCost(P-1, mis, cost));
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    for (int i=1; i<=tst; i++)
        solve(i);
    return 0;
}
