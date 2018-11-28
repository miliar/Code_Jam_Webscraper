/*
 * Author: OldY
 * Created Time:  2011/5/7 11:29:02
 * File Name: C.cpp
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

int ans,cnt,tmp,sum;
int T,n;

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> n;
        ans = maxint;
        cnt = 0;
        sum = 0;
        for(int i = 0 ; i < n ; i++){
            cin >> tmp;
            sum += tmp;
            cnt ^= tmp;
            ans = min(ans , tmp);
        }
        cout << "Case #" << t << ": ";
        if(cnt == 0) cout << sum-ans << endl;
        else cout << "NO" << endl;
    }
    return 0;
}

