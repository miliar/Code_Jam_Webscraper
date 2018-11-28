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

const int maxn = 1010;

TT n, a[maxn], b[maxn];

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      cin >> n;
      for (i = 0; i < n; i++) cin >> a[i];
      for (i = 0; i < n; i++) cin >> b[i];
      sort(a, a+n); sort(b, b+n);
      TT ans = 0;
      for (i = 0; i < n; i++) ans += a[i] * b[n-i-1];
      cout << "Case #" << sc << ": " << ans << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}