#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(x) printf("%s: %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

int n, m;

const int maxn = 2010;

int p[maxn];
vector <int> like[maxn];
vector <int> kind[maxn];

int main() {
    freopen("gcj_b1.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int T = 1; T <= ca; T++) {
        printf("Case #%d:", T);
        scanf("%d%d", &n, &m);
        for (int i = 0; i < m; i++) {
            int t;
            scanf("%d", &t);
            like[i].clear();
            kind[i].clear();
            for (int j = 0; j < t; j++) {
                int t1, t2;
                scanf("%d%d", &t1, &t2);
                like[i].push_back(t1 - 1);
                kind[i].push_back(t2);
            }
        }
        memset(p, 0, sizeof(p));
        bool solve = true;
        while (1) {
            bool to_break = true;
            for (int i = 0; i < m; i++) {
                int flag = false;
                for (int j = 0; j < like[i].size(); j++)
                    if (p[like[i][j]] == kind[i][j]) {
                        flag = true;
                        break;
                    }
                if (flag == false) {
                    to_break = false;
                }
                if (flag == false) {
                    int ok = false;
                    for (int j = 0; j < like[i].size(); j++)
                        if (kind[i][j] == 1) {
                            ok = true;
                            p[like[i][j]] = 1;
                        }
                    if (ok == false) {
                        solve = false;
                        break;
                    }
                }
            }
            if (solve == false)
                break;
            if (to_break)
                break;
        }
        if (solve) {
            for (int i = 0; i < n; i++)
                printf(" %d", p[i]);
            printf("\n");
        }
        else
            printf(" IMPOSSIBLE\n");
    }
    
    return 0;
}


