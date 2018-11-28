#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"

using namespace std;

int ind(char be) {
    switch (be) {
        case 'A': return 0;
        case 'D': return 1;
        case 'E': return 2;
        case 'F': return 3;
        case 'Q': return 4;
        case 'R': return 5;
        case 'S': return 6;
        case 'W': return 7;
    }
}

int main() {
    //                 A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
    int is_base[26] = {1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0};
    int T; scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        fprintf(stderr, "Case #%d of %d...\n", Ti, T);

        char comb[8][8];
        bool opp[8][8];
        for (int i = 0; i < 8; ++i)
            for (int j = 0; j < 8; ++j)
                comb[i][j] = '\0';
        for (int i = 0; i < 8; ++i)
            for (int j = 0; j < 8; ++j)
                opp[i][j] = false;

        int C; scanf("%d ", &C);
        for (int i = 1; i <= C; ++i) {
            char a, b, c;
            scanf("%c%c%c ", &a, &b, &c);
            comb[ind(a)][ind(b)] = c;
            comb[ind(b)][ind(a)] = c;
        }

        int D; scanf("%d ", &D);
        for (int i = 1; i <= D; ++i) {
            char a, b;
            scanf("%c%c ", &a, &b);
            opp[ind(a)][ind(b)] = true;
            opp[ind(b)][ind(a)] = true;
        }

        string el_to_invoke;
        int N; scanf("%d ", &N);
        for (int i = 1; i <= N; ++i) {
            char a;
            scanf("%c", &a);
            el_to_invoke.push_back(a);
        }

        string result;
        for (int i = 0; i < N; ++i) {
            char c = el_to_invoke[i];
            if (result.size() == 0) {
                result.push_back(el_to_invoke[i]);
                continue;
            }
            char c_prev = result[result.size()-1];
            bool is_opp = false;
            bool combined = false;

            if (is_base[c_prev-'A']) {
                char rep = comb[ind(c)][ind(c_prev)];
                if (rep != '\0') {
                    result[result.size()-1] = rep;
                    combined = true;
                }
            }

            if (not combined) {
                for (int j = 0; j < result.size(); ++j) {
                    if (is_base[result[j]-'A'] && opp[ind(c)][ind(result[j])]) {
                        is_opp = true;
                        break;
                    }
                }
                if (is_opp) {
                    result.clear();
                } else {
                    result.push_back(c);
                }
            }
        }

        cout << "Case #" << Ti << ": [";
        for (int i = 0; i < result.size(); ++i) {
            cout << result[i];
            if (i != result.size()-1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    return 0;
}

