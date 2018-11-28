#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

const string W = "welcome to code jam";

int data[2][1000];

int main() {
    string sn; getline(cin, sn);
    int n = atoi(sn.c_str());
    for (int i = 1; i <= n; i++) {
        string s; getline(cin, s);

        cout << "Case #" << i << ": ";
        int len = s.size();
        int curr = 0, next = 1;
        for (int j = 0; j < len; j++) data[curr][j] = 1;
        for (int j = W.size()-1; j >= 0; j--) {
            char comp = W[j];
            int acc = 0;
            for (int k = s.size()-1; k >= 0; k--) {
                data[next][k] = acc;
                if (comp == s[k]) {
                    data[next][k] += data[curr][k];
                    if (data[next][k] >= 10000) data[next][k] -= 10000;
                }
                acc = data[next][k];
            }
            curr = 1-curr; next = 1-next;
        }
        printf("%04d\n", data[curr][0]);
    }
    return 0;
}

