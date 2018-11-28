#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;
#define FOR(n) for(int i = 0; i < n; i++)
#define FORR(a, b) for(int i = a; i <= b; i++)
#define sq(x) x*x
#define PB push_back
typedef long long ll;
typedef __int64 i64;
typedef double db;
const int intinf = 0x3fffffff;
const ll llinf = ll(1)<<60;
const i64 i64inf = i64(1)<<60;
const db eps = 1e-8;


const int N = 505;
char mat[N][N];
db wp[N], wp2[N], owp[N], oowp[N];
int n;


void calwp() {
    
    int i, j, k;
    for(i = 0; i < n; i++) {
        int all = 0, cnt = 0;
        for(j = 0; j < n; j++) {
            if(mat[i][j] != '.') all++;
            if(mat[i][j] == '1') cnt++;
        }
        wp[i] = db(cnt)/db(all);
    }    
}

void calowp() {
    
    int i, j, k;
    db sum = 0;
    int num = 0;
    for(i = 0; i < n; i++) {
        sum = 0, num = 0;
        for(j = 0; j < n; j++) {
            if(mat[i][j] == '.') continue;
            int all = 0, cnt = 0;
            for(k = 0; k < n; k++) {
                if(i == k) continue;
                if(mat[j][k] != '.') all++;
                if(mat[j][k] == '1') cnt++;
            }
            wp2[j] = db(cnt)/db(all);
            sum += wp2[j];
            num++;
        }
        owp[i] = sum/db(num);
    }    
}

void caloowp() {
    
    int i, j, k;
    
    for(i = 0; i < n; i++) {
        int cnt = 0;
        db sum = 0;
        for(j = 0; j < n; j++) {
            if(mat[i][j] == '.') continue;
            cnt++;
            sum += owp[j];    
        }    
        oowp[i] = sum / db(cnt);
    }
}

db calRPI() {
    
    int i, j, k;
    for(i = 0; i < n; i++) {
        db ans = 0;
        ans = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        printf("%.10f\n", ans);    
    }
}

int main() {
    
    freopen("in2.txt", "r", stdin);
    freopen("ans.out", "w", stdout);
    
    
    
    int t, i, j, k;
    cin >> t;
    
    for(int cas = 1; cas <= t; cas++) {
        
        cin >> n;
        for(i = 0; i < n; i++)
            cin >> mat[i];
        
        
        printf("Case #%d:\n", cas);
        calwp();
        calowp();
        caloowp();
        calRPI();
       
        
       
    }
    
    
   // while(1);
    return 0;    
}
