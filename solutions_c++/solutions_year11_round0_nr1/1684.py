#include <iostream>
#include <cstdio>

using namespace std;

const int inf = (int)1e9;

int r;
int t[200], p[200];
int d[200][200][200];
int queue[8000000];

inline bool good(int a){
    return ((a >= 0) && (a < 100));
}

inline void relax(int a, int b, int c, int dd){
    if(d[a][b][c] > dd){
        d[a][b][c] = dd;
        queue[r++] = a;
        queue[r++] = b;
        queue[r++] = c;
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for(int ttt = 0; ttt < tt; ttt++){
        int n;
        scanf("%d", &n);
        for(int i = 1; i <= n; i++){
            char ch;
            scanf("%c", &ch);
            while((ch != 'O') && (ch != 'B')){
                scanf("%c", &ch);
            }
            t[i] = 1;
            if(ch == 'B'){
                t[i] = 2;
            }
            scanf("%c", &ch);
            while((ch < '0') || (ch > '9')){
                scanf("%c", &ch);
            }
            p[i] = 0;
            while((ch >= '0') && (ch <= '9')){
                p[i] = p[i] * 10 + ch - '0';
                scanf("%c", &ch);
            }
            p[i]--;
        }
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < 100; j++){
                for(int z = 0; z <= n; z++){
                    d[i][j][z] = inf;
                }
            }
        }
        d[0][0][0] = 0;
        int l = 0;
        r = 3;
        queue[0] = 0;
        queue[1] = 0;
        queue[2] = 0;
        while(l < r){
            int a = queue[l++];
            int b = queue[l++];
            int c = queue[l++];
            if((c < n) && (t[c + 1] == 1) && (a == p[c + 1])){
                for(int i = -1; i <= 1; i++){
                    if(good(b + i)){
                        relax(a, b + i, c + 1, d[a][b][c] + 1);
                    }
                }
            }
            if((c < n) && (t[c + 1] == 2) && (b == p[c + 1])){
                for(int i = -1; i <= 1; i++){
                    if(good(a + i)){
                        relax(a + i, b, c + 1, d[a][b][c] + 1);
                    }
                }
            }
            for(int i = -1; i <= 1; i++){
                for(int j = -1; j <= 1; j++){
                    if((good(a + i)) && (good(b + j))){
                        relax(a + i, b + j, c, d[a][b][c] + 1);
                    }
                }
            }
        }
        int ans = inf;
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < 100; j++){
                ans = min(ans, d[i][j][n]);
            }
        }
        printf("Case #%d: %d\n", ttt + 1, ans);
    }
    return 0;
}
