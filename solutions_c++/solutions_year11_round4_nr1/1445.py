#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const double eps = 1e-9;
const int maxn = 1010;
int x, s, r, t, n;
int sum = 0;

struct Node {
    int b, e, w;
    Node() {}
    Node(int _b, int _e, int _w): b(_b), e(_e), w(_w) {}
    bool operator<(const Node &m) const {
        return w < m.w;
    }
    void input() {
        scanf("%d%d%d", &b, &e, &w);
        sum += e - b;
    }
    double len() {
        return (double)(e - b);
    }
    double calc() {
        return len() / (double)(r + w);
    }
}node[maxn];

void work() {
    sum = 0;
    scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
    for(int i=0; i<n; ++i) {
        node[i].input();
    }
    if(sum < x) node[n++] = Node(0, x - sum, 0);
    sort(node, node + n);
    double tt = t, res = 0;
    for(int i=0; i<n; ++i) {
        double nt = node[i].calc();
        if(nt < tt && tt > eps) {
            tt -= nt;
            res += nt;
        } else {
            nt = tt + (node[i].len() - (r + node[i].w)*tt)/(double)(s + node[i].w);
            res += nt;
            tt = 0;
        }
    }
    printf("%.10lf\n", res);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; ++i) {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
