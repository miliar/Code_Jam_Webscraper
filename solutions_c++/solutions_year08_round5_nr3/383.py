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
int t, m, n;
int ans, temp, a, b;
char room[100][100];
int tag[100][100];
int cnt[100][100];

// Funtion Definitions
// ==============================
int _not(int r, int c)
{
    if (! (0 <= r && r < m))
        return (1);
    if (! (0 <= c && c < n))
        return (1);
    if (tag[r][c])
        return (0);
    return (1);
}    

void dfs(int r, int c)
{
    if (r == m && c == 0) {
        maxi(ans, temp);
        return;
    }
    
    if (temp + cnt[r][c] <= ans ||
        temp + (m - r) * n / 2 <= ans)
        return;
    
    if (room[r][c] == '.' &&
        _not(r - 1, c - 1) &&
        _not(r - 1, c + 1) &&
        _not(r, c - 1)) {
        tag[r][c] = 1;
        temp++;
        if (c == n - 1)
            dfs(r + 1, 0);
        else
            dfs(r, c + 1);
        temp--;
        tag[r][c] = 0;
    }
    
    if (c == n - 1)
        dfs(r + 1, 0);
    else
        dfs(r, c + 1);
}    

int main()
{
    int i, j, k;
    
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d", &m, &n);
        for (j = 0; j < m; j++)
            scanf("%s", room[j]);
            
        a = b = 0;
        for (j = 0; j < m; j++)
            for (k = 0; k < n; k++)
                if (k % 2 == 0 && room[j][k] == '.')
                    a++;
                else if (k % 2 == 1 && room[j][k] == '.')
                    b++;  
                    
        // print(d, a);
        // print(d, b);
                    
        ans = max(a, b); 
        
        // print(d, ans);
        
        fill(cnt, 0);
        if (room[m - 1][n - 1] == '.')
            cnt[m - 1][n - 1] = 1;
        for (j = m - 1; j >= 0; j--)
            for (k = n - 1; k >= 0; k--) {
                if (j != m - 1 || k != n - 1) {
                    if (room[j][k] == '.')
                        cnt[j][k] = 1;
                    if (k == n - 1)
                        cnt[j][k] += cnt[j + 1][0];
                    else
                        cnt[j][k] += cnt[j][k + 1];
                }    
            }             
            
        /*
        for (j = 0; j < m; j++) {
            for (k = 0; k < n; k++)
                printf("%d ", cnt[j][k]);
            endl;
        }    
        continue;
        */
            
        fill(tag, 0);
        temp = 0;
        
        dfs(0, 0);
            
        printf("Case #%d: %d\n", i + 1, ans);
    }    
	
 	return (0);
}

