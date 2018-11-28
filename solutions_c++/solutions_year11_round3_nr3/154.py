/*
 * Author: OldY
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
const int maxint = -1u>>1;
const double pi = acos(-1.0);


int T,n;
long long oth[110],l,r;

int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> n >> l >> r;
        for(int i = 0 ; i < n ; i++) cin >> oth[i];
        bool f = false;
        long long ans;
        for(ans = l ; ans <= r ; ans++){
            int i;
            for(i = 0 ; i < n ; i++){
                if(ans%oth[i] == 0 || oth[i]%ans == 0) continue;
                else break;
            }
            if(i == n && (ans%oth[n-1] == 0 || oth[n-1]%ans == 0)){
                f = true;
                break;
            }
        }
        cout << "Case #" << t << ": ";
        if(f) cout << ans << endl;
        else cout << "NO" << endl;
        
    }
    return 0;
}

