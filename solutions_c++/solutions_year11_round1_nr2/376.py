#include <cstdio>
#include <cassert>
#include <vector>
#include <string>
using namespace std;

int guesses(vector<string>& _, string answer, char seq[]) {
//    printf("\nCalled with ans=%s, seq=%s\n", answer.c_str(), seq);
    bool possible[_.size()];
    for (int i = 0; i < _.size(); i++) possible[i] = true;

    int left = _.size();
    int wrong = 0;
    for (int i = 0; i < 26; i++) {
//        printf("iteration %d(%c), left=%d\n", i+1, seq[i], left);
        if (left == 1)
            return wrong;

        char c = seq[i];
        int len = answer.length();
        bool revealed[15] = {};

        bool should_guess = false;
        for (int i = 0; i < _.size(); i++) {
            if (possible[i]) {
                if (_[i].find(c) != string::npos) {
//                    printf("Found %c in %s\n", c, _[i].c_str());
                    should_guess = true;
                }
            }
        }

        if (!should_guess) {
//            printf("Skipping %c\n", c);
            continue;
        }

        bool right=  0;
        for (int i = 0; i < len; i++) {
            if (answer[i] == c) {
                revealed[i] = true;
                right = 1;
            }
        }

        if (!right)
            wrong++;

        for (int i = 0; i < len; i++) {
            bool rev = revealed[i];
            for (int k = 0; k < (int)_.size(); k++) {
                if ( (_[k][i] == c) != rev ) {
                    left -= possible[k];
                    possible[k] = false;
                }
            }
        }
    }

    return wrong;
}

void solve_seq(vector<string>& words, char seq[]) {
    string best_word;
    int best = -1;

    for (int i = 0; i < (int)words.size(); i++) {
        vector<string> _;
        for (int k = 0; k < (int)words.size(); k++) {
            if (words[k].length() == words[i].length()) {
                _.push_back(words[k]);
            }
        }

        int cur = guesses(_, words[i], seq);
//        printf("Picking %s gets %d\n", words[i].c_str(), cur);
        if (cur > best) {
            best = cur;
            best_word = words[i];
        }
    }

    printf(" %s", best_word.c_str());
}

void solve() {
    int nw, ns;
    scanf("%d %d\n", &nw, &ns);

    vector<string> words;
    for (int i = 0; i < nw; i++) {
        char buf[20] = {};
        scanf("%s", buf);
        words.push_back(string(buf));
    }

    for (int i = 0; i < ns; i++) {
        char seq[30] = {};
        scanf("%s", seq);
        solve_seq(words, seq);
    }
    printf("\n");
}

int main() {
    int n;
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) {
        printf("Case #%d:", i+1);
        solve();
    }

    return 0;
}
