#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

typedef vector <int> tv;

int n;
bool fl, good;
int a[3000], b[3000], col[3000];
bool used[3000], use[3000];
bool can[3000][3000];

void solve(tv& v, int y){
    int sz = v.size();
    for(int i = 0; i < sz - 2; i++){
        for(int j = i + 2; j < sz; j++){
            if(i == 0 && j == sz - 1){
                continue;
            }
            if(can[v[i]][v[j]]){
                tv v1, v2;
                v1.clear();
                int z = i;
                while(true){
                    v1.push_back(v[z]);
                    if(z == j){
                        break;
                    }
                    z = (z + 1) % sz;
                }
                v2.clear();
                z = j;
                while(true){
                    v2.push_back(v[z]);
                    if(z == i){
                        break;
                    }
                    z = (z + 1) % sz;
                }
                solve(v1, y);
                if(!good){
                    return;
                }
                solve(v2, y);
                return;
            }
        }
    }
    for(int i = 1; i <= y; i++){
        use[i] = false;
    }
    for(int i = 0; i < sz; i++){
        use[col[v[i]]] = true;
    }
    for(int i = 1; i <= y; i++){
        if(!use[i]){
            good = false;
            return;
        }
    }
}

void gen(int x, int y, int z){
    if(x == n){
        for(int i = 1; i <= y; i++){
            used[i] = false;
        }
        for(int i = 0; i < n; i++){
            used[col[i]] = true;
        }
        for(int i = 1; i <= y; i++){
            if(!used[i]){
                return;
            }
        }
        tv v;
        v.clear();
        for(int i = 0; i < n; i++){
            v.push_back(i);
        }
        good = true;
        solve(v, y);
        if(!good){
            return;
        }
        printf("Case #%d: %d\n", z, y);
        for(int i = 0; i < n - 1; i++){
            printf("%d ", col[i]);
        }
        printf("%d\n", col[n - 1]);
        fl = true;
        return;
    }
    for(int i = 1; i <= y; i++){
        col[x] = i;
        gen(x + 1, y, z);
        if(fl){
            return;
        }
    }
}

inline void solve(int t){
    int m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < m; i++){
        scanf("%d", &a[i]);
        a[i]--;
    }
    for(int i = 0; i < m; i++){
        scanf("%d", &b[i]);
        b[i]--;
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            can[i][j] = false;
        }
    }
    for(int i = 0; i < m; i++){
        can[a[i]][b[i]] = can[b[i]][a[i]] = true;
    }
    int ans = n;
    for(int i = 0; i < n - 1; i++){
        for(int j = i + 1; j < n; j++){
            if(can[i][j]){
                ans = min(ans, min(j - i + 1, n - (j - i + 1) + 2));
            }
        }
    }
    for(int i = ans; i > 0; i--){
        fl = false;
        gen(0, i, t);
        if(fl){
            break;
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++){
        solve(i);
    }
    return 0;
}
