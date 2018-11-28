//    Copyright (C) 2008, MDZfirst (King Arthur)
//    Latest modified: 2008/07/25 13:58
//
//    This file is used for me as a program template; you can use it and/or
//    redistribute it and/or modify it under the term that you keep all these
//    comments completely without any deletion.
//
//    Contact:
//    MDZfirst (King Arthur)
//    School of Computer Science and Technology
//    Tianjin University
//    China, 300072
//    mdzfirst@yahoo.com.cn
//    mdzfirst@gmail.com

#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <utility>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <functional>

using namespace std;

// C/C++ Operation Redefinitions
// ==============================
#define print(t, a) printf(#a " = %" #t "\n", a)
#define endl printf("\n")

#define fill(a, c) memset(&a, c, sizeof(a))
#define sqr(x) ((x) * (x))
#define mini(x, y) if ((y) < (x)) x = (y)
#define maxi(x, y) if ((x) < (y)) x = (y)

#define rep(i, a, b) for (i = (a); i < (b); i++)
#define repd(i, a, b) for (i = (b - 1); i >= (a); i--)
#define loop(n) for (int xyz(0); xyz < (n); xyz++)

// STL Redefinitions
// ==============================
#define itr iterator
#define ritr reverse_iterator
#define citr const_iterator

#define mp(x, y) make_pair((x), (y))
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define pob() pop_back()
#define pof() pop_front()
#define lb(x) lower_bound(x)
#define ub(x) upper_bound(x)

#define all(v) (v).begin(), (v).end()
#define each(ptr, v) for (ptr = (v).begin(); ptr != (v).end(); ++ptr)
#define eachd(ptr, v) for (ptr = (v).rbegin(); ptr != (v).rend(); ++ptr)

// Type Definitions
// ==============================
typedef long long ll;
typedef long double ld;

// Global Variable Definitions
// ==============================
ll t, n;
ll A, B, C, D, x, y, M;
ll cnt[3][3];
ll ans;

// Funtion Definitions
// ==============================

int main()
{
    int i, j, a, b, c, d, e, f;
    
    freopen("output2.txt", "w", stdout);
    
    scanf("%I64d", &t);
    for (i = 0; i < t; i++) {
        fill(cnt, 0);
        ans = 0;
        scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &A, &B, &C, &D, &x, &y, &M);
        for (j = 0; j < n; j++) {
            cnt[x % 3][y % 3]++;            
            x = (A * x + B) % M;
            y = (C * y + D) % M;
        }
                
        // 三个各不相同 
        for (x = 0; x < 9; x++)
            for (y = x + 1; y < 9; y++) {
                a = x / 3;
                b = x % 3;
                c = y / 3;
                d = y % 3;
                e = (6 - a - c) % 3;
                f = (6 - b - d) % 3;
                if (3 * e + f <= y)
                    continue;
                ans += cnt[a][b] * cnt[c][d] * cnt[e][f];
            }
        
        // 只有两个相同
        for (x = 0; x < 9; x++) {
            a = x / 3;
            b = x % 3;
            c = (6 - a - a) % 3;
            d = (6 - b - b) % 3;
            if (a == c && b == d)
                continue;
            ans += cnt[a][b] * (cnt[a][b] - 1) / 2 * cnt[c][d];
        }     
        
        // 三个都相同
        for (x = 0; x < 9; x++) {
            a = x / 3;
            b = x % 3;
            ans += cnt[a][b] * (cnt[a][b] - 1) * (cnt[a][b] - 2) / 6;
        }  
        
        printf("Case #%d: %I64d\n", i + 1, ans);
    }    
	
	return (0);
}

