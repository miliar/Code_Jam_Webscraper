#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

int dist_[101][101][101];

struct state {
    int o, b, gdje;

    state(int o = 0, int b = 0, int gdje = 0) :
        o(o), b(b), gdje(gdje) {}

    int& dist() {
        return dist_[o][b][gdje];
    }
};

char robseq[101];
int numseq[101];
int n;

bool valid(int x) {
    return 0 <= x && x < 100;
}

void update(queue<state>& Q, state curr, state next) {
    if (!valid(next.o)) return;
    if (!valid(next.b)) return;
    if (next.dist() != -1) return;

    next.dist() = curr.dist() + 1;
    Q.push(next);
}

int bfs() {
    memset(dist_, -1, sizeof dist_);
    state start(0,0,0);
    start.dist() = 0;

    queue<state> Q;

    for (Q.push(start); !Q.empty(); Q.pop()) {
        state curr = Q.front();

        if (curr.gdje == n) {
            return curr.dist();
        }

        // inace se siri

        // idemo prvo rijesiti samo pomake
        for (int dx = -1; dx <= 1; ++dx)
            for (int dy = -1; dy <= 1; ++dy)
                update(Q, curr, state(curr.o+dx, curr.b+dy, curr.gdje));

        if (curr.o == numseq[curr.gdje] && robseq[curr.gdje] == 'O') {
            for (int dx = -1; dx <= 1; ++dx) {
                update(Q, curr, state(curr.o, curr.b+dx, curr.gdje+1));
            }
        }
        if (curr.b == numseq[curr.gdje] && robseq[curr.gdje] == 'B') {
            for (int dx = -1; dx <= 1; ++dx) {
                update(Q, curr, state(curr.o+dx, curr.b, curr.gdje+1));
            }
        }
    }
    return -1;
}

int main(void) {
 int test; scanf("%d", &test);

 for (int cs = 0; cs < test; ++cs) {
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        char buff[12]; scanf("%s", buff);
        robseq[i] = *buff;
        scanf("%d", numseq+i);
        --numseq[i];
    }

    int sol = bfs();
    printf("Case #%d: %d\n", cs+1, sol);
 }
 return 0;
}
