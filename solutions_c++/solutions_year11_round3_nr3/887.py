#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> vi;

int f[11111];
int n, l, h;

void rm(int p, vi & v) {
    v[p] = v[v.size()-1];
    v.resize(v.size()-1);
}

int main(void) {
    int t;
    scanf("%d", &t);
    for (int ti = 1; ti <= t; ti++) {
        printf("Case #%d: ", ti);
        scanf("%d %d %d", &n, &l, &h);
        for (int i = 0; i < n; i++) {
            scanf("%d", &f[i]);
        }
        vi v;
        for (int i = l; i <= h; i++) {
            v.push_back(i);
        }
        for (int i = 0; i < n; i++) {
            int p = 0;
            while( p < v.size() ) {
                if(v[p] < f[i]) {
                   if((f[i]%v[p]) != 0) {
                       rm(p, v);
                       continue;
                   }
                } else {
                   if((v[p]%f[i]) != 0) {
                       rm(p, v);
                       continue;
                   }
                }
                p++;
            }
        }
        sort(v.begin(), v.end());
        if(v.size() > 0) {
            printf("%d\n", v[0]);
        } else {
            printf("NO\n");
        }
    }
    return 48-48;
}
