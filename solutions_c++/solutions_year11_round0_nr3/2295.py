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

int solve(int x) {
    cout<<"Case #"<<x<<": ";
    long c[1111];
    long n,s,i,j,k;
    cin>>n;
    for (i = 1; i <= n; i++) cin>>c[i];
    s = c[1];
    for (i = 2; i <= n; i++) s = s xor c[i];
    if (s != 0) {
        cout<<"NO\n";
        return 0;
    }
    long min;
    min = 1111111;
    for (i = 1; i <= n; i++) if (c[i] < min) min = c[i];
    s = 0; 
    for (i = 1; i <= n; i++) s = s + c[i];
    cout<<s-min<<"\n";
}

int main() {
    freopen("C-large.in", "rt", stdin);
    freopen("c.out", "wt", stdout);
    int t,i,j;
    cin>>t;
    for (i = 1; i <= t; i++) {
        solve(i);
    }
};
