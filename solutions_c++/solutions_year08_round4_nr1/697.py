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
const int MAXN = 11000;
const int INF = (int)(1e8 + 1e-8);

int a[MAXN][2], b[MAXN][2], g[MAXN], ch[MAXN];
bool counted[MAXN];

void go(int v){
    if (counted[v]) return;
    counted[v] = 1;
    go(2 * v);
    go(2 * v + 1);
    
    forn(p, 2){
        if (b[v][p] < INF){
            forn(i, 2){
                if (a[2 * v][i] > INF - 1) continue;
                
                forn(j, 2){
                    if (a[2 * v + 1][j] > INF - 1) continue;
                    int val = 0;
                    
                    if (p) val = i & j;
                    else
                        val = i | j; 
                    a[v][val] = min(a[v][val], b[v][p] + a[2 * v][i] + a[2 * v + 1][j]);   
                }
            }      
        }
    }
}

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("output.txt", "wt", stdout);    

    int tk;
    scanf("%d", &tk);   
    
    forn(ii, tk){
       int n, v;
       
       scanf("%d %d", &n, &v);

       forn(i, n + 1){
           g[i] = -1;
           ch[i] = -1;
           forn(j, 2){
               a[i][j] = INF;
               b[i][j] = INF;
           }
           counted[i] = 0;
       }
       
       
       forn(i, (n - 1) / 2){
           scanf("%d %d", &g[i + 1], &ch[i + 1]);
           
           b[i + 1][g[i + 1]] = 0;
           
           if (ch[i + 1]){
              b[i + 1][(g[i + 1] + 1) % 2] = 1;
           }
       }
       
       forn(i, (n + 1) / 2){
           scanf("%d", &g[(n - 1) / 2 + i + 1]);
           a[(n - 1) / 2 + i + 1][g[(n - 1) / 2 + i + 1]] = 0;
           counted[(n - 1) / 2 + i + 1] = 1;
       }
       fore(i, 1, n + 1){
           go(i);
       }
       printf("Case #%d: ", ii + 1);
   
       if (a[1][v] > INF - 1){
          printf("IMPOSSIBLE\n");
       }
       else
          printf("%d\n", a[1][v]);
       
       
    }          
    return 0;
}

