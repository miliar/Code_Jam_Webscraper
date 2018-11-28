#include <cstdio>
#include <string>
#include <cstring>
#include <cctype>
#include <set>
#include <vector>
#include <iostream>
#include <sstream>
using namespace std;

struct Tree {
    Tree *sub[26];
    Tree() { for (int i = 0; i < 26; ++i) sub[i] = NULL; }
    void insert(char *s) {
        if (*s != '\0') {
            int idx = *s - 'a';
            if (sub[idx] == NULL) sub[idx] = new Tree();
            sub[idx]->insert(s + 1);
        }
    }
};

int go(vector<string>& pattern, int idx, Tree* tree) {
    if (tree == NULL) return 0;
    if (idx == pattern.size()) return 1;
    int count = 0;
    for (int i = 0; i < pattern[idx].size(); ++i) {
        count += go(pattern, idx + 1, tree->sub[pattern[idx][i]-'a']);
    }
    return count;
}

int main() {
    int L, D, N;
    Tree tree;

    scanf("%d %d %d", &L, &D, &N);

    for (int i = 0; i < D; ++i) {
        char w[L+10];
        scanf("%s", w);
        tree.insert(w);
    }

    for (int c = 0; c < N; ++c) {
        vector<string> pattern;
        char p[1000];
        scanf("%s", p);

        for (int i = 0, len = strlen(p); i < len; ++i) {
            if (p[i] == '(') {
                string s;
                while (p[++i] != ')') s += p[i];
                pattern.push_back(s);
            } else {
                string s; s = p[i];
                pattern.push_back(s);
            }
        }

        printf("Case #%d: %d\n", c + 1, go(pattern, 0, &tree));
    }

    return 0;
}
