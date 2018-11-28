#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int a[600][600];
int p[100][100];

int main(){
    int i, j, k, cas, re, m, n, l;
    int r, c, d;
    freopen("B-small-attempt1.in", "r", stdin); freopen("w.txt", "w", stdout);
    scanf("%d", &cas);
    for(re = 1; re <= cas; re++){
        printf("Case #%d: ", re);
        scanf("%d%d%d", &r, &c, &d);
        for(i = 0; i < r; i++)
            for(j = 0; j < c; j++){
                scanf("%1d", &a[i][j]);
                a[i][j] += d;
            }
        int pp = min(r, c);
        int ans = -1;
        for(int len = pp; len >= 3; len--){
            for(i = 0; i + len <= r; i++)
                for(j = 0; j + len <= c; j++){
                    long long x = 0, y = 0, sum = 0;
                    for(k = 0; k < len; k++)
                        for(l = 0; l < len; l++)
                            {
                                if(k == 0 && l == len - 1
                                        || k == len - 1 && l == len - 1
                                        || k == len - 1 && l == 0
                                        || k == 0 && l == 0) continue;
                                x += (LL)a[i+k][j+l] * k;
                                y += (LL)a[i+k][j+l] * l;
                                sum += (LL)a[i+k][j+l];
                            }
                    //printf("%d %d %d %lld %lld %lld\n", i, j, len, x, y, sum);
                    if(x * 2 == sum * (len - 1) && y * 2 == sum * (len - 1)){
                        ans = len;
                        goto found;
                    }

                }

        }
        found:
        if(ans > -1)
            printf("%d\n", ans);
        else
            puts("IMPOSSIBLE");
    }
}
