#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

int main() 
{
   int T;
   int n, s, p, cnt;
   double pts[1001];
   cin  >> T;

   for(int t = 1; t <= T; t++)
   {
      cnt = 0;
      cin >> n >> s >> p;
      for(int i = 0; i < n; i++)
         cin >> pts[i];

      for(int i = 0; i < n; i++)
      {

         //cout <<  pts[i]-p << endl;
         if( pts[i]-p >= (p-1)*2 && pts[i]-p >= 0) cnt++;
         else if(pts[i]-p >= (p-2)*2 && s && pts[i]-p >= 0) { cnt++; s--; }
      }

      cout << "Case #" << t << ": " << cnt << endl;
   }

return 0;
}
