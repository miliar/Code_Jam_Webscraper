/**********************************************************************
Author: hanshuai
Created Time:  2011/5/22 0:10:05
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
const int maxn = 105;
char s[maxn][maxn];
int N;
pair<int,int> WP[maxn];
double OWP[maxn], OOWP[maxn];
void solve(){
    for(int i = 0; i < N; i ++){
        int t1 = 0, t2 = 0;
        for(int j = 0; j < N; j ++){
            if(s[i][j] != '.') t2 ++;
            if(s[i][j] == '1') t1 ++;
        }
        WP[i] = make_pair(t1, t2);
    }
    
    for(int i = 0; i < N; i ++){
        double ret = 0;
        int cnt = 0;
        for(int j = 0; j < N; j ++){
            if(s[i][j] == '.') continue;
            cnt ++;
//            if(i == j) continue;
            pair<int,int> p = WP[j];
            if(s[j][i] != '.') p.second --;
            if(s[j][i] == '1') p.first --;
            ret += (double)p.first / p.second;
        }
        OWP[i] = ret/cnt;
    }
    
    for(int i = 0; i < N; i ++){
        double ret = 0;
        int cnt = 0;
        for(int j = 0; j < N; j ++){
            if(s[i][j] == '.') continue;
            ret += OWP[j];
            cnt ++;
        }
        OOWP[i] = ret/cnt;
    }
    
}
int main() {
    freopen("a.out", "w", stdout);
    int cas = 0, test;
    scanf("%d", &test);
    while(test--){
        scanf("%d", &N);
        for(int i = 0; i < N; i ++) scanf("%s", s[i]);
        solve();
        printf("Case #%d:\n", ++cas);
        for(int i = 0; i < N; i ++){
//            printf("%lf %lf %lf\n", 1.0*WP[i].first/WP[i].second, OWP[i], OOWP[i]);
            printf("%.10lf\n", 0.25*WP[i].first/WP[i].second
                    +0.50*OWP[i]+0.25*OOWP[i]);
        }
    }
    return 0;
}

