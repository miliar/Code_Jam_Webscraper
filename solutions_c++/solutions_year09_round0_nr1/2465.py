#include <iostream>
#include <string>

#define MAXLEN 256

using namespace std;

bool patMatch(char *pat, char *word) {
    bool g = false;
    int pp, pw;

    pp = 0;
    pw = 0;

    while(pat[pp] && word[pw]) {
        //cout << "testing: pat: " << pat[pp] << "; word: " << word[pw] << endl;
        if(pat[pp] == '(') {
            g = true;
            pp++;
        } else if(pat[pp] == ')') {
            return false;
        } else {
            if(word[pw] == pat[pp]) {
                pp++;
                pw++;
                if(g) {
                    while(pat[pp] != ')') {
                        pp++;
                        //cout << pat[pp];
                        //cout << pp;
                    }
                    pp++;
                    g = false;
                }
            } else {
                if(!g) {
                    return false;
                } else {
                    pp++;
                }
            }
        }
    }

    return true;
}

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int l, d, n;
    int i, j;
    int cnt;

    cin >> l >> d >> n;

    char words[d][l + 1];
    char cases[n][MAXLEN];

    for(i = 0; i < d; i++) {
        cin >> words[i];
        //cout << words[i] << endl;
    }

    for(i = 0; i < n; i++) {
        cin >> cases[i];
        //cout << cases[i] << endl;
        cnt = 0;
        for(j = 0; j < d; j++) {
            //cout << "PATMATCH: " << cases[i] << ", " << words[j] << endl;
            if(patMatch(cases[i], words[j])) {
                cnt++;
            }
        }
        cout << "Case #" << (i + 1) << ": " << cnt << endl;
    }

    return 0;
}
