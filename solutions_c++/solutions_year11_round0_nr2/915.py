#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

#define Fill(A, n) memset(A, n, sizeof(A))
string FILENAME = "B-large";

const int MAX_C = 36;
const int MAX_D = 28;

int C, D, N;
string combine[MAX_C], oppose[MAX_D];

char inCombine(char x, char y) {
    for (int i = 0; i < C; i++)
        if (combine[i][0] == x && combine[i][1] == y
                || combine[i][0] == y && combine[i][1] == x) return combine[i][2];
    return 0;
}

bool inOppose(char x, char y) {
    for (int i = 0; i < D; i++)
        if (oppose[i][0] == x && oppose[i][1] == y
                || oppose[i][0] == y && oppose[i][1] == x) return true;
    return false;
}

int main() {
    freopen((FILENAME + ".in").c_str(), "r", stdin);
    freopen((FILENAME + ".out").c_str(), "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d", &C);
        for (int i = 0; i < C; i++)
            cin >> combine[i];

        scanf("%d", &D);
        for (int i = 0; i < D; i++)
            cin >> oppose[i];

        scanf("%d", &N);
        string S;
        cin >> S;

        string Q = "";
        for (int i = 0; i < N; i++) {
            char c;
            if (c = inCombine(S[i], Q[Q.size()-1])) {
                Q[Q.size() - 1] = c;
                continue;
            }
            Q += S[i];
            for (int b = Q.size() - 1; b >= 0; b--)
                if (inOppose(Q[b], Q[Q.size() - 1])) {
                    Q = "";
                    break;
                }
        }

        printf("Case #%d: [", t + 1);
        for (int i = 0; i < Q.size(); i++) {
            if (i) cout << ", ";
            cout << Q[i];
        }
        cout << "]" << endl;
    }

}