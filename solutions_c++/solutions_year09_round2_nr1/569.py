/*
 * Author: momodi
 * Created Time:  2009/9/13 0:23:43
 * File Name: a.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
using namespace std;
#define out(x) fprintf(stderr, "%s: %I64d\n", #x, (long long)(x))
#define SZ(v) ((int)(v).size())
const int maxint=-1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
map<int, double> p;
map<int, string> str;
set<int> have;
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d:\n", cc);
        int n;
        scanf("%d", &n);
        char buf[1000];
        gets(buf);
        int c = 0;
        vector<int> now;
        p.clear();
        str.clear();
        have.clear();
        while (c < n) {
//            printf("%d\n", c);
            if (cin.peek() == '\n') {
                ++c;
                getchar();
            } else if (cin.peek() == '(') {
                if (now.empty()) {
                    now.push_back(0);
                } else {
                    if (have.count(now.back()) == 0) {
                        have.insert(now.back());
                        now.push_back(now.back() * 2 + 1);
                    } else {
                        now.push_back(now.back() * 2 + 2);
                    }
                }
                getchar();
            } else if (cin.peek() == ')') {
                now.pop_back();
                getchar();
            } else if (isdigit(cin.peek())) {
                double tmp;
                cin >> tmp;
//                printf("%lf\n", tmp);
                p[now.back()] = tmp;
            } else if (isalpha(cin.peek())) {
                int len = 0;
                while (isalpha(cin.peek())) {
                    buf[len++] = getchar();
                }
                buf[len] = 0;
                str[now.back()] = buf;
            } else {
                getchar();
            }
        }
        int Q;
        scanf("%d", &Q);
        while (Q--) {
            double ans = 1;
            scanf("%s", buf);
            int num;
            scanf("%d", &num);
            set<string> sets;
            while (num--) {
                scanf("%s", buf);
                sets.insert(buf);
            }
            int k = 0;
            while (p.count(k)) {
                ans *= p[k];
                if (sets.count(str[k])) {
                    k = k * 2 + 1;
                } else {
                    k = k * 2 + 2;
                }
            }
            printf("%.7lf\n", ans);
        }
    }
    return 0;
}

