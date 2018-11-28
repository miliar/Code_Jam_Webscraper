#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long
#define ld long double

const ld EPS = 1e-9;
const int MAXN = 2000;

int a[MAXN], b[MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
    int tk, n;
    cin >> tk;
    
    forn(ii, tk){
        scanf("%d", &n);
        
        forn(i, n){
            scanf("%d", &a[i]);
        }
        
        forn(i, n){
            scanf("%d", &b[i]);
        }
        sort(a, a + n);
        sort(b, b + n);
        reverse(a, a + n);
        ll res = 0;
        forn(i, n){
                ll cur = a[i];
                cur *= b[i];
                res += cur;
        }
        printf("Case #%d: ", ii + 1);
        cout << res << endl;
    }   
          
    return 0;
}

