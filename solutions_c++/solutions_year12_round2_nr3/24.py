#include <stdio.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <bitset>
#include <time.h>
#include <climits>

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

LL a[999], ans1[999], ans2[999];
int an1, an2;

struct Tp {
    LL x;
    int last;

    Tp(LL x = 0, int last = 0):x(x),last(last){};

    bool operator<(const Tp& B)const{
        return x > B.x;
    }
};


int main(void){
    freopen("in","r",stdin);
    freopen("out","w",stdout);

    int T;
    scanf("%d\n",&T);
    for(int _=1;_<=T;_++){
        int n;
        LL s = 0;
        cin >> n;
        for (int i = 0; i < n;i++) {
            cin >> a[i];
            s += a[i];
       }

       priority_queue<Tp> q;
       map<LL, int> pr;
       sort(a, a + n);

       for (int i = 0; i < n; i++) {
            q.push(Tp(a[i], i));
            pr[a[i]] = i;
       }
       LL ans = -1, ansi = 0;
       while (!q.empty()) {
            Tp t = q.top(); q.pop();
            for (int i = t.last + 1; i < n; i++) {
                LL s = t.x + a[i];
                if (pr[s]) {
                    ans = s;
                    ansi = i;
                    break;
                } else {
                    pr[s] = i;
                    q.push(Tp(s, i));
                }
            }
            if (ans != -1) break;
       }
        bool can = true;
        printf("Case #%d:\n",_);
        if (!can) {
            puts("Impossible");
        } else {
            LL x = ans, s1 = 0, s2 = 0;
            while (x != 0) {
                s1 += a[pr[x]];

                cout << a[pr[x]] << " ";
                x -= a[pr[x]];
            }
            cout << endl;

            cout << a[ansi] << " ";
            s2 = a[ansi];
            x = ans - a[ansi];
            while (x != 0) {
                s2 += a[pr[x]];
                cout << a[pr[x]] << " ";
                x -= a[pr[x]];
            }
            cout << endl;

            if (s1 != s2) {
                cerr << "!!!!" << _ << "!!!!!" << endl;
            }
        }
        cout << flush;
    }

    return 0;
}
