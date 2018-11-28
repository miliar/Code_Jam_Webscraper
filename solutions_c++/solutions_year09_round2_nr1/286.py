/**********************************************************************
Author: Xay
Created Time:  2009-9-13 0:20:46
File Name: contest\gcj09r1b\a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxl = 100 + 5;
const int maxlen = 80 + 3;
const int maxn = 100 + 3;
struct node {
    string s;
    double p;
    int lf, rt;
};

char s[maxl * maxlen], s0[maxlen];
int pre[maxl * maxlen];
node rec[maxl * maxlen];
set<string> m;
int num;

void build(char *s, int n) {
    int now = 0, next;
    for (int i = 0; i < n; i = next) {
//        printf("%d:\n", i);
        next = i + 1;
        if (s[i] == ' ') continue;
        if (s[i] == '(') {
            pre[num] = now;
            if (rec[now].lf == 0) rec[now].lf = num;
            else rec[now].rt = num;
            now = num++;
        } else if (s[i] == ')') {
            now = pre[now];
        } else if (isdigit(s[i])) {
            sscanf(s + i, "%lf", &rec[now].p);
            while (s[next] != ')' && s[next] != ' ') ++next;
        } else if (isalpha(s[i])) {
//            printf("~\n");
            sscanf(s + i, "%s", s0);
//            printf("~~~%d: %s\n", now, s0);
            rec[now].s = string(s0);
//            printf("~~\n");
            while (s[next] != ' ') ++next;
        }
    }
//    printf("%d\n", now);
}
int main()
{
    freopen("a.out", "w", stdout);
    int t, l, ca = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d\n", &l);
        s[0] = 0;
        while (l--) {
            gets(s0);
            strcat(s, s0);
            strcat(s, " ");
        }
//        printf("%s\n", s);
        num = 1;
        for (int i = 0; i < maxl * maxlen; ++i) {
            rec[i].s = string();
            rec[i].p = rec[i].lf = rec[i].rt = 0;
        }
        build(s, strlen(s));
//        for (int i = 0; i < num; ++i) {
//            printf("%d: %lf %s %d %d\n", i, rec[i].p, rec[i].s.c_str(), rec[i].lf, rec[i].rt);
//        }
        int n;
        scanf("%d", &n);
        printf("Case #%d:\n", ++ca);
        for (int i = 0; i < n; ++i) {
            m.clear();
            int k;
            scanf("%s%d", s, &k);
            for (int j = 0; j < k; ++j) {
                scanf("%s", s0);
                m.insert(string(s0));
            }
            int now = 1;
            double ans = rec[now].p;
            while (rec[now].s[0]) {
                if (m.find(rec[now].s) != m.end()) {
                    now = rec[now].lf;
                } else {
                    now = rec[now].rt;
                }
                ans *= rec[now].p;
            }
            printf("%.7lf\n", ans);
        }
    }
    return 0;
}

