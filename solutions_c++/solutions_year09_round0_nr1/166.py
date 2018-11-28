#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef long double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

int L, d, n, can[15][26];
VS a;

int main()
{
   freopen("input.txt" ,"rt", stdin); freopen("output.txt", "wt", stdout);
   int i, j, k;
   string s;
   
   cin >> L >> d >> n;
   getline(cin, s);
   for (i = 0; i < d; i++) {
      getline(cin, s);
      a.PB(s);
   }
   for (int sc = 0; sc < n; sc++) {
      getline(cin, s);
      memset(can, 0, sizeof(can));
      k = 0; 
      for (i = 0; i < L; i++) {
         if (s[k] >= 'a' && s[k] <= 'z') {
            can[i][s[k]-'a'] = 1;
         } else {
            while (s[++k] != ')')
               can[i][s[k]-'a'] = 1;
         }
         k++;
      }
      
      int ans = 0;
      for (i = 0; i < d; i++) {
         int ok = 1;
         for (j = 0; j < L; j++)
            if (!can[j][a[i][j]-'a']) {ok = 0; break;}
         ans += ok;
      }
      
      cout << "Case #" << sc+1 << ": " << ans << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}