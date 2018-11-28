#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
#include <vector>
#include <string.h>
using namespace std;

struct nn {
    map<string, nn*> next;
}mem[1000000], *pp, *root;

int T, n, m;
int res;

void process(char *str) {
    nn *p = root;
    int i = 0;
    char *token = strtok(str, "/");
    while (token) {
        if (p->next.find(string(token)) == p->next.end()) {
            p->next[string(token)] = pp++;
            p->next[string(token)]->next.clear();
            res++;
        }
        p = p->next[string(token)];
        token = strtok(NULL, "/");
    }
}


int main() {
    char str[1000];
    scanf("%d", &T);
    int c, i;
    for (c = 1; c <= T; c++) {
        scanf("%d%d", &n, &m);
        root = mem;
        root->next.clear();
        pp = mem + 1;
        for (i = 0; i < n; i++) {
            scanf("%s", str);
            process(str);
        }
        res = 0;
        for (i = 0; i < m; i++) {
            scanf("%s", str);
            process(str);
        }
        printf("Case #%d: %d\n", c, res);
    }
    return 0;
}
