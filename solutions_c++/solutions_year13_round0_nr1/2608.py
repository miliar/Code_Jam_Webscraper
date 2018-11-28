#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 1005;
const int INF = 1 << 29;
const long long MOD = 55566677ll;
const int dx[] = {-1, 0, 0, 1, 1, 1, -1, -1};
const int dy[] = {0, -1, 1, 0, 1, -1, -1, 1};

int n, m;
char s[10][10];

void prep(){
}

void init(){
//    if (scanf("%d", &n) == EOF) exit(0);
    n = m = 4;
    for (int i = 0;i < n;i++){
        scanf("%s", s[i]);
    }
}

bool check(char c){
    for (int i = 0;i < n;i++){
        for (int j = 0;j < m;j++){
            if (i == 0 || j == 0){
                for (int d = 0;d < 8;d++){
                    int cx = i;
                    int cy = j;
                    bool f = true;
                    for (int k = 0;k < 4;k++){
                        if (cx < 0 || cx  >= n || cy < 0 || cy >= m){
                            f = false;
                            break;
                        }
                        if (s[cx][cy] != c && s[cx][cy] != 'T'){
                            f = false;
                            break;
                        }
                        cx += dx[d];
                        cy += dy[d];
                    }
                    if (f){
//                        printf("check %c %d %d %d\n", c, i, j, d);
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

bool exist(char c){
    for (int i = 0;i < n;i++){
        for (int j = 0;j < m;j++){
            if (s[i][j] == c) return true;
        }
    }
    return false;
}

void work(){
    bool f1 = check('X');
    bool f2 = check('O');
    bool f3 = exist('.');
    if (f1){
        printf("X won\n");
    }
    else if (f2){
        printf("O won\n");
    }
    else if (f3){
        printf("Game has not completed\n");
    }
    else{
        printf("Draw\n");
    }
}

int main(){
#ifdef LATTE
//    freopen("a.in", "r", stdin);
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int T, t = 0;
    prep();
    scanf("%d", &T);
    while (T--){
        init();
        printf("Case #%d: ", ++t);
        work();
    }
    return 0;
}
