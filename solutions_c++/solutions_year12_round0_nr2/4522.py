using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define D(x) cout << #x " is " << x << endl

struct Triplet{
    int a,b,c;
    
    Triplet(){
        a = -1; b = -1; c = -1;
    }
    
    Triplet(int i, int j, int k){
        assert(i <= j and j <= k);
        assert(k - i <= 2 and k - i >= 0);
        a = i; b = j; c = k;
    }
    
    bool surprise(){
        if (c <= a + 1) return false;
        return true;
    }
    
    int sum(){
        return a + b + c;
    }
    
    int best(){
        assert(c == max(a, max(b, c)));
        return c;
    }
    
    void print(){
        printf("%d = (%d, %d, %d)", a+b+c, a, b, c); ( b <= a + 1 and c <= a + 1 ) ? puts("") : puts("*");
    }
    
};

const int MAXN = 105;
const int MAXS = 105;
Triplet a [35][2];
int score[MAXN];
int dp[MAXN][MAXS];



int main(){
    for (int sum = 0; sum <= 30; sum++){
        //printf("Para la suma: %d\n", sum);
        for (int i = 0; i <= 10; i++){
            for (int j = i; j <= min(10, i + 2); j++){
                int k = sum - i - j;
                if ( i <= k and k <= i + 2 and j <= k and k <= j + 2 and k >= 0 and k <= 10){
                    //printf("(%d, %d, %d)", i, j, k); ( j <= i + 1 and k <= i + 1 ) ? puts("") : puts("*");
                    Triplet t = Triplet(i, j, k);
                    if (t.surprise()) a[sum][1] = t;
                    else a[sum][0] = t; 
                }
            }
        }
    }
    int cases; cin >> cases;
    int run = 1;
    while (cases--){
        int n, s, p;
        cin >> n  >> s >> p;
        for (int i = 0; i < n; i++){
            cin >> score[i];
            // a[score[i]][0].print();
            // a[score[i]][1].print();
        }
        
        for (int i = 0; i < s; i++) dp[n][i] = -1 << 30;
        dp[n][s] = 0;
        //for (int i = 0; i <= n; i++) dp[i][s + 1] = -1 << 30;
        
        for (int i = n - 1; i >= 0; i--){
            for (int k = 0; k <= s; k++){
                dp[i][k] = dp[i + 1][k] + (a[score[i]][0].best() >= p ? 1 : 0);
                if (a[score[i]][1].a != -1 and k < s){
                    dp[i][k] = max(dp[i][k], dp[i + 1][k + 1] + (a[score[i]][1].best() >= p ? 1 : 0));
                }
            }
        }
        // for (int i = 0; i <= n; i++){
        //     for (int k = 0; k <= s; k++){
        //         printf("%d ", dp[i][k]);
        //     }
        //     puts("");
        // }
        
        printf("Case #%d: %d\n", run++, dp[0][0]);
        
    }
    
    
    return 0;
}
