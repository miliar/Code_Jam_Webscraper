#include <cstdio>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#define LD long double

using namespace std;

class node {
    public:
    LD p;
    string f;
    int left;
    int right;
    node(){}
    node(LD _p, string _f) {
        p = _p;
        left = -1;
        right = -1;
        f = _f;
    }
};

vector<node*> tree;
char Tab[2048];

void readN(int *it) {
    char c = getchar();
    while (c!='(')
        c=getchar();
    LD p;
    scanf("%llf",&p);
    c=getchar();
    while (c!=')' && !(c>='a' && c<='z'))
        c = getchar();
    if (c == ')') {
        tree.push_back(new node(p, string()) );
        int w = tree.size()-1;
        *it = w;
    } else {
        string x;
        while (c>='a' && c<='z') {
            x.push_back(c);
            c = getchar();
        }
        tree.push_back(new node(p, x) );
        int w = tree.size()-1;
        *it = w;
        readN( &tree[w]->left );
        readN( &tree[w]->right );
        char c=getchar();
        while (c!=')')
            c=getchar();
    }

}

void createT() {
    int p;
    scanf("%d",&p);
    for (int i=0;i<tree.size();++i)
        delete tree[i];
    tree.clear();
    readN(&p);
}

set<string>feat;

LD simulate(int it, LD p) {
    p *= tree[it]->p;
    if (tree[it]->left == -1)
        return p;
    if (feat.find(tree[it]->f) != feat.end())
        return simulate(tree[it]->left, p);
    return simulate(tree[it]->right, p);
}

int main() {
    int lw;
    scanf("%d",&lw);
    for (int L=1;L<=lw;++L) {
        createT();
        int m;
        scanf("%d",&m);
        printf("Case #%d:\n",L);
        while (m--) {
            scanf("%s",Tab);
            int n;
            scanf("%d",&n);
            feat.clear();
            while (n--) {
                scanf("%s",Tab);
                string x = Tab;
                feat.insert(x);
            }
            LD p = simulate(0, 1.0);
            printf("%.7llf\n",p);
        }
    }
    
    return 0;
}
