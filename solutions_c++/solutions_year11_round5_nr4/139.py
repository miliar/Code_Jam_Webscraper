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


const int maxn = 200;


char s[maxn];
char a[maxn];


void rec(int k, LL cur) {
    if (!s[k]) {
        LL d = sqrt(long double(cur));
        if (d*d == cur || (d+1)*(d=1) == cur) {
            strcpy(a, s);
        }
    } else {
        if (s[k] == '?') {
            s[k] = '0';
            rec(k+1, 2*cur);
            s[k] = '1';
            rec(k+1, 2*cur+1);
            s[k] = '?';
        } else {
            if (s[k] == '1') {
                cur = cur*2 + 1;
            } else {
                cur = cur*2;
            }
            rec(k+1, cur);
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int tests_num = 0;
    cin >> tests_num;
    
    for (int cur_test = 1; cur_test <= tests_num; ++cur_test) {
        
        memset(a, 0, sizeof(a));
        scanf("%s", s);
        
        rec(0, 0);
        
        printf("Case #%d: ", cur_test);
        printf("%s\n", a);
        
    }
    

    return 0;
}