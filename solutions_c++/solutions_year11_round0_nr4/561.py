/*
 * Author: OldY
 * Created Time:  2011/5/7 13:16:44
 * File Name: D.cpp
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

int T,n,tmp;
double ans;

int main() {
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> n;
        ans = n;
        for(int i = 1 ; i <= n ; i++){
            cin >> tmp;
            if(i == tmp) ans -= 1.0;
        }
        printf("Case #%d: %.6f\n",t,ans);
    }
    return 0;
}

