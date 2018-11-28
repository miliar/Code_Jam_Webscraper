#include <iostream>

const int MAX_N = 100;
const int MAX_M = 255;
const int INF = 100000000;
int A[MAX_N], D, I, M, N;

using namespace std;

void ReadData() {
    cin >> D >> I >> M >> N;
    for (int i = 0; i < N; ++i)
        cin >> A[i];
}

int Abs(int a) {
    return a >= 0 ? a : -a;
}

bool IsSmooth(int a, int b) {
    return Abs(a - b) <= M;
}

int Insert(int a, int b) {
    if (IsSmooth(a, b))
        return 0;
    if (M == 0)
        return INF;
    int diff = Abs(a - b);
    return ((diff + M - 1) / M - 1) * I;
}

bool IsSmooth(int a, int b, int c) {
    return IsSmooth(a, b) && IsSmooth(b, c);
}

int MinCost(int a, int b) {
    int res = Insert(a, b);
    res = min(res, D);
    for (int a1 = 0; a1 <= MAX_M; ++a1)
        for (int b1 = 0; b1 <= MAX_M; ++b1)
            res = min(res, Abs(a1 - a) + Abs(b1 - b) + Insert(a1, b1));
    return res;
}

int MinCost(int a, int b, int c) {
    int res = min(D + MinCost(a, b),  MinCost(b, c) + D);
    res = min(res, Insert(a, b) + Insert(b, c));
    res = min(res, MinCost(a, c) + D);
    res = min(res, D * 2);
    for (int a1 = 0; a1 <= MAX_M; ++a1) {
        for (int b1 = 0; b1 <= MAX_M; ++b1) {
            for (int c1 = 0; c1 <= MAX_M; ++c1) {
                res = min(res, Abs(a1 - a) + Abs(b1 - b) + Abs(c1 - c) + Insert(a1, b1) + Insert(b1, c1));
                if (res == 0)
                    return res;
            }
        }
    }
    return res;
}

int Work() {
    if (N == 1)
        return 0;
    if (N == 2)
        return MinCost(A[0], A[1]);
    return MinCost(A[0], A[1], A[2]);
}

void Output(int t, int res) {
    cout << "Case #" << t << ": " << res << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        ReadData();
        Output(i, Work());
    }
    return 0;
}

