/* CopyRight (c) cnHawk */
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
#define Tx tree[i].x
#define Ty tree[i].y
#define Tjx tree[j].x
#define Tjy tree[j].y

struct node{
    int x, y;
}tree[102400];

int md[3][3];

node mm(int a, int b){
    return (node){a, b};
}

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int kase, N;
    scanf("%d", &N);
    for(kase = 1; kase <= N; kase++){
        int n, A, B, C, D, x, y, M, i, j;
        int nmd[3][3];
        memset(md, 0, sizeof(md));
        scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x, &y, &M);
        tree[0] = mm(x%3, y%3);
        md[x%3][y%3]++;
        for(i = 1; i < n; i++){
            x = (int)(((LL)A * x + B) % M);
            y = (int)(((LL)C * y + D) % M);
            md[x%3][y%3]++;
            tree[i] = mm(x%3, y%3);
        }
        LL ans = 0;
        for(i = 0; i < n; i++){
            md[Tx][Ty] --;
            memcpy(nmd, md, sizeof(md));
            for(j = i+1; j < n; j++){
                nmd[Tjx][Tjy]--;
                ans += nmd[(9-Tx-Tjx)%3][(9-Ty-Tjy)%3];
            }
        }
        printf("Case #%d: %I64d\n", kase, ans);
    }
      
    return 0;
}
