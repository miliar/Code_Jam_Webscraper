#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <conio.h>
using namespace std;

const int di[] = {-1, 0, 0, 1};
const int dj[] = {0, 1, -1, 0};
const int maxn = 12 + 5; 
const int maxb = 5; 
const int maxl = 10000000 + 10;
 
char mp[maxn][maxn];
int bn, r, c; 

struct Node {
    int x[maxb], y[maxb], step;
    bool boo;
    
    int abs(int x) { return x > 0 ? x : -x; }
    
    bool covered()
    {
        for (int i = 0; i < bn; ++i)
        for (int j = 0; j < bn; ++j)
            if (i!=j && x[i]==x[j] && y[i]==y[j]) return true;
        return false;
    }
    
    void calc()
    {
        boo = true;
        int fat[maxb] = {0, 1, 2, 3, 4};
        for (int i = 0; i < bn; ++i)
        for (int j = 0; j < bn; ++j) {
            if (i == j) continue;
            if (abs(x[i]-x[j])+abs(y[i]-y[j]) > 1) continue;
            int ri = i, rj = j;
            while (fat[ri] != ri) ri = fat[ri];
            while (fat[rj] != rj) rj = fat[rj];
            fat[ri] = rj;
        }
        
        int r = 0;
        while (fat[r] != r) r = fat[r];
        for (int i = 1; i < bn; ++i) {
            int ri = i;
            while (fat[ri] != ri) ri = fat[ri];
            if (ri != r) boo = false;
        }
    }
    
    void sort()
    {
        for (int i = 0; i+1 < bn; ++i)
        for (int j = i+1; j < bn; ++j)
            if (x[i]>x[j] || x[i]==x[j]&&y[i]>y[j]) {
                int t = x[i]; x[i] = x[j]; x[j] = t;
                t = y[i]; y[i] = y[j]; y[j] = t;
            }
    }
    
    bool operator<(const Node &t) const
    {
        for (int i = 0; i < bn; ++i) {
            if (x[i] < t.x[i]) return true;
            if (x[i] > t.x[i]) return false;
            if (y[i] < t.y[i]) return true;
            if (y[i] > t.y[i]) return false;
        }
        return false;
    }
    bool operator==(const Node &t) const
    {
        for (int i = 0; i < bn; ++i)
            if (x[i]!=t.x[i] || y[i]!=t.y[i]) return false;
        return true;
    }
    void print()
    {
        for (int i = 0; i < bn; ++i) printf("%d %d[]", x[i], y[i]);
        printf("\n");
    }
} q[maxl], final;

set<Node> p;

int main(void)
{
    freopen("D.in", "r", stdin);
    freopen("D2.out", "w", stdout);
    int tot;
    scanf("%d", &tot);
    for (int cas = 1; cas <= tot; ++cas) {
        printf("Case #%d: ", cas);
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; ++i) scanf("%s", mp[i]);
        bn = 0;
        int fbn = 0;
        
        for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j) {
            if (mp[i][j] == '.') continue;
            if (mp[i][j] == '#') continue;
            if (mp[i][j] == 'x') {
                final.x[fbn] = i;
                final.y[fbn] = j;
                ++fbn;
            }
            if (mp[i][j] == 'o') {
                q[0].x[bn] = i;
                q[0].y[bn] = j;
                ++bn;
            }
            if (mp[i][j] == 'w') {
                final.x[fbn] = i;
                final.y[fbn] = j;
                q[0].x[bn] = i;
                q[0].y[bn] = j;
                ++bn; ++fbn;
            }
        }
        q[0].sort();
        q[0].calc();
        q[0].step = 0;
        final.sort();
        p.clear();
        
        if (q[0] == final) { printf("0\n"); continue; }
        
        int st = 0, sf = 0, re = -1, found = 0;
        p.insert(q[0]);
        
        while (st<=sf && sf<maxl) {
            for (int i = 0; i < bn; ++i)
            for (int k = 0; k < 4; ++k) {
                ++sf;
                if (sf == maxl) break;
                q[sf] = q[st];
                q[sf].x[i] = q[st].x[i] + di[3-k];
                q[sf].y[i] = q[st].y[i] + dj[3-k];
                if (q[sf].x[i]<0 || q[sf].x[i]>=r || q[sf].y[i]<0 || q[sf].y[i]>=c) {
                    --sf;
                    continue;
                }
                if (mp[q[sf].x[i]][q[sf].y[i]] == '#') {
                    --sf;
                    continue;
                }
                if (q[sf].covered()) {
                    --sf;
                    continue;
                }
                
                q[sf].x[i] = q[st].x[i] + di[k];
                q[sf].y[i] = q[st].y[i] + dj[k];                
                if (q[sf].x[i]<0 || q[sf].x[i]>=r || q[sf].y[i]<0 || q[sf].y[i]>=c) {
                    --sf;
                    continue;
                }
                if (mp[q[sf].x[i]][q[sf].y[i]] == '#') {
                    --sf;
                    continue;
                }
                if (q[sf].covered()) {
                    --sf;
                    continue;
                }
                q[sf].calc();
                if (!q[st].boo && !q[sf].boo) {
                    --sf;
                    continue;
                }
                q[sf].sort();
                if (p.find(q[sf]) != p.end()) {
                    --sf;
                    continue;
                }
                ++q[sf].step;
                p.insert(q[sf]);
                if (q[sf] == final) {
                    found = 1;
                    re = q[sf].step;
                }
            }
            if (found) break;
            //q[st].print();
            ++st;
        }

        printf("%d\n", re);
    } 
    return 0; 
}

