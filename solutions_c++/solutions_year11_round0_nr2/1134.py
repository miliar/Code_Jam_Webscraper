/*
 * Sat May  7 13:21:03 CST 2011
 */
#define see(n) cerr << #n << " = " << n << endl
#define seeArray(n, a) cerr << #a << " = ";\
    for (int __i__ = 0; __i__ < (int) n; ++__i__)\
        cerr << a[__i__] << " ";\
    cerr << endl;
#define seeArray2(n, m, a) cerr << #a << " = " << endl;\
    for (int __i__ = 0; __i__ < (int) n; ++__i__) {\
        for (int __j__ = 0; __j__ < (int) m; ++__j__)\
            cerr << a[__i__][__j__] << " ";\
        cerr << endl;\
    }
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <sstream>
#include <cctype>
#include <ctime>
#include <numeric>
using namespace std;
const int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

const int maxn = 128;
int cases, cas = 1;
map<pair<char, char>, char> tran;
map<char, set<char> > no;
char text[maxn];

int main() {
    for (scanf("%d", &cases); cases--; ++cas) {
        tran.clear(); no.clear();
        int m; scanf("%d", &m); for (int i = 0; i < m; ++i) {
            char buf[8]; scanf("%s", buf);
            tran[make_pair(buf[0], buf[1])] = buf[2];
            tran[make_pair(buf[1], buf[0])] = buf[2];
        }
        scanf("%d", &m); for (int i = 0; i < m; ++i) {
            char buf[8]; scanf("%s", buf);
            no[buf[0]].insert(buf[1]);
            no[buf[1]].insert(buf[0]);
        }
        int n; scanf("%d", &n); scanf("%s", text); string now;
        for (int i = 0; i < n; ++i) {
            int len = now.size();
            if (len > 0 && tran.find(make_pair(now[len - 1], text[i])) != tran.end()) {
                char ch = tran[make_pair(now[len - 1], text[i])]; now = now.substr(0, len - 1); now += ch;
            } else {
                map<char, set<char> >::const_iterator it = no.find(text[i]);
                bool ok = true; if (it != no.end()) for (int k = 0; k < len && ok; ++k) if (it->second.find(now[k]) != it->second.end()) {
                    ok = false;
                }
                if (ok) {
                    now += text[i];
                } else {
                    now = "";
                }
            }
        }
        printf("Case #%d: ", cas);
        if (now.empty()) {
            printf("[]\n");
        } else {
            printf("[%c", now[0]); for (unsigned i = 1; i < now.size(); ++i) {
                printf(", %c", now[i]);
            }
            printf("]\n");
        }
    }
    return 0;
}
