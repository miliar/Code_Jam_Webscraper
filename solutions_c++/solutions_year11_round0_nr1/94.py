#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int cas, tt;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas ++) {
        int pos1 = 1, pos2 = 1;
        int tim1 = 0, tim2 = 0, last = 0;
        char ch; int pos, n;
        scanf("%d", &n);
        for (int i = 0; i < n; i ++) {
            scanf(" %c%d", &ch, &pos);
            if (ch == 'O') {
                tim1 = max(last + 1, tim1 + abs(pos - pos1) + 1);
                pos1 = pos; last = tim1;
            } else {
                tim2 = max(last + 1, tim2 + abs(pos - pos2) + 1);
                pos2 = pos; last = tim2;
            }
        }
        printf("Case #%d: %d\n", cas, last);
    }
    return 0;
}

