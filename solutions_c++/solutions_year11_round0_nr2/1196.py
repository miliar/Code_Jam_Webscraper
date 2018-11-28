#include <cstdio>
#include <stack>
#include <iostream>
using namespace std;
char com[100];
char opp[100];
char query[200];
char ans[200];
int exist[300];
char theopp[400];
char thecom[400], get[400];

int main() {
   //     freopen("b.in", "r", stdin);
   //     freopen("b.out", "w", stdout);
    int T, cas = 1, c, d, n;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &c);
        memset(thecom, 0, sizeof (thecom));
        memset(theopp, 0, sizeof (theopp));
        for (int i = 0; i < c; ++i) {
            scanf("%s", com);
            thecom[com[0]] = com[1];
            thecom[com[1]] = com[0];
            get[com[0]] = get[com[1]] = com[2];
        }
        scanf("%d", &d);
        for (int i = 0; i < d; ++i) {
            scanf("%s", opp);
            theopp[opp[0]] = opp[1];
            theopp[opp[1]] = opp[0];
        }
        scanf("%d", &n);
        scanf("%s", query);
        stack<char> s;
        memset(exist, 0, sizeof (exist));
        for (int i = 0; i < n; ++i) {
            if (s.empty()) {
                s.push(query[i]);
                exist[query[i]]++;
            } else {
                char ch = s.top();
                if (ch == thecom[query[i]]) {
                    s.pop();
                    exist[ch]--;
                    s.push(get[query[i]]);
                    exist[get[query[i]]]++;
                    if (exist[theopp[get[query[i]]]]) {
                        while (!s.empty()) {
                            s.pop();
                        }
                        memset(exist, 0, sizeof (exist));
                    }
                    continue;
                }
                if (exist[theopp[query[i]]]) {
                    while (!s.empty()) {
                        s.pop();
                    }
                    memset(exist, 0, sizeof (exist));
                    continue;
                }
                s.push(query[i]);
                exist[query[i]]++;
            }
        }
        int anslen = 0;
        while (!s.empty()) {
            ans[anslen++] = s.top();
            s.pop();
        }
        printf("Case #%d: [", cas++);
        for (int i = anslen - 1; i >= 0; --i) {
            printf("%c", ans[i]);
            if (i != 0) {
                printf(", ");
            }
        }
        puts("]");
    }
    //    system("pause");
    return 0;
}
