#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define VI vector<int>
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const int maxn = 3010;
const int r = 3005;
const int g = 8192;
const int dx[4] = {0,1,0,-1};
const int dy[4] = {1,0,-1,0};

string s, t2;
char eu[g][g],ed[g][g],el[g][g],er[g][g];
char wu[g][g],wd[g][g],wl[g][g],wr[g][g];

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      int t;
      cin >> t; s = "";
      for (i = 1; i <= t; i++) {
         int t1;
         cin >> t2 >> t1;
         for (j = 1; j <= t1; j++) s += t2;
      }
      
      int x=maxn,y=maxn,d=0;
      for (i = 0; i < s.length(); i++) {
         switch (s[i]) {
            case 'L':
               d--; if (d < 0) d = 3;
               break;
            case 'R':
               d++; if (d > 3) d = 0;
               break;
            case 'F':
               switch (d) {
                  case 0:
                     er[y][x-1] = el[y][x] = sc;
                     break;
                  case 1:
                     ed[x][y] = eu[x][y-1] = sc;
                     break;
                  case 2:
                     er[y-1][x-1] = el[y-1][x] = sc;
                     break;
                  case 3:
                     ed[x-1][y] = eu[x-1][y-1] = sc;
                     break;
               }
               x += dx[d]; y += dy[d];
               break;
         }
      }
      
      int st = -r+maxn, fin = r+maxn;
      
      for (x = -r; x <= r; x++) {
         int cur = 0, xx = x+maxn;
         for (y = fin; y >= st; y--) {
            if (eu[xx][y] == sc) {if (!cur) cur = 1; else cur = 3-cur;}
            wu[xx][y] = cur;
         }
         cur = 0;
         for (y = st; y <= fin; y++) {
            if (ed[xx][y] == sc) {if (!cur) cur = 1; else cur = 3-cur;}
            wd[xx][y] = cur;
         }
      }
      for (y = -r; y <= r; y++) {
         int cur = 0, yy = y+maxn;
         for (x = fin; x >= st; x--) {
            if (er[yy][x] == sc) {if (!cur) cur = 1; else cur = 3-cur;}
            wr[yy][x] = cur;
         }
         cur = 0;
         for (x = st; x <= fin; x++) {
            if (el[yy][x] == sc) {if (!cur) cur = 1; else cur = 3-cur;}
            wl[yy][x] = cur;
         }
      }
      
      int ans = 0;
      for (x = st; x <= fin; x++)
         for (y = st; y <= fin; y++)
            if (wl[y][x] == 2 && wr[y][x] == 2 || 
                wu[x][y] == 2 && wd[x][y] == 2)
                   ans++;
      
      cout << "Case #" << sc << ": ";
      cout << ans;
      cout << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}