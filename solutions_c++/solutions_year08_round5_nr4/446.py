//    Copyright (C) 2008, MDZfirst (King Arthur)
//    Latest modified: 2008/08/05 13:18
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
#include <ctime>
#include <cctype>
#include <complex>
#include <memory>

#pragma comment(linker, "/STACK:60777216")

// C/C++ Operation Redefinitions
// ==============================
#define print(t, a) printf(#a " = %" #t "\n", a)
#define endl printf("\n")

#define fill(a, c) memset(&(a), c, sizeof(a))
#define copy(a, c) memcpy(&(a), &(c), sizeof(a))
#define sqr(x) ((x) * (x))
#define abs(x) ((x < 0) ? - (x) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((y) < (x) ? (x) : (y))
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

#define fi first
#define se second

#define mp make_pair
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define lb lower_bound
#define ub upper_bound
#define np next_permutation
#define pp prev_permutation

#define all(v) (v).begin(), (v).end()
#define each(ptr, v) for (ptr = (v).begin(); ptr != (v).end(); ++ptr)
#define eachd(ptr, v) for (ptr = (v).rbegin(); ptr != (v).rend(); ++ptr)
#define has(v, a) v.find(a) != v.end()

using namespace std;

// Type Definitions
// ==============================
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

// Global Variable Definitions
// ==============================
int t, H, W, R, r, c;
int board[100][100], dp[100][100];

// Funtion Definitions
// ==============================

int main()
{
    int i, j, k;
    
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d %d", &H, &W, &R);
        fill(board, 0);
        fill(dp, 0);
        for (j = 0; j < R; j++) {
            scanf("%d %d", &r, &c);
            board[r - 1][c - 1] = 1;
        }
        
        dp[0][0] = 1;
        
        for (j = 0; j < H; j++)
            for (k = 0; k < W; k++)
                if (board[j][k] == 0) {
                    dp[j][k] %= 10007;
                    if (j + 2 < H && k + 1 < W)
                        dp[j + 2][k + 1] += dp[j][k];
                    if (j + 1 < H && k + 2 < W)
                        dp[j + 1][k + 2] += dp[j][k];
                }    
        
        printf("Case #%d: %d\n", i + 1, dp[H - 1][W - 1] % 10007);
    }    
	
 	return (0);
}

