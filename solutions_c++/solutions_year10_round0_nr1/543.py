#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <set>
#include <map>



#define for0(i,n) for (int i = 0; i < n; i++)
#define for1(i,n) for (int i = 1; i <= n; i++)
#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

int main () {
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
  
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        int64 n, k;
        cin >> n >> k;
        ++k;
        cout << "Case #" << i + 1 << ": ";
        if ((k % (1 << n)) == 0) cout << "ON" << endl;
        else cout << "OFF" << endl;
        
        
        
    }
    
}
