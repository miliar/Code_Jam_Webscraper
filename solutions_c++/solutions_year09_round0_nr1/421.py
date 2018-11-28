
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int L, D, N;
    cin >> L >> D >> N;
    vector <string> word(D);
    for (int i = 0; i < D; ++i)
        cin >> word[i];
    int tst;
    tst = N;
    for (int cas = 0; cas < tst; ++cas) {
        string pattern;
        cin >> pattern;
        vector <int> letters;
        for (int i = 0; i < (int)pattern.size(); ++i)
            if (isalpha(pattern[i]))
                letters.push_back(1 << (pattern[i] - 'a'));
            else {
                int j = i + 1;
                int set = 0;
                while (j < (int)pattern.size() && isalpha(pattern[j])) {
                    set |= 1 << (pattern[j] - 'a');
                    ++j;
                }
                letters.push_back(set);
                i = j;
            }
        int res = 0;
        for (int i = 0; i < D; ++i)
            if ((int)letters.size() == L) {
                bool ok = true;
                for (int j = 0; j < L; ++j)
                    if ((letters[j] & (1 << (word[i][j] - 'a'))) == 0) {
                        ok = false;
                        break;
                    }
                if (ok)
                    ++res;
            }
        cout << "Case #" << cas + 1 << ": " << res << endl;
    }
    return 0;
}