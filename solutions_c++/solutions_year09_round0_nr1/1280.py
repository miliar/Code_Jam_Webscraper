#include <iostream>
#include <string>
using namespace std;

string a[5100];
int b[16][26];
int L, D, N;

int ok(string &s) {
    memset(b, 0, sizeof(b));
    int t = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '(') {
           int j = i + 1;
           while(s[j] != ')') {
                      b[t][s[j]-'a']=1;
                      j++;
           }
           i = j;
        } else {
           b[t][s[i]-'a']=1;
        }
        t++;
    }
    int ret = 0;
    for (int i = 0; i < D; ++i) {
        int f = 1;
        for (int j = 0; j < L && f; ++j) {
            if (!b[j][a[i][j]-'a']) f = 0;
        }
        if (f) ret++;
    }
    return ret;
}
int main() {
    cin >> L >> D >> N;
    for (int i = 0; i <D; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < N; ++i) {
        cout << "Case #" << i + 1 << ": ";
        int ret = 0;
        string s;
        cin >> s;
        cout << ok(s) << endl;
    }
    return 0;
}
     
