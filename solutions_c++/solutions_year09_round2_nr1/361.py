/**********************************************************************
Author: Felicia
Created Time:  2009/9/13 0:11:52
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

typedef long long int64;
const int maxint = 0x7FFFFFFF;
const int64 maxint64 = 0x7FFFFFFFFFFFFFFFLL;

struct node {
    double p;
    string prop;
    int lch;
    int rch;
    node() {}
    node(const double &_p, const string &_prop, const int &_lch, const int &_rch) :
        p(_p), prop(_prop), lch(_lch), rch(_rch) {}
};

vector <node> tree;

void skip() {
    int ch;
    while (ch = getchar()) {
        if (ch == ' ' || ch == '\n')
            continue;
        else {
            ungetc(ch, stdin);
            break;
        }
    }
}

int read_node() {
    int ret = tree.size();
    tree.push_back(node());
    skip();
    scanf("(");
    skip();
    scanf("%lf", &tree[ret].p);
    skip();
    char s[200];
    s[0] = getchar();
    s[1] = 0;
    if (s[0] == ')') {
        tree[ret].lch = -1;
        tree[ret].rch = -1;
        return ret;
    }
    scanf("%[^ \n()]", s + 1);
    tree[ret].prop = s;
    int r1 = read_node();
    int r2 = read_node();
    tree[ret].lch = r1;
    tree[ret].rch = r2;
    skip();
    scanf(")");
    skip();
    return ret;
}

void print_node(int now) {
    printf("(%lf %s", tree[now].p, tree[now].prop.c_str());
    printf("[%d][%d]", tree[now].lch, tree[now].rch);
    if (tree[now].lch != -1) {
        print_node(tree[now].lch);
        print_node(tree[now].rch);
    }
    printf(")");
}

set <string> aprop;

void travel_tree() {
    double p = 1;
    int now = 0;
    while (1) {
        p *= tree[now].p;
        if (tree[now].lch == -1)
            break;
        if (aprop.find(tree[now].prop) != aprop.end()) {
//            printf("l");
            now = tree[now].lch;
        } else {
//            printf("r");
            now = tree[now].rch;
        }
    }
//    printf("\n");
    printf("%.7lf\n", p);
}

int main() {
    freopen("a-large.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int T = 1; T <= ca; ++T) {
        tree.clear();
        printf("Case #%d:\n", T);
        scanf("%*d");
        read_node();
//        print_node(0);
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            int m;
            scanf("%*s%d", &m);
            aprop.clear();
            for (int j = 0; j < m; ++j) {
                char buf[100];
                scanf("%s", buf);
                aprop.insert(buf);
            }
            travel_tree();
        }
    }
    return 0;
}

