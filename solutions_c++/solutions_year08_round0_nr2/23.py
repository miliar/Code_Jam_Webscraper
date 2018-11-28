#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <set>

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

const int maxn = 220;

struct ride
{
   int l, r, d;
};

int t, n, m, ans[2];
string s;
ride a[maxn];

int Calc(const string& s)
{
   return ((s[0]-'0')*10 + (s[1]-'0'))*60 + (s[3]-'0')*10 + (s[4]-'0');
}

bool Less(const ride& a, const ride& b)
{
   if (a.l == b.l) return a.r < b.r;
   else return a.l < b.l;
}

int main()
{
   freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);

   int i, j, num;
   
   cin >> num;
   for (int sc = 1; sc <= num; sc++) {      
      cin >> t >> n >> m;
      for (i = 0; i < n+m; i++) {
         cin >> s; a[i].l = Calc(s);
         cin >> s; a[i].r = Calc(s);
         if (i < n) a[i].d = 0; else a[i].d = 1;
      }
      sort(a, a+m+n, Less);
      ans[0] = ans[1] = 0;
      multiset<int> trains[2];
      for (i = 0; i < n+m; i++) {
         multiset<int> &q = trains[a[i].d];
         if (q.size() && *(q.begin()) + t <= a[i].l) q.erase(q.begin());
         else ans[a[i].d]++;
         trains[1-a[i].d].insert(a[i].r);
      }
      cout << "Case #" << sc << ": " << ans[0] << " " << ans[1] << endl;
   }

   fclose(stdin); fclose(stdout);
   return 0;   
}