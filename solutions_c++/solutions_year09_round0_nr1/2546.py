#include <iostream>
#include <set>

using namespace std;

struct word {
    word() {
        for (int i = 0; i < 26; i++) {
            next[i] = NULL;
        }
    }
    struct word * next[26];
};

struct word root;

int many(string p, struct word *x, int len) {
    int total = 0;

    if (len == 0) return 1;

    if (p[0] == '(') {
        int j = 0;
        while (p[j] != ')') j++;
        for (int k = 1; k < j; k++) {
            int c = p[k] - 'a';

            if (x->next[c] != NULL) {
                total += many(p.substr(j+1), x->next[c], len-1);
            }
        }
    } else {
        int c = p[0] - 'a';

        if (x->next[c] != NULL) {
            total += many(p.substr(1), x->next[c], len-1);
        }
    }

    return total;
}

int main() {
    int wordsc;
    int patterns;
    int len;

    cin >> len >> wordsc >> patterns;

    for (int i = 0; i < wordsc; i++) {
        string w;
        cin >> w;

        struct word *x = &root;
        for (unsigned int j = 0; j < w.length(); j++) {
            int c = w[j] - 'a';

            if (x->next[c] == NULL) {
                x->next[c] = new word;
            }
            x = x->next[c];
        }
    }

    for (int i = 0; i < patterns; i++) {
        string p;
        cin >> p;

        printf("Case #%d: %d\n", i+1, many(p, &root, len));
    }

    return 0;
}
