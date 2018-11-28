#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;


int main () 
{
    freopen ("input.txt", "rt", stdin);
    freopen ("output.txt", "wt", stdout);
  
    int t;
    cin >> t;
    for (int l = 0; l < t; ++l) {
        int n;
        cin >> n;
        vector <int> a (n), b (n);
        for (int i = 0; i < n; ++i)
            cin >> a[i] >> b[i];
        int res = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if  ((a[i] < a[j]) && (b[i] > b[j]))
                    res++;
        cout << "Case #" << l + 1 << ": " << res << endl;
    }
      
 
    
    return 0;
} 
