#include <iostream>
#include <vector>
#include <cstdio>
#include <queue>

using namespace std;

struct node {
    int r, c;
    int t;
    node(int t = 0, int r = 0, int c = 0)
        : t(t)
        , r(r)
        , c(c)
    {
    }

    bool operator < (const node& other) const {
        return t > other.t;
    }
};

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void solve() {
    int H, N, M;
    cin >> H >> N >> M;
    vector< vector<int> > C(N, vector<int>(M)), F(N, vector<int>(M));
    int ans = 0;

    for (int i = 0; i < N; i++) for (int j = 0; j < M; j++)
        cin >> C[i][j];
    for (int i = 0; i < N; i++) for (int j = 0; j < M; j++)
        cin >> F[i][j];

    vector< vector<int> > leave(N, vector<int>(M));
    priority_queue<node> h;

    h.push(node(0, 0, 0));
    while (h.empty() == false) {
        node nd = h.top(); h.pop();
        int r = nd.r;
        int c = nd.c;
        if (leave[r][c]) continue;
        leave[r][c] = 1;
        int t = nd.t;

        if (r == N - 1 && c == M - 1) {
            ans = t;
            break;
        }

        for (int i = 0; i < 4; i++) {
            int r1 = r + dx[i];
            int c1 = c + dy[i];
            if (r1 >= 0 && r1 < N && c1 >= 0 && c1 < M) {
                int t1 = t;
                
                if (F[r][c] > C[r1][c1] - 50) continue;
                if (F[r1][c1] > C[r1][c1] - 50) continue;
                if (F[r1][c1] > C[r][c] - 50) continue;

                if (H - t > C[r1][c1] - 50) {
                    t1 += H - t + 50 - C[r1][c1];
                }

                int H1 = H - t1;
                int cost = 100;
                if (H1 >= 20 + F[r][c]) cost = 10;
                if (t1 == 0) cost = 0;

//                cerr << '\n' << H1 << ' ' << F[r][c] << endl;
//                cerr << t1 << ' ' << cost << ' ' << r1 << ' ' << c1 << endl;
                h.push(node(t1 + cost, r1, c1));
            }
        }
    }

    static int test = 0;
    cout << "Case #" << ++test << ": " << ans/10 << '.' << ans%10 << endl;    
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}
