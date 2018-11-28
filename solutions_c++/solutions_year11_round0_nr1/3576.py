#include <cstdlib>
#include <algorithm>
#include <limits.h>
#include <stdio.h>
using namespace std;

int main() {
    freopen("/home/gaia/Downloads/in", "r", stdin);
    freopen("/home/gaia/Downloads/out", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        int who = -1;
        int sum = 0;
        int pre=0;
        int ox = 1, bx = 1;
        while (n--) {
            char s[3];
            int x,tim,find=0;
            scanf("%s%d", s, &x);
            if (s[0] == 'O') {
                tim = abs(x - ox);
                ox = x;
                if (who != 0)tim = max(0, tim - pre);
                else find=1;
                who=0;
            } else {
                tim = abs(x - bx);
                bx = x;
                if (who != 1)tim = max(0, tim - pre);
                else find=1;
                who=1;
            }
            tim++;
            sum += tim;
            if(find)pre+=tim;
            else pre = tim;
        }
        printf("Case #%d: %d\n",cas++,sum);
    }
    return 0;
}

