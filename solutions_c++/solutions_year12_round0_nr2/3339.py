#include <iostream>
using namespace std;

int main(int argc, const char *argv[])
{
   int T, N, S, p;
   int ans;
   cin >> T;
   cin.get();

   for (int c = 0; c < T; c++) 
   {
      ans = 0;
      cin >> N >> S >> p;
      const int highstd = p * 3 - 2, lowstd = p * 3 - 4;

      for (int i = 0; i < N; i++) 
      {
         int score;
         cin >> score;
         if ( score >= highstd )
            ans++;
         else if ( score >= lowstd )
         {
            if ( S > 0 && lowstd > 0 )
            {
               S--;
               ans++;
            }
         }
      }

      // Output
      cout << "Case #" << c+1 << ": " << ans << endl;
      cin.get();
   }

   return 0;
}
