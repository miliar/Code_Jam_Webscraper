#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <ctime>
#include <cstdlib>
#define Hash1 (LL)11111
#define Hash2 (LL)13337
#define lson l,m,rt << 1
#define rson m + 1,r,rt << 1 | 1
#define eps 1e-8
#define ft first
#define sd second
#define zero(x) (((x)>0?(x):-(x))<eps)
#define LL long long
#define Test puts("END")
#define pi acos(-1.0)
#pragma comment(linker, "/STACK:32000000")
using namespace std;
const int MOD = 1000000007;
const int INF = 1000000000;
const int N = 10;
const int M = 1000;

char mp[N][N];
bool flag;

int solve();

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int t = 1;t <= cas;t ++){
        for(int i = 0;i < 4;i ++)
            scanf("%s",mp[i]);
        flag = false;
        int ans = solve();
        printf("Case #%d: ",t);
        if(ans == 0){
            if(!flag) puts("Draw");
            else puts("Game has not completed");
        }
        else if(ans == 1) puts("X won");
        else puts("O won");
    }
    return 0;
}

int solve()
{
    int X,O;
    for(int i = 0;i < 4;i ++){//row
        X = O = 0;
        for(int j = 0;j < 4;j ++){
            if(mp[i][j] == '.') flag = true;
            if(mp[i][j] == 'X' || mp[i][j] == 'T') X ++;
            if(mp[i][j] == 'O' || mp[i][j] == 'T') O ++;
        }
        if(X >= 4) return 1;
        if(O >= 4) return 2;
    }
    for(int i = 0;i < 4;i ++){//col
        X = O = 0;
        for(int j = 0;j < 4;j ++){
            if(mp[j][i] == 'X' || mp[j][i] == 'T') X ++;
            if(mp[j][i] == 'O' || mp[j][i] == 'T') O ++;
        }
        if(X >= 4) return 1;
        if(O >= 4) return 2;
    }
    X = O = 0;
    for(int i = 0;i < 4;i ++){//left dra
        if(mp[i][i] == 'X' || mp[i][i] == 'T') X ++;
        if(mp[i][i] == 'O' || mp[i][i] == 'T') O ++;
        if(X >= 4) return 1;
        if(O >= 4) return 2;
    }
    X = O = 0;
    for(int i = 0;i < 4;i ++){
        if(mp[i][3 - i] == 'X' || mp[i][3 - i] == 'T') X ++;
        if(mp[i][3 - i] == 'O' || mp[i][3 - i] == 'T') O ++;
        if(X >= 4) return 1;
        if(O >= 4) return 2;
    }
    return 0;
}