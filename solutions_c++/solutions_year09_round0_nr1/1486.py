#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int L, D, N;

vector<string> words;
vector<bitset<26> > pattern;

int let2num(char c) { return c - 'a'; }

int solve_one() {
    int i, k, sol = 0;
    char c;
    pattern.resize(L);
    for (i = 0; i < L; i++) {
        pattern[i].reset();
        cin >> c;
        if ('(' != c) {
            pattern[i][let2num(c)] = 1;
        } else {
            do {
                cin >> c;
                if (')' != c)
                    pattern[i][let2num(c)] = 1;
            } while(')' != c);
        }
    }
    for (i = 0; i < D; i++) {
        for (k = 0; k < L; k++)
            if (!pattern[k][let2num(words[i][k])]) {
                break;
            }
        if (k == L) {
            sol++;
        }
    }
    return sol;
}

int main(void)
{
    int i;
    cin >> L >> D >> N;
    words.resize(D);
    for (i = 0; i < D; i++)
        cin >> words[i];
    for (i = 1; i <= N; i++)
        cout << "Case #" << i << ": " << solve_one() << endl;
    return 0;
}
