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


int T;
long long n,pd,pg;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> n >> pd >> pg;
        bool can = false;
        long long tmp = 100LL/__gcd(100LL,pd);
        if(pd == 0LL || pg == 0LL){
            if(pd == pg) can = true;
        }
        else{
            if(tmp <= n){
                if(pg == 100LL){
                    if(pd == 100LL) can = true;
                }
                else can = true;
            }
        }
        cout << "Case #" << t << ": ";
        if(can) cout << "Possible" << endl;
        else cout << "Broken" << endl;        
    }
    return 0;
}

