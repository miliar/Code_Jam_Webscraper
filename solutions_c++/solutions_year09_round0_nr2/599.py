#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)

#define ll long long
#define ld long double
#define PII pair <int, int>

#define x first
#define y second

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

/*
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
*/
const ld EPS = 1e-9;
const int MAXN = 200;

int a[MAXN][MAXN];
int us[MAXN][MAXN];
PII w[MAXN * MAXN];
char ans[MAXN][MAXN];
int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    
       
    int tk;
    cin >> tk;
    
    forn(ii, tk){
        int n, m;
        cin >> n >> m;
        
        forn(i, n){
            forn(j, m){
                scanf("%d", &a[i][j]);
                ans[i][j] = ' ';
            }
        }
        
        memset(us, 0, sizeof us);
        
        int cnt = 0;
        
        forn(i, n){
            forn(j, m){
                if (!us[i][j]){
                   us[i][j] = 1;
                   w[0] = PII(i, j);
                   
                   int t = 1;
                   
                   while (true){
                       int x = w[t - 1].x;
                       int y = w[t - 1].y;
                       int nx, ny, mx = (int)(1e7 + 1e-7), K = -1;
                       
                       forn(k, 4){
                           nx = x + dx[k];
                           ny = y + dy[k];
                           
                           if (nx < 0 || nx > n - 1) continue;
                           if (ny < 0 || ny > m - 1) continue;
                           if (a[nx][ny] < a[x][y] && a[nx][ny] < mx){
                              mx = a[nx][ny];
                              K = k;
                           }                           
                       } 
                       
                       if (K == -1) break;
                       
                       w[t] = PII(x + dx[K], y + dy[K]);
                       ++t;
                       if (us[x + dx[K]][y + dy[K]]) break;
                       us[x + dx[K]][y + dy[K]] = 1;
                   }
                   
                   if (ans[w[t - 1].x][w[t - 1].y] == ' ') {
                      ans[w[t - 1].x][w[t - 1].y] = 'a' + cnt;
                      ++cnt;
                   }
                   
                   for(int k = t - 1; k > -1; --k){
                       ans[w[k].x][w[k].y] = ans[w[t - 1].x][w[t - 1].y];
                   }
                }
            }
        }
        
        printf("Case #%d:\n", ii + 1);
                
        forn(i, n){
            forn(j, m){
                //if (j + 1 < m) 
                    printf("%c ", ans[i][j]);
//                else
//                    printf("%c\n", ans[i][j]);
            }
            printf("\n");
        }
    }          
    return 0;
}

