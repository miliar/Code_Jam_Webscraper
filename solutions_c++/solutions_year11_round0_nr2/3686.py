#include <iostream>
#include<cstdio>
#include<cstring>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 0; i < cas; i++) {
        int c, d, n;
        scanf("%d", &c);
        map<string, char>com;
        map<char, char>cle;
        for (int i = 0; i < c; i++) {
            char list[5];
            scanf("%s", list);
            string tmp;
            char s;
            tmp.append(1, list[0]);
            tmp.append(1, list[1]);
            s = list[2];
            com.insert(make_pair(tmp, s));
            swap(tmp[0], tmp[1]);
            com.insert(make_pair(tmp, s));
        }
        scanf("%d", &d);
        for (int i = 0; i < d; i++) {
            char list[5];
            scanf("%s", list);
            char a = list[0], b = list[1];
            cle.insert(make_pair(a, b));
            cle.insert(make_pair(b, a));
        }
        scanf("%d", &n);
        char res[1000];
        int len = 0;
        string now;
        cin >> now;
        for (int i = 0; i < n; i++) {
            res[len] = now[i];
            len++;
            while (len > 1) {
                string tmp;
                tmp.append(1, res[len - 1]);
                tmp.append(1, res[len - 2]);
                if (com.find(tmp) == com.end()) {
                    break;
                } else {
                    char left = com.find(tmp)->second;
                    len--;
                    res[len - 1] = left;
                }
            }
            for (int i = 0; i < len - 1; i++) {
                if (cle.find(res[i]) != cle.end() && cle.find(res[i])->second == res[len - 1]) {
                    len = 0;
                    break;
                }
            }
        }
        printf("Case #%d: [", i + 1);
        for (int i = 0; i < len; i++) {
            if (i != 0)
                printf(", ");
            printf("%c", res[i]);
        }
        printf("]\n");
    }
    return 0;
}
