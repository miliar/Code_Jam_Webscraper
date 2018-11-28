#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define mp make_pair
#define sz(x) x.size()
using namespace std;

typedef long long ll;

ll ans, miss[2][5000][15];
int x, m[5000];

int main(void){int i, j, t, tt, p;
    
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(tt=0; tt<t; tt++){
              
          memset(miss, -1, sizeof(miss));    
          scanf("%d", &p);
          int n = 1 << p;
          int d = 0;
          fo(i,n){
                  scanf("%d", &x);
                  m[i] = x;
                  fo(j,(x+1)){
                          miss[d][i][j] = 0;
                          }
                  }
          
          n/=2;
          
          while(n){
                   fo(i,n){
                           scanf("%d", &x);
                           
                           fo(j,11){
                                    miss[1-d][i][j] = -1;
                                    if (miss[d][2*i][j+1] != -1 && miss[d][2*i+1][j+1] != -1)
                                       miss[1-d][i][j] = miss[d][2*i][j+1] + miss[d][2*i+1][j+1];
                                    if (miss[d][2*i][j] != -1 && miss[d][2*i+1][j] != -1 && 
                                       ( miss[1-d][i][j] == -1 || miss[1-d][i][j] > x + miss[d][2*i][j] + miss[d][2*i+1][j]))
                                         miss[1-d][i][j] = x + miss[d][2*i][j] + miss[d][2*i+1][j];
                                    }
                           
                           }
                   
                   d = 1-d;
                   n/=2;
                   }
          
          ans = ((ll) 100000000) * 100000000;
          fo(j,11)if(miss[d][0][j] != -1)ans = min(ans, miss[d][0][j]);
          cout << "Case #" << tt+1 << ": " << ans << endl;
    }   
    return 0;
}
