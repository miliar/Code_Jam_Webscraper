#include <iostream>
#include <vector>

void ReadData(int &R, int &K, std::vector<int> &G) {
    int n;
    std::cin >> R >> K >> n;
    for (int i = 0; i < n; ++i) {
        G.push_back(0);
        std::cin >> G[i];
    }
}

void Go(int p, int &np, long long &t, int k, const std::vector<int> &g) {
    for (t = 0, np = p; ;) {
        if (t != 0 && np == p)
            return;
        if (t + g[np] <= k) {
            t += g[np];
            np = (np + 1) % g.size();
        } else {
            return;
        }
    }
}

long long Work(int R, int K, const std::vector<int> &G) {
    std::vector<int> C;
    std::vector<long long> T;
    for (int i = G.size(); i > 0; --i) {
        C.push_back(-1);
        T.push_back(-1);
    }
    int s = 0, p = 0;
    C[p] = s;
    long long t = 0, pt;
    T[p] = t;
    for (; s != R;) {
        ++s;
        Go(p, p, pt, K, G);
        t += pt;
        if (C[p] != -1) {
           int q = (R - s) / (s - C[p]);
           s += (s - C[p]) * q;
           t += (t - T[p]) * q;
        }
        C[p] = s;
        T[p] = t;
    }
    return t;
}

void Output(int t, long long res) {
    std::cout << "Case #" << t << ": " << res << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        int R, K;
        std::vector<int> G;
        ReadData(R, K, G);
        Output(i, Work(R, K, G));
    }
    return 0;
}

