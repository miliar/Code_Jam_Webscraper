#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

#define Fill(A, n) memset(A, n, sizeof(A))
string FILENAME = "D-large";

const int MAX_N = 1000;
int a[MAX_N];
bool visited[MAX_N];


int visit(int p) {
    visited[p] = true;
    if (!visited[a[p]]) return visit(a[p]) + 1;
    return 1;
}

int main() {
    freopen((FILENAME + ".in").c_str(), "r", stdin);
    freopen((FILENAME + ".out").c_str(), "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            scanf("%d", &a[i]);
            a[i]--;
        }

        double expectedSteps = 0;
        Fill(visited, false);
        for (int i = 0; i < N; i++)
            if (a[i] != i && !visited[i]) expectedSteps += visit(i);

        printf("Case #%d: %.6lf\n", t + 1, expectedSteps);
    }
}
