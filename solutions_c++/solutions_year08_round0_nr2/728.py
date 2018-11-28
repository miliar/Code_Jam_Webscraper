#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long
#define ld long double

const int MAXN = 1000;

struct trip{
    int t1, t2, k;
    
    trip(){
        t1 = 0;
        t2 = 0;
        k = 0;
    }
    
    trip(int T1, int T2, int K){
        t1 = T1;
        t2 = T2;
        k = K;
    }
};


string s1, s2;
int tk, n, m;
trip v[MAXN * 2];

bool us[MAXN];
int ans[2];

bool lesss(trip a, trip b){
    if (a.t1 != b.t1) return a.t1 < b.t1;
    if (a.t2 != b.t2) return a.t2 < b.t2;

    if (a.k != b.k) return a.k < b.k;
    return 0;    
}

int make(string s1){
    int h = (s1[0] - '0') * 10 + s1[1] - '0';
    int m = (s1[3] - '0') * 10 + s1[4] - '0';
    return h * 60 + m;
}


int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    

    cin >> tk;
    
    forn(ii, tk){
         int T;
         cin >> T;
         cin >> n;
         cin >> m;
         
         int N = 0;
         
         forn(i, n){
             cin >> s1;
             cin >> s2;
             
             v[N] = trip(make(s1), make(s2), 0);
             ++N;
         }
         
         forn(i, m){
             cin >> s1;
             cin >> s2;
             
             v[N] = trip(make(s1), make(s2), 1);
             ++N;
         }
         
         memset(us, 0, sizeof us);
         sort(v, v + N, lesss);
         memset(ans, 0, sizeof ans);
         
         forn(i, N){
             if (us[i]) continue;
             ++ans[v[i].k];
             int t = v[i].t2 + T;
             int k = (v[i].k + 1) % 2;
             us[i] = 1;
             
             forn(j, N){
                 if (us[j]) continue;
                 if (v[j].t1 >= t && v[j].k == k){
                     us[j] = 1;
                     t = v[j].t2 + T;
                     k = (v[j].k + 1) % 2;
                 }
             }
             
         }   
            
         printf("Case #%d: %d %d\n", ii + 1, ans[0], ans[1]);
    }       
          
    return 0;
}

