#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct PB {
    int id;
    int t;
};

int T,N;
vector<PB> seq;

void init() {
    cin >> N;
    seq.clear();
    for( int i = 0; i < N; i++ ) {
        char r;
        int t;
        cin >> r >> t;
        PB tmp;
        if( r == 'O' ) {
            tmp.id = 0;
            tmp.t = t;
        }
        else {
            tmp.id = 1;
            tmp.t = t;
        }
        seq.push_back(tmp);
    }
}

void solve(int tc) {
    int pos[2],st[2];
    pos[0] = 1, pos[1] = 1;
    st[0] = 0, st[1] = 0;
    int ret = 0;
    for( int j = 0; j < seq.size(); j++ ) {
        int id = seq[j].id;
        if( pos[id] == seq[j].t ) ret += 1;
        else {
            int need = abs(pos[id]-seq[j].t);
            if( ret - st[id] >= need ) {
                ret += 1;
            }
            else {
                ret = need + st[id]+1;
            }
            pos[id] = seq[j].t;
        }
        st[id] = ret;
    }
    printf("Case #%d: %d\n", tc, ret);
}

int main() {
    cin >> T;
    for( int k = 0; k < T; k++ ) {
        init();
        solve(k+1);
    }
    system("pause");
    return 0;
}
