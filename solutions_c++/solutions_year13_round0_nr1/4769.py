#include <cstdio>
#include <stdlib.h>
#include <cstring>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <time.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long LL;
#define INF 0x3f3f3f3f
#define PI acos(-1)

const int N = 10;
const int n = 4;

int x[N], y[N];
char mp[N][N];

bool win(char c){
    memset(x, 0, sizeof(x));
    memset(y, 0, sizeof(y));
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++){
            if(mp[i][j] == c)
                x[i]++, y[j]++;
            else if(mp[i][j] == 'T')
                x[i] += 10, y[j] += 10;
        }
    for(int i = 0; i < n; i++)
        if(x[i] == 4 || x[i] == 13) return true;
        else if(y[i] == 4 || y[i] == 13) return true;

    int d1 = 0, d2 = 0;
    for(int i = 0; i < n; i++){
        if(mp[i][i] == c) d1++;
        else if(mp[i][i] == 'T') d1 += 10;
        if(mp[i][n - 1- i] == c) d2++;
        else if(mp[i][n - 1 - i] == 'T') d2 += 10;
    }
    if(d1 == 4 || d1 == 13 || d2 == 4 || d2 == 13) return true;
    return false;
}
int main(){
    #ifdef ONLINE_JUDGE
    #else
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    scanf("%d", &T);
    for(int kcase = 1; kcase <= T; kcase++){
        for(int i = 0; i < n; i++)
            scanf("%s", mp[i]);

        bool X = false, O = false;
        if(win('X')) X = true;
        if(win('O')) O = true;

        bool D = true;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if(mp[i][j] == '.') D = false;

        printf("Case #%d: ", kcase);
        if(X) printf("X won\n");
        else if(O) printf("O won\n");
        else if(D) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
