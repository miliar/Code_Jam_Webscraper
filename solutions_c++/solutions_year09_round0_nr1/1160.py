#include <iostream>
#include <string>
using namespace std;

int L,D,N;
string word[5005];
bool pattern[20][30];
int X,K;

bool match(int w);

int main() {
    char c;

    cin >> L >> D >> N;
    for (int i = 0; i < D; i++)
        cin >> word[i];

    for (X = 1; X <= N; X++) {
        for (int i = 0; i < L; i++)
            for (int j = 0; j < 26; j++)
                pattern[i][j] = false;

        for (int i = 0; i < L; i++) {
            cin >> c;
            if (c == '(')
                while (true) {
                    cin >> c;
                    if (c == ')')
                        break;
                    pattern[i][c-'a'] = true;
                }
            else
                pattern[i][c-'a'] = true;
        }

        K = 0;
        for (int i = 0; i < D; i++)
            if (match(i))
                K++;
        cout << "Case #" << X << ": " << K << endl;
    }

    return 0;
}

bool match(int w) {
    for (int i = 0; i < L; i++)
        if (!pattern[i][word[w][i]-'a'])
            return false;
    return true;
}
