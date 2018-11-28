#include <cstdio>
#include <algorithm>
using namespace std;

int a[1000];
int pos[1001];
int L, t, N, C;

int get_cost(int cost, int i, int t) {
    int ret = 0;
    if (cost >= t) {
        ret = pos[i+1]-pos[i];
    } else {
        int len = pos[i+1]-pos[i];
        if (cost + 2*len > t) { // bit ce splitanja
            len -= (t-cost)/2;
            ret = (t-cost);
            ret += len;
        } else { // nece biti splitanja
            ret = 2*(pos[i+1]-pos[i]);
        }
    }
    return ret;
}

int main(void) {
 int test; scanf("%d", &test);

 for (int cs = 0; cs < test; ++cs) {
    scanf("%d%d%d%d", &L, &t, &N, &C);
    for (int i = 0; i < C; ++i) {
        scanf("%d", a+i);
    }
    for (int i = 0; i < N; ++i) {
        pos[i+1] = a[i%C];
    }
    pos[0] = 0;
    for (int i = 1; i <= N; ++i) {
        pos[i] += pos[i-1];
       // printf("- %d\n", pos[i]);
    }

    int sol = 1000000;
    if (L >= 0) {
      sol = 2*pos[N];
    }
    if (L >= 1) {
      for (int i = 0; i < N; ++i) {
        int cost = pos[i]*2;
        cost += get_cost(cost, i, t);
        cost += 2*(pos[N]-pos[i+1]);
        sol = min(sol, cost);
      }
    }
    if (L >= 2) {
        for (int i = 0; i < N; ++i) {
            for (int j = i+1; j < N; ++j) {
                int cost = pos[i]*2;
                int a = get_cost(cost, i, t);
                cost += a;
                cost += 2*(pos[j]-pos[i+1]);
                int b = get_cost(cost, j, t);
                cost += b;
                cost += 2*(pos[N]-pos[j+1]);
                sol = min(sol, cost);
            }
        }
    }

    printf("Case #%d: %d\n", cs+1, sol);
 }
 return 0;
}
