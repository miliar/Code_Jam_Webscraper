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
const int MAXN = 100;
const int MAXM = 2000;

int mask[MAXN];
string s[MAXN];
char tmp[MAXN];
int a[MAXN][MAXM], cnt[MAXM];
bool can[MAXN][MAXM];
bool good[MAXM][MAXM];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
    
    mask[0] = 1;
    
    forn(i, 15){
        mask[i + 1] = 2 * mask[i];
    }   
    
    int tk;
    scanf("%d", &tk);
    int n, m;
    
    memset(good, 0, sizeof good);
        
    forn(i, mask[10]){
        forn(j, mask[10]){
            good[i][j] = 1;
            
            forn(k, 10){
                if (i & mask[k]){
                    if (j & mask[k]){
                        good[i][j] = 0;
                        break;
                    }
                    if (j & mask[k + 1]){
                        good[i][j] = 0;
                        break;
                    }
                    if (k){
                        if (j & mask[k - 1]){
                            good[i][j] = 0;
                            break;
                        }
                    }
                }
            }        
        }
    }

    forn(i, mask[10]){
        cnt[i] = 0;
        forn(k, 10){
            if (i & mask[k]) ++cnt[i];
        }
    }
    
    forn(ii, tk){    
        scanf("%d %d", &n, &m);   
             
        forn(i, n){
            scanf("%s", &tmp);
            s[i] = tmp;
        }
        
        forn(i, m + 1){
            forn(j, mask[n]){
                a[i][j] = -1;
                can[i][j] = 0;
            }
        }
        
        a[0][0] = 0;
                
        forn(i, m){
            forn(j, mask[n]){
                bool f = 1;
                forn(k, n){
                    if (j & mask[k]){
                        if (s[n - 1 - k][i] == 'x') f = 0;
                    }
                }
                can[i][j] = f;
            }
        }

        
        
        forn(i, m){
            forn(j, mask[n]){
                if (a[i][j] < 0) continue;
                forn(ma, mask[n]){
                    if (!can[i][ma]) continue;
                    if (!good[j][ma]) continue;
                    a[i + 1][ma] = max(a[i + 1][ma], a[i][j] + cnt[ma]);
                }
            }
        }
        int ans = -1;
        forn(i, m + 1){
            forn(j, mask[n]){
                ans = max(ans, a[i][j]);
            }
        }  
        printf("Case #%d: %d\n", ii + 1, ans);
    }
          
    return 0;
}

