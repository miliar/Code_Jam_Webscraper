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

int a[MAXN][MAXN], b[MAXN][MAXN], d[MAXN], t[MAXN];
bool us[MAXN];

int mask[MAXN];
int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
    int tk, n, m;
    cin >> tk;
    
    mask[0] = 1;
    
    forn(i, 20){
        mask[i + 1] = 2 * mask[i];
    }
    
    forn(ii, tk){
        scanf("%d", &n);
        scanf("%d", &m);

        forn(i, m){
            scanf("%d", &t[i]);
            
            forn(j, t[i]){
                scanf("%d %d", &a[i][j], &b[i][j]);
                --a[i][j];
            }
        }
        
        int res = n + 1, m1 = 0;
        
        forn(ma, mask[n]){
            int cnt = 0;
            
            forn(i, n){
                d[i] = 0;
                if (ma & mask[i]){
                    d[i] = 1;
                    ++cnt;
                }
            }

            forn(i, m){
                bool f = 0;
                forn(j, t[i]){
                    int x = a[i][j], y = b[i][j];
                
                    if (d[x] == y){
                        f = 1;
                    } 
                }
                if (!f) cnt = n + 2;
            }
            if (cnt < res){
               res = cnt;
               m1 = ma;
            }

        }

        printf("Case #%d: ", ii + 1);

        if (res < n + 1){
            forn(i, n){
                int x = 0;
                if (m1 & mask[i]) x = 1;
                
                printf("%d ", x);
            }
            printf("\n");
        }
        else
            printf("IMPOSSIBLE\n");
    }   
          
    return 0;
}

