#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

char trans[256];

void predo() {
    string Q[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string A[3] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};

    for (int k = 0; k < 3; k++)
        for (int i = 0; i < Q[k].length(); i++)
            trans[Q[k][i]] = A[k][i];
    trans['q'] = 'z';
    trans['z'] = 'q';
    trans[' '] = ' ';
    /*for (int i = 'a'; i <= 'z'; i++)
        printf("%c -> %c\n", i, trans[i]);*/
}

void solve() {
    string input;
    getline(cin, input);
    for (int i = 0; i < input.length(); i++)
        printf("%c", trans[input[i]]);
    puts("");
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    predo();
    int testN;
    scanf("%d", &testN); char buf[10]; gets(buf);
    for (int i = 1; i <= testN; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
