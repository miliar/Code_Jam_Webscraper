#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

struct Case {
    int num_typed;
    int total;
    vector<double> probs;
};

void solve_case(int n, Case& c)
{
    double result;

    double p1 = 1.0;
    for (int i = 0; i < c.num_typed; ++i) {
        p1 *= c.probs[i];
    }
    double e1 = p1 * (c.total - c.num_typed + 1) + (1 - p1) * (2 * c.total - c.num_typed + 2);
    double e2 = c.total + 2;
    double min = e1 > e2 ? e2 : e1;

    double bp = p1;
    double be;
    for (int i = 1; i <= c.num_typed; ++i) {
        bp /= c.probs[c.num_typed - i];
        be = bp * (2 * i + c.total - c.num_typed + 1) + (1 - bp) * (2 * i + 2 * c.total - c.num_typed + 2);
        if (be < min) min = be;
    }

    printf("Case #%d: %f\n", n, min);
}

int main(int argc, char *argv[])
{
    FILE *f = fopen(argv[1], "r");
    int n;

    fscanf(f, "%d", &n);
    for (int i = 0; i < n; ++i) {
        Case c;
        fscanf(f, "%d %d", &c.num_typed, &c.total);
        for (int j = 0; j < c.num_typed; ++j) {
            double k;
            fscanf(f, "%lf", &k);
            c.probs.push_back(k);
        }

        solve_case(i+1, c);
    }
    fclose(f);
}
