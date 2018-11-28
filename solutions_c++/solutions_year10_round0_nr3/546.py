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
    for (int l = 0; l < t; ++l) {
        int64 r, k, n;
        cin >> r >> k >> n;
        vector <int64> a(2*n);
        for (int64 i = 0; i < n; ++i)
            cin >> a[i];
        for (int64 i = 0; i < n; ++i)
            a[n + i] = a[i];
        vector <int64> res (n, 0), s (n, 0);
        for (int64 i = 0; i < n; ++i) {
            int64 x = 0;
            for (int64 j = 0; j < n; ++j) {
                x += a[i+j];
                if (x > k) {
                   res[i] = x - a[i+j];
                   s[i] = i + j;
                   if (s[i] >= n) s[i] -= n;
                   break;
                }
                if (j == n-1) {
                   res[i] = x;
                   s[i] = i;
                }
            }
        }
       
         
        int64 ans = 0;
        vector <bool> ok (n, false);
        int64 j = 0;
        ok[0] = true;
        int64 start;
        while (true)
            {       
                   j = s[j];
                   if (ok[j]) {
                              start = j;
                              break;
                   }
                   ok[j] = true;
            }
        j = start;
        int64 ans_from_start = res[j];
        int64 start_length = 1;
        while (true)
            {       
                   j = s[j];
                   if (j == start) break;
                   ans_from_start += res[j];
                   ++start_length;
            }
        j = 0;
        while (r > 0) {
              if (j == start) break;
              ans += res[j];
              j = s[j]; 
              r--;
        }
        
        ans += ((r / start_length) * ans_from_start);
        r %= start_length; 
       
        while (r > 0) {
              ans += res[j];
              j = s[j]; 
              r--;
        }
       
        
        cout << "Case #" << l + 1 << ": " << ans << endl;
        
        
        
       
        
    }
    
    return 0;
    
}
