#include <iostream>
using namespace std;

long long n, A, B, C, D, x0, y0, M;
long long cnt[9];

void add(long long X, long long Y) {
    cnt[X % 3 * 3 + Y % 3]++;
}

bool valid(int x1, int y1, int x2, int y2, int x3, int y3) {
    return (x1 + x2 + x3) % 3 == 0 && (y1 + y2 + y3) % 3 == 0;
}

long long count() {
    long long C = 0;
    for(int i = 0; i < 9; ++i)
        for(int j = i; j < 9; ++j)
            for(int k = j; k < 9; ++k)
                if(valid(i / 3, i % 3, j / 3, j % 3, k / 3, k % 3))
                    if(i == j)
                        if(j == k)
                            C += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) / 6;
                        else
                            C += cnt[i] * (cnt[i] - 1) * cnt[k] / 2;
                    else
                        if(j == k)
                            C += cnt[i] * cnt[j] * (cnt[j] - 1) / 2;
                        else
                            C += cnt[i] * cnt[j] * cnt[k];
    return C;
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        memset(cnt, 0, sizeof(cnt));
        long long X = x0, Y = y0;
        add(X, Y);
        for(int k = 1; k < n; ++k) {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            add(X, Y);
        }
        cout << "Case #" << i << ": " << count();
        if(i < T)
            cout << "\n";
    }
    return 0;
}
