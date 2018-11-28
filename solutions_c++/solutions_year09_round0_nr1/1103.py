#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <cmath>

using namespace std;

const int alf = 27;

class node {
    public:

        int w[alf];
        int ile;

        node() {
            for (int i=0;i<alf;++i)
                w[i] = -1;
            ile = 0;
        }
};

vector<node> tree;

void create() {
    tree.clear();
    tree.push_back( node() );
}

void add(char *s, int l) {
    int iter = 0;
    for (int i=0;i<l;++i) {
        int akt = s[i] - 'a';
        if (tree[iter].w[akt] == -1) {
            tree.push_back( node() );
            int newiter = tree.size() - 1;
            tree[iter].w[akt] = newiter;
            iter = newiter;
        } else {
            iter = tree[iter].w[akt];
        }
    }
    tree[iter].ile++;
}

int bfs(char *s, int it, int f, int l) {
    char c = *s;
    if (c != '(') {
        int czym = *s - 'a';
        int gdzie = tree[it].w[czym];
        if (gdzie == -1)
            return 0;
        it = gdzie;
        if (f == l)
            return tree[it].ile;
        return bfs(s+1, it, f+1, l);
    } else {
        s++;
        int res = 0;
        char *ns = s;
        while (*ns != ')')
            ns++;
        ns++;
        while (*s!=')') {
            int czym = *s++ - 'a';
            int gdzie = tree[it].w[czym];
            if (gdzie == -1)
                continue;
            if (f==l)
                res += tree[gdzie].ile;
            else
                res += bfs(ns, gdzie, f+1, l);
        }
        return res;
    }
    return 0;
}

int main() {
    int n, m, q;
    scanf("%d%d%d",&n,&m,&q);
    char tekst[5000];
    create();
    while (m--) {
        scanf("%s",tekst);
        add(tekst, n);
    }

    for (int it=1;it<=q;++it) {
        scanf("%s",tekst);
        int res = bfs(tekst, 0, 1, n);
        printf("Case #%d: %d\n",it, res);
    }
}
