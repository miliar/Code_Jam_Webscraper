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
int t, m, v;
int gate[10010], changable[10010], dp[10010][2], l;

// Funtion Definitions
// ==============================

int main()
{
    int i, j;
    
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d", &m, &v);
        for (j = 1; j <= (m - 1) / 2; j++)
            scanf("%d %d", gate + j, changable + j);
        for (j = 1; j <= (m + 1) / 2; j++) {
            scanf("%d", &l);
            dp[(m - 1) / 2 + j][l] = 0;
            dp[(m - 1) / 2 + j][1 - l] = 1000000;
        }    
        for (j = (m - 1) / 2; j >= 1; j--) {
            if (gate[j]) {
                dp[j][1] = dp[j * 2][1] + dp[j * 2 + 1][1];
                dp[j][0] = dp[j * 2][1] + dp[j * 2 + 1][0];
                mini(dp[j][0], dp[j * 2][0] + dp[j * 2 + 1][1]);
                mini(dp[j][0], dp[j * 2][0] + dp[j * 2 + 1][0]);
            } else {
                dp[j][0] = dp[j * 2][0] + dp[j * 2 + 1][0];
                dp[j][1] = dp[j * 2][1] + dp[j * 2 + 1][1];
                mini(dp[j][1], dp[j * 2][0] + dp[j * 2 + 1][1]);
                mini(dp[j][1], dp[j * 2][1] + dp[j * 2 + 1][0]);
            }
            if (changable[j]) {
                if (gate[j]) {
                    mini(dp[j][0], dp[j * 2][0] + dp[j * 2 + 1][0] + 1);
                    mini(dp[j][1], dp[j * 2][0] + dp[j * 2 + 1][1] + 1);
                    mini(dp[j][1], dp[j * 2][1] + dp[j * 2 + 1][0] + 1);
                    mini(dp[j][1], dp[j * 2][1] + dp[j * 2 + 1][1] + 1);
                } else {
                    mini(dp[j][0], dp[j * 2][0] + dp[j * 2 + 1][0] + 1);
                    mini(dp[j][0], dp[j * 2][0] + dp[j * 2 + 1][1] + 1);
                    mini(dp[j][0], dp[j * 2][1] + dp[j * 2 + 1][0] + 1);
                    mini(dp[j][1], dp[j * 2][1] + dp[j * 2 + 1][1] + 1);
                }        
            }
        }
        printf("Case #%d: ", i + 1);    
        if (dp[1][v] >= 1000000)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", dp[1][v]);     
    }    
	
	return (0);
}

