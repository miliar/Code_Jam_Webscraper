#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>

using namespace std;

typedef long long LL;


const int maxn = 1010;

int a[maxn];
multiset<int> cur;
int s[maxn];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int tests_num = 0;
    cin >> tests_num;
    
    for (int cur_test = 1; cur_test <= tests_num; ++cur_test) {
        
        int n;
        cin >> n;
        cur.clear();
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            cur.insert(a[i]);
            s[i] = 0;
        }
        
        int l = 0, r = n+1;
        
        if (n > 0) {
            while (r-l > 1) {
                int x = (l+r)/2;
                bool prov = true;
                cur.clear();
                for (int i = 0; i < n; ++i) {
                    s[i] = 0;
                    cur.insert(a[i]);
                }
                int m = 0;
                while (!cur.empty() && prov) {
                    bool p = false;
                    for (int i = 0; i < m; ++i) {
                        if (*cur.begin() == s[i]+1) {
                            ++s[i];
                            cur.erase(cur.begin());
                            p = true;
                            break;
                        }
                    }
                    if (!p) {
                        s[m] = *cur.begin();
                        cur.erase(cur.begin());
                        for (int i = 1; i < x; ++i) {
                            if (cur.empty() || cur.find(s[m]+1) == cur.end()) {
                                prov = false;
                                break;
                            } else {
                                cur.erase(cur.find(s[m]+1));
                                ++s[m];
                            }
                        }
                        ++m;
                    }
                }
                if (prov) {
                    l = x;
                } else {
                    r = x;
                }
            }
        }
        
        
        printf("Case #%d: ", cur_test);
        
        cout << l << endl;
    }
    

    return 0;
}