#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <set>
#include <utility>

using namespace std;

int main(void)
{
   int T;
   cin >> T;
   for(int i = 1; i <= T; ++i)
   {
      cout << "Case #" << i << ": ";
      int A, B;
      cin >> A >> B;
      int ans = 0;
      for(int x = A; x <= B; ++x)
      {
         ostringstream strm;
         strm << x;
         string numstr(strm.str());
         int len = numstr.length();
         for(int j = 1; j < len; ++j)
         {
            string outstr;
            rotate_copy(numstr.begin(), numstr.begin() + j, numstr.end(), 
                  back_inserter(outstr));
            istringstream str2int(outstr);
            int nRotated;
            str2int >> nRotated;
            if(nRotated > x && nRotated >= A && nRotated <= B)
            {
               ++ans;
               cerr << x << " " << nRotated << endl;
            }
         }
      }
      cout << ans << endl;
   }
   return 0;
}
