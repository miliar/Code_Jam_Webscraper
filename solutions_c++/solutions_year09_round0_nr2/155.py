#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i)
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i)
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i)
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std;
static const double EPS = 1e-9;
typedef long long ll;

/** ------ find-union ------ **/
struct Node {
    char label;
    int rank;
    struct Node *p;
};

typedef struct Node Node;

void init(Node &a) {
    a.label = '\0';
    a.rank = 0;
    a.p = &a;
}

Node *find(Node *a) {
    if (a->p != a)
        a->p = find(a->p);
    return a->p;
}

void merge(Node *a, Node *b) {
    Node *pa = find(a);
    Node *pb = find(b);
    
    if (pa != pb) {
        if (pa->rank < pb->rank)
            swap(pa, pb);
        pb->p = pa;
    }
}
/** ------ find-union ------ **/

#define MAX_H 100
#define MAX_W 100

vector<string> solve(const vector<vector<int> > &input) {
    static const int di[4] = {-1, 0, 0, 1};
    static const int dj[4] = {0, -1, 1, 0};
    static Node nodes[MAX_H][MAX_W];
    int H = input.size();
    int W = input[0].size();
        
    REP(i, H) REP(j, W) init(nodes[i][j]);

    REP(i, H) REP(j, W) {
        int max_d = -1;
        int max_k = -1;
        REP(k, 4) {
            int ii = i + di[k];
            int jj = j + dj[k];
            if (0 <= ii && ii < H && 0 <= jj && jj < W &&
                input[ii][jj] < input[i][j]) {
                int d = input[i][j] - input[ii][jj];
                if (d > max_d) {
                    max_d = d;
                    max_k = k;
                }
            }
        }
        if (max_k != -1)
            merge(&nodes[i][j], &nodes[i+di[max_k]][j+dj[max_k]]);
    }

    vector<string> ret(H, string(W, ' '));
    char id = 'a';
    REP(i, H) REP(j, W) {
        Node *p = find(&nodes[i][j]);
        if (p->label == '\0') {
            assert(id <= 'z');
            p->label = id;
            ++id;
        }
        ret[i][j] = p->label;
    }

    return ret;
}

int main(void)
{
    int T;
    cin >> T;

    REP(caseID, T) {
        int H, W;
        cin >> H >> W;
        vector<vector<int> > input(H, vector<int>(W));
        REP(i, H) REP(j, W) cin >> input[i][j];

        vector<string> ans = solve(input);
        cout << "Case #" << caseID+1 << ":" << endl;
        REP(i, H) {
            REP(j, W) {
                if (j)
                    cout << ' ';
                cout << ans[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
