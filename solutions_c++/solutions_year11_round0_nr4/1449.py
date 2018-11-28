#include <iostream>
#include <vector>

using namespace std;

double fact(double i) {
    if (i == 0)
        return 1.0;
    return i * fact(i - 1);
}

int perm_dfs(int curr, vector<int> &perm, vector<bool> &visited) {
    if (visited[curr]) return 0;
    visited[curr] = true;
    return 1 + perm_dfs(perm[curr], perm, visited);
}

int main() {
    int T; cin >> T;

    for (int t = 0; t < T; t++)
    {
        int N; cin >> N;
        vector<int> perm(N);
        for (int i = 0 ; i < N; i++) { cin >> perm[i]; perm[i]--; }
        vector<bool> visited(N, false);
        double ret = 0;
        while (true) {
            int next = -1;
            for (int i = 0; i < N; i++)
            {
                if (visited[i])
                    continue;
                if (perm[i] == i)
                    visited[i] = true;
                else
                {
                    next = i;
                    break;
                }
            }
            if (next == -1)
                break;
            ret += perm_dfs(next, perm, visited);
        }
        cout << "Case #" << t + 1 << ": " << ret << endl;
    }
}
