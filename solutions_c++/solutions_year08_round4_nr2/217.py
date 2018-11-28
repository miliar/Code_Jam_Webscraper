#include <cstdio>
#include <map>

using namespace std;

struct Node {
    int x, y;

    Node() {
    }

    Node(int x, int y) : x(x), y(y) {
    }
};

map<int, Node> rec;

int main() {
    int t, i, N, M, A, x, y, x1, y1, x2, y2, v;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        scanf("%d %d %d", &N, &M, &A);
        rec.clear();
        for (x = 0; x <= N; x++)
            for (y = 0; y <= M; y++)
                rec[x * y] = Node(x, y);
        map<int, Node>::iterator p;
        Node curr, succ;
        bool flag = 0;
        for (p = rec.begin(); p != rec.end(); p++) {
            curr = p->second;
            v = p->first + A;
            if (rec.find(v) != rec.end()) {
                succ = rec.find(v)->second;
                x1 = curr.x;
                y2 = curr.y;
                x2 = succ.x;
                y1 = succ.y;
                printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
                flag = 1;
                break;
            }
        }
        if (!flag) printf("IMPOSSIBLE\n");
    }
    return 0;
}
