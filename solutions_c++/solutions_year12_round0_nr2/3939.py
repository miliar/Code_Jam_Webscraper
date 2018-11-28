#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int t, n, s, p;
int cnt1, cnt2;

int main() {
    freopen("a.txt", "r", stdin);
    freopen("a.out", "w", stdout);
    
    cin >> t;
    for (int cs = 1; cs <= t; ++cs) {
        cnt1 = cnt2 = 0;
        cin >> n >> s >> p;
        while (n--) {
            int total, p1 = 0, p2 = 0;
            cin >> total;
            for (int i = 0; i <= 10; ++i)
                for (int j = i; j <= 10 && j <= i + 2; ++j) {
                    int k = total - i - j;
                    if (k < j || k > 10 || k - i > 2) continue;
        
                    if (k >= p) {
                        if (k - i == 2) p2 = 1;
                            else p1 = 1;
                    }
                }
            if (p1) cnt1++;
                else if (p2) cnt2++;
        }
        printf("Case #%d: %d\n", cs, cnt1 + min(cnt2, s));
    }
}
