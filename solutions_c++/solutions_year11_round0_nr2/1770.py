#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int SIZE = 50;

char Cb[SIZE][SIZE];
bool Op[SIZE][SIZE];
int nTests;

string GetString(int len) {
    string res;
    char ch;
    do ch = getchar(); while (ch == ' ');
    for (int i = 0; i < len; i++) {
        res += ch;
        ch = getchar();
    }
    return res;
}

bool Check(char ch) {
    return 'A' <= ch && ch <= 'Z';
}

int main() {
    freopen("EXAMPLE.INP", "r", stdin);
    freopen("B.OUT", "w", stdout);
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; t++) {
        int c; scanf("%d", &c);
        memset(Cb, ' ', sizeof(Cb));
        for (int i = 0; i < c; i++) {
            string s = GetString(3);
            Cb[s[0] - 'A'][s[1] - 'A'] =
            Cb[s[1] - 'A'][s[0] - 'A'] = s[2];
        }

        int d; scanf("%d", &d);
        memset(Op, false, sizeof(Op));
        for (int i = 0; i < d; i++) {
            string s = GetString(2);
            Op[s[0] - 'A'][s[1] - 'A'] =
            Op[s[1] - 'A'][s[0] - 'A'] = true;
        }

        int n; scanf("%d", &n);
        string S = GetString(n);
        vector <char> res(1, S[0]);

        for (int i = 1; i < n; i++) {
            if (res.size() > 0 && Check(res.back())
                && Cb[S[i] - 'A'][res.back() - 'A'] != ' ')
                res[res.size() - 1] = Cb[S[i] - 'A'][res.back() - 'A'];
            else {
                bool check = false;
                for (int j = 0; j < res.size(); j++)
                    if (Check(res[j]) && Op[S[i] - 'A'][res[j] - 'A']) {
                        check = true;
                        break;
                    }
                if (check) res.clear();
                else res.push_back(S[i]);
            }
        }

        printf("Case #%d: [", t);
        if (res.size() > 0) {
            for (int i = 0; i < res.size() - 1; i++)
                printf("%c, ", res[i]);
            printf("%c]", res.back());
        }
        else printf("]");
        if (t < nTests) printf("\n");
    }
}
