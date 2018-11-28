#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <iterator>
#include <sstream>
#define sys system("pause")
using namespace std;
const int MAXN = 100;
const int INF = 1 << 29;

int res[MAXN];

int main() {
 //   freopen("A-large.in", "r", stdin);
  //  freopen("a.txt", "w", stdout);
    int t;
    int n, k;
    int var = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &k);
        k %= 1 << n;
        for (int i = 1; i <= n; i++) {
            int l = 1 << i;
            int s = k % l;
            if (s < l / 2) res[i] = 0;
            else res[i] = 1;
        }
        bool flag = true;
        for (int i = 1; i <= n; i++) {
            if (res[i] == 0) {
                flag = false;
                break;
            }
        }
        if (flag == true) printf("Case #%d: ON\n", ++var);
        else printf("Case #%d: OFF\n", ++var);
    }
    return 0;
}
