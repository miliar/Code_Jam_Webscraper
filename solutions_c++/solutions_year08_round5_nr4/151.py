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
const int MAXN = 110;
const int BASE = 10007;

int x[MAXN], y[MAXN];
int a[MAXN][MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
    int tk;
    scanf("%d", &tk);
    int n, m, r;
    
    forn(ii, tk){    
        scanf("%d %d %d", &n, &m, &r);   
             
        forn(i, r){
            scanf("%d %d", &x[i], &y[i]);
        }
        
        memset(a, 0, sizeof a);
        a[1][1] = 1;
        
        forn(i, n + 1){
            forn(j, m + 1){
                bool f = 1;
                forn(k, r){
                    if (i == x[k] && j == y[k]) f = 0;
                }
                if (!f) continue;
                a[i + 1][j + 2] += a[i][j];
                a[i + 1][j + 2] %= BASE;
                
                a[i + 2][j + 1] += a[i][j];
                a[i + 2][j + 1] %= BASE;
            }
        }
        
        printf("Case #%d: %d\n", ii + 1, a[n][m]);
    }
          
    return 0;
}

