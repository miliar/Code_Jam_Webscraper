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
const int MAXN = 6010;
const int SH = 3002;

//const int MAXN = 310;
//const int SH = 122;

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

char tmp[MAXN];
bool a[MAXN][MAXN];
short b[MAXN][MAXN];

int mask[MAXN];
bool da[MAXN];
string s;
int x11[MAXN], y11[MAXN];
int x22[MAXN], y22[MAXN];

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    

    mask[0] = 1;

    forn(i, 10){
        mask[i + 1] = 2 * mask[i];
    }
       
    int tk;
    scanf("%d", &tk);
    int n, m;
    
    memset(da, 0, sizeof da);
    forn(ma, mask[4]){
        if (ma & mask[0]){
           if (ma & mask[1]){
              da[ma] = 1;
           }
        }
        if (ma & mask[2]){
           if (ma & mask[3]){
              da[ma] = 1;
           }
        }

    }
    
    forn(ii, tk){    
        scanf("%d", &n);   
        int t, k = 1, X = SH, Y = SH;
        memset(a, 0, sizeof a);
        a[X][Y] = 1;
        
//        int x1 = 0, x2 = 0, y1 = 0, y2 = 0;
        
        forn(i, MAXN){
            x11[i] = MAXN - 1;
            x22[i] = -MAXN + 1;
            
            y11[i] = MAXN - 1;
            y22[i] = -MAXN + 1;
        }
        
        x11[SH] = 0;
        x22[SH] = 0;
        y11[SH] = 0;
        y22[SH] = 0;
        
        ll sum = 0;
        
        forn(i, n){
            scanf("%s", &tmp);
            s = tmp;
            scanf("%d", &t);
            
            forn(jj, t){
                forn(j, s.size()){
                    if (s[j] == 'F'){
                        X += dx[k];
                        Y += dy[k];

                        a[X][Y] = 1;
                        sum += dx[k] * Y;   
                        
                        x11[Y] = min(x11[Y], X);
                        x22[Y] = max(x22[Y], X);
                        
                        y11[X] = min(y11[X], Y);
                        y22[X] = max(y22[X], Y);
                    }
                    
                    if (s[j] == 'R'){
                       k += 1;
                       while (k > 3) k -= 4;
                    }
                    
                    if (s[j] == 'L'){
                       k += 3;
                       while (k > 3) k -= 4;
                    }                    
                }
            }
        }

        if (sum < 0) sum = -sum;
        //cout << sum << endl;
        
        memset(b, 0, sizeof b);

//        /*        
        forn(i, MAXN){
            int ma = 0;
            fore(j, y11[i], y22[i] + 1){
                if (a[i][j]) ma = 1;
                b[i][j] += ma;    
            }
        }

        forn(i, MAXN){
            int ma = 0;
            for(int j = y22[i]; j > y11[i] - 1; --j){
                if (a[i][j]) ma = 2;
                b[i][j] += ma;    
            }
        }

        forn(j, MAXN){
            int ma = 0;
            fore(i, x11[j], x22[j] + 1){
                if (a[i][j]) ma = 4;
                b[i][j] += ma;    
            }
        }

        forn(j, MAXN){
            int ma = 0;
            for(int i = x22[j]; i > x11[j] - 1; --i){
                if (a[i][j]) ma = 8;
                b[i][j] += ma;    
            }
        }

        int ans = -sum;        
  //      /*
        forn(i, MAXN){
            forn(j, MAXN){
                if (!da[b[i][j]]) continue;
                if (da[b[i + 1][j]] && da[b[i + 1][j + 1]] && da[b[i][j + 1]]) ++ans;
            }
        }
//        */
        printf("Case #%d: %d\n", ii + 1, ans);
    }
          
    return 0;
}

