#include <iostream>
#include <string>
#include <set>
using namespace std;

int tree[151000][30];
int tot = 0;
int l, d, n;

int getid(char c) {
    return c-'a';
}
void build() {
    char word[100];
    scanf("%s", word);
//    printf("word: %s\n", word);
    int p = 0;
    int len = strlen(word);
    for(int i=0; i<len; i++) {
        if(tree[p][getid(word[i])] == 0) {
            tree[p][getid(word[i])] = ++tot;
        }
//        printf("%d ", p);
        p = tree[p][getid(word[i])];
    }
//        printf("%d \n", p);
}

int qq[10000];
int h, t;
void ptree() {
    h = t = 0;
    qq[t++] = 0;
    while(h<t) {
        printf("%d ", qq[h]);
        for(int i=0; i<26; i++) if(tree[qq[h]][i]) qq[t++] = tree[qq[h]][i];
        h ++;
    }
}
char pattern[3000];
int p;
char sp[30];
int lsp;

bool getsp() {
    lsp = 0;
    if(pattern[p] == '(') {
        p++;
        while(pattern[p]!=')') {
            sp[lsp++] = pattern[p++];
        }
        p++;
    }
    else {
        sp[lsp++] = pattern[p++];
    }
}

set<int> que[2];
set<int>::iterator sit;
int size[2];
int from=0, to=1;

int solve() {
    int i, j;
    scanf("%s", pattern);
    p = 0;
    que[from].clear();
    que[to].clear();
    size[to] = 0;
    size[from] = 1;
    que[from].insert(0);
    for(i=0; i<l; i++) {
        getsp();
        que[to].clear();
        for(sit = que[from].begin(); sit!=que[from].end(); sit++) {
            for(j=0; j<lsp; j++) {
                int tt = tree[*sit][getid(sp[j])];
//                printf("tt: %d\n", tt);
                if(tt) {
                    que[to].insert(tt);
                }
            }
        }
//        printf("size(%d): %d\n", i, que[to].size());
        from = 1 - from;
        to = 1 - to;
    }
    return que[from].size();
}
int main() {
    int i;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d%d%d", &l, &d, &n);
    for(i=0; i<d; i++) {
        build();
    }
//    ptree();
    for(i=0; i<n; i++) {
        printf("Case #%d: %d\n", i+1, solve());
    }
//    while(1);
    return 0;
}
