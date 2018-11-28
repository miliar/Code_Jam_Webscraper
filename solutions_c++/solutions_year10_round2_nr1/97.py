/*
 * Author: momodi
 * Created Time:  2010/5/8 19:00:54
 * File Name: a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <string>
#include <map>
#include <set>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
#define take(a, b) (((a) >> (b)) & 1)
#define move(v) (1 << (v))

map<string, set<string> > children;
char buf[1000000];
struct Tree {
    map<string, Tree> chi;
};
Tree root;

int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        root.chi.clear();
        int n, m;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", &buf);
            for (char *p = buf; *p; ++p) {
                if (*p == '/') {
                    *p = ' ';
                }
            }
            stringstream O(buf);
            Tree *pre = &root;
            string s;
            while (O >> s) {
                pre = &(pre->chi[s]);
            }
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            scanf("%s", &buf);
            for (char *p = buf; *p; ++p) {
                if (*p == '/') {
                    *p = ' ';
                }
            }
            stringstream O(buf);
            Tree *pre = &root;
            string s;
            while (O >> s) {
                if (pre->chi.count(s) == 0) {
                    ++ans;
                }
                pre = &(pre->chi[s]);
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}

