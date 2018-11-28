#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main()
{
    int L, D, N;
    cin >> L >> D >> N;
    cin.get();

    string W[5000];
    for (int i = 0; i < D; i++) {
        string temp;
        getline(cin, temp);
        W[i] = temp;
    }

    int C[500];
    for (int i = 0; i < N; i++) {
        string P;
        getline(cin, P);
        int pos = 0;
        string patterns[15];
        for (int j = 0; j < L; j++) {
            string p = "";
            if (P[pos] == '(') {
                pos++;
                while (P[pos] >= 'a' && P[pos] <= 'z') {
                    p = p + P[pos];
                    pos++;
                }
            } else {
                p = p + P[pos];
                pos++;
            }
            if (P[pos] == ')') pos++;
            patterns[j] = p;
        }

        C[i] = 0;
        for (int j = 0; j < D; j++) {
            bool match = true;
            for (int k = 0; k < L; k++) {
                if (patterns[k].find(W[j][k]) == string::npos) {
                    match = false;
                    break;
                }
            }
            if (match)
                C[i]++;
        }
    }

    for (int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": " << C[i] << endl;
    }

    return 0;
}
