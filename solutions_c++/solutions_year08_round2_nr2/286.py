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
int is_prime[10000];
int prime_num;
int prime[10000];

int UFS[10000];
int t, A, B, P, ans;

// Funtion Definitions
// ==============================
void init()
{
    int i, j;
    
    fill(is_prime, -1);
    for (i = 2; i * i < 10000; i++)
        if (is_prime[i])
            for (j = i * i; j < 10000; j += i)
                is_prime[j] = 0;
    prime_num = 0;
    for (i = 2; i < 10000; i++)
        if (is_prime[i])
            prime[prime_num++] = i;
}    

int root(int p)
{
    if (UFS[p] == p)
        return (p);
    else
        return (root(UFS[p]));
}    

void unite(int a, int b)
{
    UFS[root(a)] = root(b);
}    

int main()
{
    int i, j, k, l;
    
    freopen("output.txt", "w", stdout);
    
    init();
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d %d", &A, &B, &P);
        for (j = A; j <= B; j++)
            UFS[j] = j;
        for (j = 0; j < prime_num; j++)
            if (prime[j] < P)
                continue;
            else if (prime[j] > B)
                continue;
            else {
                for (k = 1; k * prime[j] < A; k++)
                    ;
                for (l = k + 1; l * prime[j] <= B; l++)
                    if (root(l * prime[j]) != root(k * prime[j]))
                        unite(l * prime[j], k * prime[j]);
            }
        ans = 0;
        for (j = A; j <= B; j++)
            if (UFS[j] == j)
                ans++;
        printf("Case #%d: %d\n", i + 1, ans);
    }    
	
	return (0);
}



