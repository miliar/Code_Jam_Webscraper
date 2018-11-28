#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

const int maxn = 100 + 5;
const int maxm = 100000 + 5;

struct Unit {
    long long x, y;

    Unit(long long x = 0, long long y = 0): x(x), y(y) {}
    inline bool operator< (const Unit& a) const {
        return y > a.y;
    }
};

long long dist[maxm];
long long make[maxm];
int B[maxn];

int main() {
//    freopen("B.in", "r", stdin); freopen("B.out", "w", stdout);
//    freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
//    freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout); 
//    freopen("B-small-attempt2.in", "r", stdin); freopen("B-small-attempt2.out", "w", stdout);
//    freopen("B-small-attempt3.in", "r", stdin); freopen("B-small-attempt3.out", "w", stdout);
    freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
    int T, test = 1;
    long long res;

    for(cin >> T; T; T --) {
        int n, M = 0;
        long long L;

        cin >> L >> n;
        for(int i = 0; i < n; i ++) {
            cin >> B[i];
            M = max(M, B[i]);
        }
        memset(dist, -1, sizeof(dist));
        priority_queue <Unit> que;
        que.push(Unit(0LL, 0LL));
        dist[0] = make[0] = 0;
        while(!que.empty()) {
            Unit opt = que.top();
            que.pop();

            if(opt.x > L) continue;
            if(opt.y > dist[opt.x % M]) continue;
            for(int i = 0; i < n; i ++) {
                long long Next = opt.x + B[i];
                if(Next > L) continue;
                if(dist[Next % M] == -1 || dist[Next % M] > opt.y + opt.x / M + 1 - Next / M) {
                    dist[Next % M] = opt.y + opt.x / M + 1 - Next / M;
                    make[Next % M] = Next;
                    que.push(Unit(Next, dist[Next % M]));
                }
            }
        }
        cout << "Case #" << test ++ << ": ";
        if(dist[L % M] == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << dist[L % M] + make[L % M] / M + (L - make[L % M]) / M << endl;
    } 
    return 0;
}

