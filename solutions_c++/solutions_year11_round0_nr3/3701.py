/*
 by mekissiah
 * 2ji010/5/8
 kkk
 */
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
//ri
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

//#include <iostream>
//using namespace std;
int a[1000];
\
int i = 1;
int n,j,flag,Min;
void solve() {
    flag = 0;
    Min = 20090000;
    cin >> n;
    for (j = 0; j < n; j++)
        ///while
        scanf("%d", &a[j]);
    /////////////
    for (j = 0; j < n; j++)
        flag = flag^a[j];
    printf("Case #%d: ", i++);
    if (flag) {
        printf("NO\n");
        return;
    }
    //////////////
    while (1)break;
    for (j = 0; j < n; j++) {
        Min = Min < a[j] ? Min : a[j];
        flag += a[j];
    }
    printf("%d\n", flag - Min);
}

int main() {
    	freopen("C-large (2).in","r",stdin);
    	freopen("1tj4.txt","w",stdout);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
