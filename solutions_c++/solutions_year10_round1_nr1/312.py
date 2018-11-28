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

char a[100][100];
int b[100][100];
int n, k;

int sumright(int x, int y){int j, sum = 0;
    for(j=y;j<y+k && j<n;j++)sum+=b[x][j];
    return sum;
}

int sumdown(int x, int y){int j, sum = 0;
    for(j=x;j<x+k && j<n;j++)sum+=b[j][y];
    return sum;
}

int sumdgr(int x, int y){int j, sum = 0;
    fo(j,k)if(x+j < n && y+j < n)sum+=b[x+j][y+j];
    return sum;
}

int sumdgl(int x, int y){int j, sum = 0;
    fo(j,k)if(x+j < n && y-j > -1 )sum+=b[x+j][y-j];
    return sum;
}

int main(void){int i, j, l, t, tt;
    
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    fo(tt, t){
          scanf("%d%d\n", &n, &k);
          fo(i,n)gets(a[i]);
          bool red, blue;
          red = blue = false; //red = 1, blue = -1
          
          memset(b, 0, sizeof(b));
          for(i=n-1;i>-1;i--){
                  l = n-1;
                  for(j=n-1;j>-1;j--){
                          if (a[i][j] == 'R')b[l--][n-i-1] = 1;
                          if (a[i][j] == 'B')b[l--][n-i-1] = -1;
                          }
                  if (l == n-1) break;
                  }
          
          /*
          fo(i,n){
                  fo(j,n){
                          if (b[i][j] == 1) cout << "R"; else if (b[i][j] == -1) cout << "B"; else cout << ".";
                          }
                  cout << "\n";
                  }
          */
                  
          fo(i,n)fo(j,n)if(b[i][j]!=0){
                                     if (sumright(i,j) == k || sumdown(i,j) == k || sumdgr(i,j) == k || sumdgl(i,j) == k) red = true;
                                     if (sumright(i,j) == -k || sumdown(i,j) == -k || sumdgr(i,j) == -k || sumdgl(i,j) == -k) blue = true;
                                     }
          
          string ans;
          if (red && blue) ans = "Both";
          if (red && !blue) ans = "Red";
          if (!red && blue) ans = "Blue";
          if (!red && !blue) ans = "Neither";
          cout << "Case #" << tt+1 << ": " << ans << endl;
    }
    return 0;
}
