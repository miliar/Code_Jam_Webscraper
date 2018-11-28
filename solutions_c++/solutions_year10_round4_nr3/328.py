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

bool r[2][200][200];

int main(void){int t, tt, n, i, j, u, x1, y1, x2, y2;
    
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(tt=0; tt<t; tt++){
          int ans = 0, d = 0;
          bool exists;
          memset(r, 0, sizeof(r));
          
          scanf("%d", &n);
          fo(u,n){
                  scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
                  for(i = y1; i <= y2; i++)
                  for(j = x1; j <= x2; j++)
                        {
                             exists = true;
                             r[d][i][j] = 1;
                        }
                  }
          
          while(exists){
                   exists = false;
                   
                   for(i=1;i<103;i++)for(j=1;j<103;j++){
                                      r[1-d][i][j] = 0;
                                      if (r[d][i-1][j] == 1 && r[d][i][j-1] == 1) r[1-d][i][j] = 1;
                                      if (r[d][i][j] == 1 && (r[d][i-1][j] == 1 || r[d][i][j-1] == 1)) r[1-d][i][j] = 1;
                                      if (r[1-d][i][j]) exists = 1;
                                      }
                   d = 1-d;
                   ans ++;
                   }
          cout << "Case #" << tt+1 << ": " << ans << endl;
    }   
    return 0;
}
