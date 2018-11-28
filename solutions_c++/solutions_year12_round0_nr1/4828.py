#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>
#define eps 1e-6
#define pi acos(-1.0)

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    char alpf[] = "abcdefghijklmnopqrstuvwxyz";
    char tran[] = "yhesocvxduiglbkrztnwjpfmaq";
    int n;
    while (scanf("%d", &n) == 1) {
        char str[200];
        gets(str);
        for (int i = 0; i < n; i++) {
            gets(str);
            for (int j = 0; j < strlen(str); j++)
                if (str[j] != ' ')
                    str[j] = tran[str[j] - 'a'];
            printf("Case #%d: %s\n", i + 1, str);
        }
    }
    return 0;
}