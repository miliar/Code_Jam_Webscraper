#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
#include <cfloat>
#include <cassert>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <complex>
#include <utility>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <valarray>
#include <algorithm>
#include <functional>
using namespace std;

typedef int i32;
typedef unsigned int u32;
typedef long long i64;
typedef unsigned long long u64;

#define two(i)		(1<<(i))
#define towL(i)		(1LL<<(i))
#define CLR(a,v)	memset(a,v,sizeof(a))
#define MP(a,b)		make_pair(a,b)
#define SIZE(a)		((int)a.size())
#define LENGTH(a)	((int)a.length())
#define REP(i,n)	for(int i=0; i<(n); ++i)
#define REPD(i,n)	for(int i=(n)-1; i>=0; --i)
#define FOR(i,s,e)	for(int i=(s); i<=(e); ++i)
#define FORD(i,s,e)	for(int i=(s); i>=(e); --i)

template<class T>inline int cMin(T& a, T b) {
    return b < a ? a = b, 1 : 0;
}

template<class T>inline int cMax(T& a, T b) {
    return a < b ? a = b, 1 : 0;
}

template<class T>inline string to_str(T v) {
    ostringstream os;
    os << v;
    return os.str();
}


char *input_file = "E:/A-large.in";
char *output_file = "E:/A-large.out";
const bool zzzz = true;

struct Node {
    double w;
    string f;
    Node *ls, *rs;
} bb[10240];
int bbp = 0;
typedef Node *NodePtr;
NodePtr root;
char cs[1024];

int N;
set<string> g;

void go() {
    scanf("%d", &N);
    double v;
    NodePtr p;
    while (N--) {
        scanf("%s", cs);
        int n;
        scanf("%d", &n);
        g.clear();
        while (n--) {
            scanf("%s", cs);
            g.insert(string(cs));
        }
        v = 1.0;
        p = root;
        for (; p;) {
            v *= p->w;
            if (g.count(p->f))
                p = p->ls;
            else
                p = p->rs;
        }
        printf("%.7f\n", v);
    }
}

void build(NodePtr& p) {
    p = bb + bbp++;
    p->ls = p->rs = NULL;
    p->f = "";
    scanf("%lf", &(p->w));
    int c;
    for (;;) {
        c = getchar();
        if (c == ' ' || c == '\n') continue;
        if (islower(c)) {
            int i = 0;
            cs[0] = c;
            while (islower(c)) {
                cs[i++] = c;
                c = getchar();
            }
            cs[i] = 0;
            p->f = string(cs);
            if (c == '(' || c == ')') break;
        }
        if (c == '(' || c == ')') break;
    }
    if (c == '(') {
        build(p->ls);
        for (;;) {
            c = getchar();
            if (c == '(') break;
        }
        build(p->rs);
        while (getchar() != ')');
    }
}

void input() {
    bbp = 0;
    int c;
    scanf("%d", &c);
    while (getchar() != '(');
    build(root);
}

int main() {
    if (zzzz) {
        freopen(input_file, "r", stdin);
        freopen(output_file, "w", stdout);
    }
    int T;
    scanf("%d", &T);

    REP(Ti, T) {
        input();
        printf("Case #%d:\n", Ti + 1);
        go();

    }

    return 0;
}

