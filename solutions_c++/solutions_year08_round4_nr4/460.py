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
int t, k;
vector<int> v;
char str[1010], temp[1010];
int ans;

// Funtion Definitions
// ==============================
void done()
{
    int i, j;
    int cnt;
 
    for (i = 0; str[i]; i += k)
        for (j = 0; j < k; j++)
            temp[i + j] = str[i + v[j]];
    cnt = 0;
    for (i = 0; str[i]; i++)
        if (i == 0 || temp[i] != temp[i - 1])
            cnt++;
    mini(ans, cnt);
}    

int main()
{
    int i, j;
    
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %s", &k, str);
        v.clear();
        for (j = 0; j < k; j++)
            v.pb(j);
        ans = 1000000;
        while (1) {
            done();
            if (! next_permutation(v.begin(), v.end()))
                break;
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }    
	
	return (0);
}

