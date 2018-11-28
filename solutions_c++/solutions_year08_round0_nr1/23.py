#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>

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

const int maxn = 110;
const int maxk = 1010;

string tmp, s[maxn], q[maxk];
int n, k, seq[maxk], a[maxn];

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {      
      cin >> n; getline(cin, tmp);
      for (i = 0; i < n; i++) getline(cin, s[i]);
      cin >> k; getline(cin, tmp);
      for (i = 0; i < k; i++) {
         getline(cin, tmp);
         for (j = 0; j < n; j++) if (s[j] == tmp) break;
         seq[i] = j;
      }
      
      i = 0; int ans = -1;
      while (i < k) {
         memset(a, 255, sizeof(a));
         int best = -1;
         for (j = i; j < k; j++)
            if (a[seq[j]] < 0) {
               a[seq[j]] = j; best = j;
            }
         for (j = 0; j < n; j++) 
            if (a[j] < 0) {best = k; break;}
         i = best; ans++;
      }
      if (ans < 0) ans = 0;
      cout << "Case #" << sc << ": " << ans << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}