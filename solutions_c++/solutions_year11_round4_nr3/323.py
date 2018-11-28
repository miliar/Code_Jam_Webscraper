#include <cstdio>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#define sys system("pause")
using namespace std;

bool notp[1010]; //素数判定  
int pr[1010], pn; //pr存放素数,pn当前素数个数。
int t[1010];

void getprime() {
    pn = 0;
    memset(notp, 0, sizeof ( notp));
    for (int i = 2; i < 1010; i++) {
        if (!notp[i]) pr[pn++] = i;
        for (int j = 0; j < pn && pr[j] * i < 1010; j++) {
            notp[pr[j] * i] = i;
            if (i % pr[j] == 0) break;
        }
    }
}

int main() {
  //   freopen("a.in", "r", stdin);
   //   freopen("a.txt", "w", stdout);
    int T;
    getprime();
    int n; //long long?
    scanf("%d", &T);
    int cas = 1;
    while (T--) {
        scanf("%d", &n);
        if (n == 1) {
            printf("Case #%d: 0\n", cas++);
            continue;
        }
        memset(t, 0, sizeof(t));
        int a = 0, b = 0;
        for (int i = 2; i <= n; ++i) {
            for (int j = 0; pr[j] <= i; ++j) {
                if (i % pr[j] == 0) {
                    int w = 0;
                    int tmp = i;
                    if (t[pr[j]] == 0) {
                        ++a;
                    }
                    while (tmp % pr[j] == 0) {
                        tmp /= pr[j];
                        ++w;
                    } 
                    if (w > t[pr[j]]) {
                        t[pr[j]] = w;
                    }
                }
            }
        }
        for (int i = 2; i <= n; ++i) {
            b += t[i];
        }
        ++b;
      //  cout << a << endl << b << endl;
        printf("Case #%d: %d\n", cas++, b - a);
    }
   // sys;
    return 0;
}
