#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;

typedef vector<int> vi;
typedef vector<char> vc;

class state {

    private:

    vi vx;
    int p;
    int x;

    public:

    state() {
        p = 0;
        x = 1;
    }

    void add(int xi) {
        vx.push_back(xi);
    }

    void go(int t) {
        if (p == vx.size() || vx[p] == x) {
            return;
        }
        if (abs(x - vx[p]) <= t) {
            x = vx[p];
            return;
        }
        if (x < vx[p]) {
            x += t;
        } else {
            x -= t;
        }
    }

    int push(void) {
        int t = abs(x - vx[p]) + 1;
        x = vx[p];
        p++;
        return t;
    }

};

void load(state & o, state & b, vc & seq) {

    int n, x;
    char c[666];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {

        scanf("%s %d", c, &x);

        seq.push_back(c[0]);
        if (c[0] == 'O') {
            o.add(x);
        } else {
            b.add(x);
        }
    }
}

int main(void) {

    int t;
    scanf("%d", &t);

    for (int ti = 1; ti <= t; ti++) {
        printf("Case #%d: ", ti);

        state o, b;
        vc seq;
        load(o, b, seq);

        int dt, t;
        t = 0;
        for (int i = 0; i < seq.size(); i++) {

            if (seq[i] == 'O') {
                dt = o.push();
                b.go(dt);
            } else {
                dt = b.push();
                o.go(dt);
            }
            t += dt;

        }

        printf("%d\n", t);
    }

    return 48-48;
}
