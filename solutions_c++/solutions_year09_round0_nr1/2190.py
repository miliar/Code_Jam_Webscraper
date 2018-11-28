#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int L, D, N;
string Line[10000];
string token[10000];

void read() {
    cin >> L >> D >> N;
    for (int i = 0; i < D; i ++) cin >> Line[i];
}

void work() {
    string tmp;
    int k;
    bool flag;
    for (int i = 0; i < N; i ++) {
        cin >> tmp;
        k = 0;
        flag = 0;
        for (int j = 0; j < tmp.length(); j ++) {
            if (tmp[j] == '(') {
                flag = 1;
                token[k] = "";
            } else if (tmp[j] == ')') {
                k ++;
                flag = 0;
            } else {
                if (flag) token[k] += tmp[j]; else token[k ++] = tmp[j];
            }
        }

        int count = 0;
        bool ok;
        for (int p = 0; p < D; p ++) {
            ok = 1;
            for (int l = 0; l < L; l ++)
                if (token[l].find(Line[p][l]) == string::npos) {
                    ok = 0;
                    break;
                }
            if (ok) count ++;
        }
        cout << "Case #" << i + 1 << ": " << count << endl;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    read();
    work();
    fclose(stdin);
    fclose(stdout);
    return 0;
}
