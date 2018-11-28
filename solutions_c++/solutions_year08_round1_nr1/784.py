#include <iostream>
using namespace std;

const int maxN = 800;
int v1[maxN], v2[maxN];
int n;

bool cmp(const int& a, const int& b)
{
   return a > b;
}

void work(int cases)
{
   sort(v1, v1 + n);
   sort(v2, v2 + n, cmp);
   int ans = 0;
   for(int i = 0; i < n; i++)
      ans += v1[i]*v2[i];
   cout << "Case #" << cases << ": " << ans << endl;
}
int main()
{
   freopen("A-small-attempt0.in","r", stdin);
   freopen("A-small-attempt0.out","w", stdout);
   int t, i, j;
   cin >> t;
   for(i = 1; i <= t; i++)
   {
      cin >> n;
      for(j = 0; j < n; j++)
         cin >> v1[j];
      for(j = 0; j < n; j++)
         cin >> v2[j];
      work(i);
   }
}
