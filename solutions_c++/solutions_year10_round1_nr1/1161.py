#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#define BLUE    11111
#define RED     11112
#define NEITHER 11113
#define BOTH    11114
#define MAXN    60

int n, k;
char map[MAXN][MAXN];

inline int max(int a, int b){return (a > b)? a: b;}
inline int min(int a, int b){return (a < b)? a: b;}
void rotate(int r, bool &blue, bool &red);
void init(){
    memset(map, 0, sizeof map);
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%s", map[i]);
}
int solve(){
    int res_r = 0, res_b = 0;
    for (int r = 0; r < 2; r++){
        bool blue, red;
        rotate(r, blue, red);
        if (blue) res_b++; else res_b = 0;
        if (red) res_r++; else res_r = 0;
    }
    if (res_b && res_r) return BOTH;
    if (res_b) return BLUE;
    if (res_r) return RED;
    else return NEITHER;
}
void calc(bool &blue, bool &red){
    int i, j;
    //calc row
    int res_b = -1, res_r = -1;
    blue = red = false;
    for (i = n - 1; i >= 0; i--){
        int b = 0, r = 0;
        for (j = 0; j < n; j++){
            if (map[i][j] == 'B') b++; else b = 0;
            if (map[i][j] == 'R') r++; else r = 0;
            res_b = max(res_b, b);
            res_r = max(res_r, r);
        }
    }
    if (res_b >= k) blue = true;
    if (res_r >= k) red = true;

    res_b = res_r = -1;
    //calc column
    for (j = 0; j < n; j++){
        int b = 0, r = 0;
        for (i = n-1; i >= 0; i--){
            if (map[i][j] == 'B') b++; else b = 0;
            if (map[i][j] == 'R') r++; else r = 0;
            res_b = max(res_b, b);
            res_r = max(res_r, r);
        }
    }
    if (res_b >= k) blue = true;
    if (res_r >= k) red = true;

    res_b = res_r = -1;
    //calc diagnal1
    for (j = 0; j <= 2*n - 2; j++){
        int b = 0, r = 0;
        for (i = max(j-n+1, 0); i < min(j+1, n); i++){
            if (map[i][j-i] == 'B') b++; else b = 0;
            if (map[i][j-i] == 'R') r++; else r = 0;
            res_b = max(res_b, b);
            res_r = max(res_r, r);
        }
    }
    if (res_b >= k) blue = true;
    if (res_r >= k) red = true;

    res_b = res_r = -1;
    //calc diagnal2
    for (j = -(n - 1); j <= (n-1); j++){
        int b = 0, r = 0;
        for (i = max(0, -j); i < min(n-j, n); i++){
            if (map[i][i+j] == 'B') b++; else b = 0;
            if (map[i][i+j] == 'R') r++; else r = 0;
            res_b = max(res_b, b);
            res_r = max(res_r, r);
        }
    }
    if (res_b >= k) blue = true;
    if (res_r >= k) red = true;

    res_b = res_r = -1;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cases = 1;
    scanf("%d", &t);
    while (cases <= t){
        int res;
        init();
        res = solve();
        switch(res)
        {
            case BLUE: printf("Case #%d: Blue", cases); break;
            case RED: printf("Case #%d: Red", cases); break;
            case NEITHER: printf("Case #%d: Neither", cases); break;
            case BOTH: printf("Case #%d: Both", cases); break;
        }
        printf("\n");
        cases++;
    }
    return 0;
}
void rotate(int r, bool &blue, bool &red){
    char buf[MAXN][MAXN];
    memset(buf, 0, sizeof buf);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++){
            switch(r){
                case 0: buf[i][j] = map[i][j]; break;
                case 1: buf[j][n - 1 - i] = map[i][j]; break;
                case 2: buf[n - 1 - i][n - 1 - j] = map[i][j]; break;
                case 3: buf[n - 1 - j][i] = map[i][j]; break;
            }
        }
    for (int j = 0; j < n; j++){
        int rec, i;
        for (rec = n-1; rec >= 0; rec --)
            if (buf[rec][j] != '.') break;
        i = 0;
        for (; rec >= 0; rec--){
            if (buf[rec][j] == '.') continue;
            buf[n - 1 - i][j] = buf[rec][j];
            i++;
        }
        for (; i < n; i++)
            buf[n-1-i][j] = '.';
    }
    memset(map, 0, sizeof map);
    memcpy(map, buf, sizeof (buf));

    calc(blue, red);
}


