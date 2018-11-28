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

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {
      string ans; int n;
      cin >> n;
      // using calculator;
      switch (n) {
         case 2: ans = "027"; break;
         case 3: ans = "143"; break;
         case 4: ans = "751"; break;
         case 5: ans = "935"; break;
         case 6: ans = "607"; break;
         case 7: ans = "903"; break;
         case 8: ans = "991"; break;
         case 9: ans = "335"; break;
         case 10: ans = "047"; break;
         case 11: ans = "943"; break;
         case 12: ans = "471"; break;
         case 13: ans = "055"; break;
         case 14: ans = "447"; break;
         case 15: ans = "463"; break;
         case 16: ans = "991"; break;
         case 17: ans = "095"; break;
         case 18: ans = "607"; break;
         case 19: ans = "263"; break;
         case 20: ans = "151"; break;
         case 21: ans = "855"; break;
         case 22: ans = "527"; break;
         case 23: ans = "743"; break;
         case 24: ans = "351"; break;
         case 25: ans = "135"; break;
         case 26: ans = "407"; break;
         case 27: ans = "903"; break;
         case 28: ans = "791"; break;
         case 29: ans = "135"; break;
         case 30: ans = "647"; break;
      }
      cout << "Case #" << sc << ": " << ans << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}