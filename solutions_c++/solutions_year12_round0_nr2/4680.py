#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


int main() 
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    
    int T;
    scanf("%d\n", &T);
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int n, s, p;
        cin >> n >> s >> p;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] >= 2 && s > 0) {
               if (a[i] >= p + max(p - 2, 0) * 2) {
                   --s;
                   ++res;
               }
            } else {
               if (a[i] >= p + max(p - 1, 0) * 2) ++res;
            }
        }
        
        printf("%d\n", res);
    }
    
    
    
    return 0;
}

