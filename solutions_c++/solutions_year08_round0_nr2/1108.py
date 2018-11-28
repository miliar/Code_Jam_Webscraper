#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

enum { A, B };
enum { START, AFTER_REST };
const int last = 23 * 60 + 59;
int cases, cas = 1;
int rest, n, m;
struct Node {
    int x, from, type;
    Node(int xx, int f, int t) : x(xx), from(f), type(t) {
    }
    bool operator<(const Node& p) const {
        if (x != p.x) {
            return x < p.x;
        } else {
            return type > p.type;
        }
    }
};
vector<Node> nodes;

int main() {
    for (cin >> cases; cases--; ) {
        nodes.clear();
        cin >> rest >> n >> m;
        for (int i = 0; i < n; ++i) {
            int a, b; char ch;
            cin >> a >> ch >> b;
            int from = a * 60 + b;
            cin >> a >> ch >> b;
            int to = a * 60 + b;
            nodes.push_back(Node(from, A, START));
            if (to + rest <= last) {
                nodes.push_back(Node(to + rest, A, AFTER_REST));
            }
        }
        for (int i = 0; i < m; ++i) {
            int a, b; char ch;
            cin >> a >> ch >> b;
            int from = a * 60 + b;
            cin >> a >> ch >> b;
            int to = a * 60 + b;
            nodes.push_back(Node(from, B, START));
            if (to + rest <= last) {
                nodes.push_back(Node(to + rest, B, AFTER_REST));
            }
        }
        sort(nodes.begin(), nodes.end());
        int aCnt = 0, bCnt = 0, aAns = 0, bAns = 0;
        for (unsigned i = 0; i < nodes.size(); ++i) {
            Node& node = nodes[i];
            if (node.type == START) {
                if (node.from == A) {
                    if (aCnt == 0) {
                        aAns++;
                    } else {
                        aCnt--;
                    }
                } else {
                    if (bCnt == 0) {
                        bAns++;
                    } else {
                        bCnt--;
                    }
                }
            } else if (node.type == AFTER_REST) {
                if (node.from == A) {
                    bCnt++;
                } else {
                    aCnt++;
                }
            }
        }
        printf("Case #%d: %d %d\n", cas++, aAns, bAns);
    }
    return 0;
}
