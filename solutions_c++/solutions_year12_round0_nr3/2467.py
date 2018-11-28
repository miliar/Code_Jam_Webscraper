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
#include <cstring>
#define PI 3.141592653589793238

using namespace std;

int ntest;

bool ok(int x, int y) {
     //cout << x << ' ' << y << endl;
     string s1 = "";
     while (x > 0) {
           s1 = char((x % 10) + '0') + s1;
           x /= 10;
     }
     string s2 = "";
     while (y > 0) {
           s2 = char((y % 10) + '0') + s2;
           y /= 10;
     }
     if (s1.length() != s2.length()) return false;
     for (int i = 0; i < s1.length() - 1; i++) {
         s1 = s1.substr(1) + s1[0];
         if (s1 == s2) return true;
         //cout << s1 << endl;
     }
     return false;
}

int main() {
    freopen("3.inp", "r", stdin);
    freopen("03.out", "w", stdout);
    
    scanf("%d", &ntest);
    for (int test = 1; test <= ntest; test++) {
        int a, b;
        scanf("%d%d", &a, &b);
        set< pair<int, int> > se;
        for (int i = a; i < b; i++) {
            string s = "";
            int tmp = i;
            while (tmp > 0) {
                  s = char((tmp % 10) + '0') + s;
                  tmp /= 10;
            }
            for (int j = 0; j < s.length() - 1; j++) {
                s = s.substr(1) + s[0];
                tmp = 0;
                for (int k = 0; k < s.length(); k++)
                    tmp = tmp * 10 + (s[k] - '0');
                if (tmp > i && tmp <= b) 
                   se.insert(make_pair(i, tmp));
            }
        }
        cout << "Case #" << test << ": " << se.size() << endl;
    }
}
