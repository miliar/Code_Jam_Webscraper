#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

int n, m;
set<string> ss;

int recur(char* str, int len)
{
    int i, cnt;
    char temp[1000];

    if (len == 0) {
        return 0;
    }
    if (ss.find(str) != ss.end()) {
        return 0;
    }

    strcpy(temp, str);
    for (i = len-1; i >= 0; i--) {
        if (temp[i] == '/')
            break;
    }
    temp[i] = 0;
    cnt = recur(temp, i) + 1;
    ss.insert(str);

    return cnt; 
}

int main()
{
    int tc, cn;
    int i, j, k;
    int cnt;
    char buf[1000];
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        scanf("%d%d", &n, &m);
        ss.clear();
        ss.insert("/");
        for (i = 0; i < n; i++) {
            scanf("%s", buf);
            ss.insert(buf);
        }
        cnt = 0;
        while (m--) {
            scanf("%s", buf);
            cnt += recur(buf, strlen(buf));
        }
        printf("Case #%d: %d\n", cn, cnt);
    }
    return 0;
}
