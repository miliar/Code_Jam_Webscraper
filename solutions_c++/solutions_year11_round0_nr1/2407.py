#include <stdio.h>
#include <algorithm>
#include <iostream>
using namespace std;
int n, t;
char ch[2];
int main(){
    int test; scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        scanf("%d", &n);
        int ret = 0, a = 1, b = 1, la = 0, lb = 0;
        while (n--){
            scanf("%s%d", ch, &t);
            if (ch[0] == 'O'){
                int nd = abs(a - t);
                if (nd > la) nd -= la; else nd = 0;
                ret = ret + nd + 1;
                a = t; la = 0; lb += nd + 1;
            } else {
                int nd = abs(b - t);
                if (nd > lb) nd -= lb; else nd = 0;
                ret = ret + nd + 1;
                b = t; lb = 0; la += nd + 1;
            }
        }
        printf("Case #%d: %d\n", cas, ret);
    }
    return 0;
}
