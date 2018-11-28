#include <fstream>
using namespace std;

const int INF = 1000000000;

ifstream in("A.in");
ofstream out("A.out");

int N, V;
int G[10005], C[10005];
int cmin[10005][2];

void solve() {
    for(int i = N; i >= 1; --i)
        if(2 * i > N)
            if(!G[i])
                cmin[i][0] = 0, cmin[i][1] = INF;
            else
                cmin[i][0] = INF, cmin[i][1] = 0;
        else {
            if(G[i] == 0) { // OR
                cmin[i][0] = min(INF, cmin[2 * i][0] + cmin[2 * i + 1][0]);
                cmin[i][1] = INF;
                cmin[i][1] = min(cmin[i][1], cmin[2 * i][0] + cmin[2 * i + 1][1]);
                cmin[i][1] = min(cmin[i][1], cmin[2 * i][1] + cmin[2 * i + 1][0]);
                cmin[i][1] = min(cmin[i][1], cmin[2 * i][1] + cmin[2 * i + 1][1]);
            }
            else { // AND
                cmin[i][0] = INF;
                cmin[i][0] = min(cmin[i][0], cmin[2 * i][0] + cmin[2 * i + 1][0]);
                cmin[i][0] = min(cmin[i][0], cmin[2 * i][0] + cmin[2 * i + 1][1]);
                cmin[i][0] = min(cmin[i][0], cmin[2 * i][1] + cmin[2 * i + 1][0]);
                cmin[i][1] = min(INF, cmin[2 * i][1] + cmin[2 * i + 1][1]);
            }
            if(C[i]) {
                G[i] = !G[i];
                if(G[i] == 0) { // OR
                    cmin[i][0] = min(cmin[i][0], cmin[2 * i][0] + cmin[2 * i + 1][0] + 1);
                    cmin[i][1] = min(cmin[i][1], cmin[2 * i][0] + cmin[2 * i + 1][1] + 1);
                    cmin[i][1] = min(cmin[i][1], cmin[2 * i][1] + cmin[2 * i + 1][0] + 1);
                    cmin[i][1] = min(cmin[i][1], cmin[2 * i][1] + cmin[2 * i + 1][1] + 1);
                }
                else { // AND
                    cmin[i][0] = min(cmin[i][0], cmin[2 * i][0] + cmin[2 * i + 1][0] + 1);
                    cmin[i][0] = min(cmin[i][0], cmin[2 * i][0] + cmin[2 * i + 1][1] + 1);
                    cmin[i][0] = min(cmin[i][0], cmin[2 * i][1] + cmin[2 * i + 1][0] + 1);
                    cmin[i][1] = min(cmin[i][1], cmin[2 * i][1] + cmin[2 * i + 1][1]);
                }
            }
        }
}


int main() {
    int T;
    in >> T;
    for(int i = 1; i <= T; ++i) {
        in >> N >> V;
        for(int j = 1; j <= N; ++j) {
            in >> G[j];
            if(j <= (N - 1) / 2)
                in >> C[j];
        }
        solve();
        out << "Case #" << i << ": ";
        if(cmin[1][V] == INF)
            out << "IMPOSSIBLE";
        else
            out << cmin[1][V];
        if(i < T)
            out << "\n";
    }
    return 0;
}
