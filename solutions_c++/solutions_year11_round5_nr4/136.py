#include <iostream> 
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

bool flag[150];
int seq[150];
int len, tot;

void init() {
    char buf[150];
    scanf("%s", buf);
    len = strlen(buf);
    tot = 0;
    for (int i = 0; i < len; i ++)
        if (flag[len-i] = (buf[i] == '?'))
            tot ++;
        else
            seq[len-i] = (buf[i] == '0' ? 0 : 1);
}

void solve(int case_index) {
    for (int st = 0, ast = 1<<tot; st < ast; ++ st) {
        for (int tmp = st, i = 1; i <= len; i ++)
            if (flag[i])
                seq[i] = (tmp&1), tmp >>= 1;
        long long x = 0;
        for (int i = len; i >= 1; i --)
            x = x*2 + seq[i];
       // cout << x << endl;
        long long a = (long long)sqrt((double)x + 0.1);
        if (a*a == x) {
            printf("Case #%d: ", case_index);
            for (int i = len; i >= 1; i --) printf("%d", seq[i]);
            printf("\n");
            return ;
        }
    }
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small.txt", "w", stdout);
    int case_count;
    scanf("%d", &case_count);
    for (int i = 1; i <= case_count; i ++) {
        cerr<<i<<endl;
        init();
        solve(i);
    }
    return 0;
}
