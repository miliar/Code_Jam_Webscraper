#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M;
vector<int> G, C, I;

void update(int& cost, int lv, int rv, int add)
{
    if (lv == -1 || rv == -1) return;
    int c = lv + rv + add;
    if (cost == -1) cost = c;
    else cost = min(cost, c);
}

void calc(int idx, int& fcost, int& tcost)
{
    fcost = tcost = -1;
    if (I[idx] != -1) {
        if (I[idx]) tcost = 0;
        else fcost = 0;
        return;
    }

    int g = G[idx];
    int c = C[idx];
    int li = 2 * idx + 1;
    int ri = 2 * idx + 2;

    int lf, lt, rf, rt;
    calc(li, lf, lt);
    calc(ri, rf, rt);

    if (g || c) {
        int add = 0;
        if (!g && c) add = 1;

        update(fcost, lf, rf, add);
        update(fcost, lf, rt, add);
        update(fcost, lt, rf, add);
        update(tcost, lt, rt, add);
    }

    if (!g || c) {
        int add = 0;
        if (g && c) add = 1;

        update(fcost, lf, rf, add);
        update(tcost, lf, rt, add);
        update(tcost, lt, rf, add);
        update(tcost, lt, rt, add);
    }

    return;
}

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int V;
        cin >> M >> V;
        G.clear();
        C.clear();
        I.clear();

        for (int i = 0; i < (M-1)/2; ++i) {
            int g, c;
            cin >> g >> c;
            G.push_back(g);
            C.push_back(c);
            I.push_back(-1);
        }

        for (int j = (M-1)/2; j < M; ++j) {
            int i;
            cin >> i;
            G.push_back(-1);
            C.push_back(-1);
            I.push_back(i);
        }

        cout << "Case #" << cs + 1 << ": ";
        int fcost, tcost;
        calc(0, fcost, tcost);
        int cost = (V ? tcost : fcost);
        if (cost == -1) cout << "IMPOSSIBLE";
        else cout << cost;
        cout << '\n';
    }

    return 0;
}
