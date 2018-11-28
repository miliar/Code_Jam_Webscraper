/*
 * =====================================================================================
 *
 *       Filename:  b.cpp
 *
 *    Description:  b
 *
 *        Version:  1.0
 *        Created:  2010/5/23 0:38:15
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *        Company:  
 *
 * =====================================================================================
 */


#include	<iostream>
using namespace std;
#define MAXN 50
#define INF 1<<30
typedef long long int64;

int64 p[MAXN], v[MAXN];

int64 solve() {
    int64 n,k,b,t;
    cin >> n >> k >> b >>t;
    for (int64 i=0; i<n; i++) cin >> p[i];
    for (int64 i=0; i<n; i++) cin >> v[i];
    
    int succ_count = 0;
    int swap_count = 0;
    for (int i=n-1; i>=0; i--) {
        if (p[i]+v[i]*t < b) continue;
        succ_count ++;
        for (int j=i+1; j<n; j++) {
            if (v[j]<v[i]) {
                if ( (v[i]-v[j])*(p[j]-p[i]) + t*v[j]*(v[i]-v[j]) < (b-p[i])*(v[i]-v[j]) )
                    swap_count ++;
            }
        }
        if (succ_count >= k) break;
    }

    if (succ_count < k)
        return -1;
    else
        return swap_count;
}

int main() {
    int64 T;
    cin >> T;
    for (int64 t=0; t<T; t++) {
        int64 ret = solve();
        cout << "Case #" << (t+1) << ": ";
        if (ret==-1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ret << endl;
    }
}
