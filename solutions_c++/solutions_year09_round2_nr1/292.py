#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

const int L = 1000;

struct Node {
    double v;
    string s;
    Node *l, *r, *p;
    Node() {};
} _dat[L], *_roo;

int _end;
set<string> _set;

void Init() {
    _roo = _dat;
    _end = 1;
    for (int i = 0; i < L; ++i) {
        _dat[i].l = NULL;
        _dat[i].r = NULL;
    }
}

void Ins(double v, string &s, Node *p) {
    _dat[_end].v = v;
    _dat[_end].s = s;
    _dat[_end].p = p;
    if (NULL == p->l) {
        p->l = _dat + _end;
    }
    else {
        p->r = _dat + _end;
    }
    ++_end;
}

void IptT(int l) {
    Node *p = _roo;
    while ('(' != getchar());
    int i = 1;
    for (;;) {
		double v;
        scanf("%lf", &v);
        int c;
        while (c = getchar(), ' ' == c || '\n' == c);
        string s;
        char cs[128];
        while (islower(c)) {
			s += c;
			c = getchar();
        }
        Ins(v, s, p);
        if (NULL == p->r) {
        	p = p->l;
		}
		else {
			p = p->r;
		}
        if (')' == c) {
            p = p->p;
            --i;
            if (0 == i) break;
        }
        for (;;) {
            while (c = getchar(), ' ' == c || '\n' == c);
            if (')' == c) {
                p = p->p;
                --i;
                if (0 == i) break;
            }
            else {
				++i;
				break;
			}
        }
        if (0 == i) break;
    }
}

double DFS(Node *p) {
    if (NULL == p) return 1.0;
    double ret = 0.0;
    if (_set.find(p->s) != _set.end()) {
        ret = DFS(p->l);
    }
    else {
        ret = DFS(p->r);
    }
    return ret * p->v;
}

int main() {
	// freopen("A_small_in.txt", "r", stdin);
	// freopen("A_small_out.txt", "w", stdout);
	// freopen("A_large_in.txt", "r", stdin);
	// freopen("A_large_out.txt", "w", stdout);
    int tc;
    char s[128];
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        Init();
        int l;
        scanf("%d", &l);
        IptT(l);
        printf("Case #%d:\n", tci);
        int a;
        scanf("%d", &a);
        while (a--) {
            _set.clear();
            int n;
            scanf("%s%d", s, &n);
            for (int i = 0; i < n; ++i) {
                scanf("%s", s);
                _set.insert(string(s));
            }
            printf("%.7lf\n", DFS(_roo->l));
        }
    }
    return 0;
}
