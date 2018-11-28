#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
const int maxn = 10000 + 5;
int ca, t, n, d[maxn], l[maxn], girl;
queue< pair<int, int> > Q;
set< pair<int, int> > st;

void Inqueue(int u, int v) {
    if(st.count(make_pair(u, v))) return;
    st.insert(make_pair(u, v));
    Q.push(make_pair(u, v));
}

void out(int tp) {
    printf("Case #%d: ", ++ca);
    if(tp == 0) printf("NO\n");
    else printf("YES\n");
}

int main() {
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        for(int i = 1; i <= n; i++) {
            scanf("%d%d", d + i, l + i);
        }
        scanf("%d", &girl);
        while(!Q.empty()) Q.pop();
        st.clear();
        Q.push(make_pair(0, 1));
        st.insert(make_pair(0, 1));
        bool ans = false;
        while(!Q.empty()) {
            int now = Q.front().first;
            int hold = Q.front().second;
            Q.pop();
            int dis = d[hold] + min((d[hold] - d[now]), l[hold]);
            //cout << now << " " << hold << " " << dis << endl;
            if(dis >= girl) {
                ans = true;
                break;
            }
            for(int i = hold + 1; i <= n; i++) {
                if(dis >= d[i]) {
                    Inqueue(hold, i);
                }
                else {
                    break;
                }
            }
        }
        if(ans) out(1);
        else out(0);
    }
    return 0;
}

