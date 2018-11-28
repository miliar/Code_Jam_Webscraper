#include <cstdio>
#include <cmath>

#include <algorithm>
#include <vector>

using namespace std;

const int MAX = 1024;

struct Segm
{
    double len;
    int v_walk, v_run;
    Segm() {}
    Segm(int a, int b, int c) : len(a), v_walk(b), v_run(c) {}

    double tWalk() { return len/v_walk; }
    double tRun() { return len/v_run; }
    double tRun(double t) {
        double l1 = t*v_run;
        if (l1 >= len)
            return len/v_run; else
            return t + (len - l1)/v_walk;
    }

    void reduceRun(double t) {
        len -= v_run*t;
    }

    double savings() const { return double(v_run - v_walk)/v_walk; }
};

bool operator<(const Segm& a, const Segm& b)
{
    return a.savings() > b.savings();
}

int L, V_walk, V_run, t_run, N;
int B[MAX], E[MAX], w[MAX];

double solve()
{
    scanf("%d %d %d %d %d", &L, &V_walk, &V_run, &t_run, &N);

    int L_walk = L;
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &B[i], &E[i], &w[i]);
        L_walk -= E[i] - B[i];
    }

    vector<Segm> segm;
    if (L_walk)
        segm.push_back(Segm(L_walk, V_walk, V_run));
    for (int i = 0; i < N; i++)
        segm.push_back(Segm(E[i]-B[i], V_walk+w[i], V_run+w[i]));

    sort(segm.begin(), segm.end());
    double t_remain = t_run, t_total = 0.0;

    for (int i = 0; i < segm.size(); i++) {
        double t0 = min(t_remain, segm[i].tRun());
        t_remain -= t0;
        segm[i].reduceRun(t0);
        t_total += segm[i].tWalk() + t0;
    }
    return t_total;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        printf("Case #%d: %.9lf\n", i+1, solve());
    return 0;
}
