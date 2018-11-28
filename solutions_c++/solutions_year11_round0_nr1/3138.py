#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <functional>
using namespace std;
#define pb push_back 
#define mp make_pair
#define sz(v) ((int)(v).size()) 
#define rep(i,n) for(int i=0;i<(n);++i) 
#define all(a) (a).begin(),(a).end()
#define foreach(i, a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define inf (1LL << 29)
typedef long long ll;
typedef vector<int> vi;

struct Op {
    char type;
    int pos;
    bool visited;
};

int get_next_pos(char type, vector<Op>& op) {
    for (int i = 0; i < sz(op); ++i) {
        if (type == op[i].type && op[i].visited == false) {
            return op[i].pos;
        }
    }
    return 0;
}

int solve() {
    int n; cin >> n;
    vector<Op> op(n);
    for (int i = 0; i < n; ++i) {
        cin >> op[i].type >> op[i].pos;
        op[i].visited = false;
    }
    int o_pos = 1, b_pos = 1, ret = 0;
    for (int c = 0; c < n; ++c) {
        Op& cur = op[c];
        int* p_main;
        int* p_sub;
        char sub_type;
        if (cur.type == 'O') {
            p_main = &o_pos;
            p_sub  = &b_pos;
            sub_type = 'B';
        } else {
            p_main = &b_pos;
            p_sub  = &o_pos;
            sub_type = 'O';
        }
        int movable  = abs(*p_main - cur.pos) + 1;
        int sub_dist = get_next_pos(sub_type, op) - *p_sub;
        int sub_move = min(abs(sub_dist), movable);
        if (sub_dist < 0) {
            sub_move = -sub_move;
        }         
        *p_main = cur.pos;
        *p_sub += sub_move;
        ret += movable;
        cur.visited = true;
    }
    return ret;
}

main() {
    ios_base::sync_with_stdio(false);

    int T; cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        cout << "Case #" << testcase << ": " << solve() << '\r' << endl;
    }
}
