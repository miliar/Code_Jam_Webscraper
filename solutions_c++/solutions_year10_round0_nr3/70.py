#include<iostream>
#include<cstdio>
#include<utility>

using namespace std;

struct node {
    long long size;
    int index;
    long long total;

    node() : index(-1) {}
};

pair<int, long long> f(const node* g, int i, int n, long long k) {
    int j = i;
    long long income = 0;
    for(;j < n + i; j++) {
        if(income + g[j % n].size <= k) income += g[j % n].size;
        else break;
    }
    return make_pair(j % n, income);
}

int main() {
    long long T, r, k, n;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        node g[1000];
        cin >> r >> k >> n;
        for(int i = 0; i < n; i++) cin >> g[i].size;

        long long total = 0;
        for(int i = 0, j = 0; i < r;) {
            if(g[j].index == -1) {
                g[j].index = i;
                pair<int, long long> p = f(g, j, n, k);
                g[j].total = total;
                total += p.second;
                j = p.first;
                i++;
            }
            else {
                int cycle_len = i - g[j].index;
                long long income = total - g[j].total;
                int round = (r - i) / cycle_len;
                i += cycle_len * round;
                total += income * round;
                for(int i = 0; i < n; i++) g[i].index = -1;
            }
        }

        cout << "Case #" << t << ": " << total << endl;
    }
}

