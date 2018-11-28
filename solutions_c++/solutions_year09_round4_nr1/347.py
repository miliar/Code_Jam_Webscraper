#include <cstdio>
#include <cstring>
#include <algorithm>
#include <deque>
#include <set>
using namespace std;
typedef __int64 int64;
#define maxn 64
int n;
set<int64>SET;
struct State{
    int p[40];
    int64 hash() {
        int64 ret = 0;
        for (int i = 0; i < n; ++i) {
            ret = ret * n + p[i]; 
        }
        return ret;
    }
};
bool check(int p[]) {
    bool ok = true;
    for (int j = 0; j < n; ++j) {
        if (p[j] > j + 1) {
            ok = false;
            break;
        }
    }
    return ok;
}

deque<State>que;
int main() {
   // freopen("a.in", "r", stdin);
    int t;
    scanf("%d", &t);
    for (int kase = 1; kase <= t; ++kase) {
        int  i;
        SET.clear();
        scanf("%d", &n);
        char str[128];
        que.clear();
        State cur;
        for (i = 0; i < n; ++i){
            scanf("%s", str);
            int j;
            for (j = n - 1; j >= 0; --j) {
                if (str[j] == '1') break;
            }
            cur.p[i] = j + 1;
        }
        int ans = 0;
        if (!check(cur.p)) {
            que.push_back(cur); 
            SET.insert(cur.hash());
            while (!que.empty()) {
                int sz = que.size();
                ans++;
                while (sz--) {
                    State cur = que.front();
                    que.pop_front();
                    for (int i = 0; i < n - 1; ++i) {
                        swap(cur.p[i], cur.p[i+1]);
                        if (check(cur.p)) {
                            goto ex;
                        } else {
                            int64 h = cur.hash();
                            if (SET.find(h) == SET.end()) {
                                SET.insert(h);
                                que.push_back(cur);
                            }
                        }
                        swap(cur.p[i], cur.p[i+1]);
                    } 
                }
            }
        }
ex:;
   printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}
