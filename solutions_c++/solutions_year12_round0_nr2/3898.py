#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int solve(long rr){
    long a[111];
    long n,s,p,i,j;
    long res = 0;
    cin >> n >> s >> p;
    for (i = 0; i < n; i ++) cin >> a[i];
    for (i = 0; i < n; i ++) {
        j = a[i]/ 3;
        if (a[i] % 3 != 0) j ++;
        if (j >= p) res ++;
        else if (s > 0 && a[i] %3 != 1 && j == p-1 && a[i] > 1 && a[i] < 29) {
            res++; s--;
        }
    }
    cout << "Case #"<<rr+1<<": "<<res<<"\n";
}

int main() {
    freopen("a.inp","r",stdin);
    freopen("a.out","w",stdout);    
    long t,i,j;
    cin >> t;
    for (i = 0; i < t; i ++ ) {
        solve(i);
    }
}
