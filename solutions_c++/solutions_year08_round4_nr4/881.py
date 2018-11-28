#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <utility>
using namespace std;

int compress(int k, const vector<int>& perm, const string& str)
{
   char lastch = 'a' - 1;
   int ans = 0;
   for(int i = 0; i < str.length(); i += k)
   {
      for(int j = 0; j < k; ++j)
      {
         if(str[i + perm[j]] != lastch)
            ++ans;
         lastch = str[i + perm[j]];
      }
   }
   return ans;
}

int main(void)
{
   int n;
   cin >> n;
   for(int i = 1; i <= n; ++i)
   {
      cout << "Case #" << i << ":";

      int k;
      cin >> k;
      cin.ignore();
      vector<int> perm(k, 0);
      for(int j = 0; j < k; ++j)
         perm[j] = j;

      const vector<int> initperm(perm);
      vector<int> bestperm(initperm);

      string tbc;
      cin >> tbc;
      int bestans = tbc.length();

      do
      {
         int ans = compress(k, perm, tbc);
         if(ans < bestans)
         {
            bestans = ans;
            /*
            for(int j = 0; j < k; ++j)
               cerr << perm[j] << " ";
            cerr << endl;
            */
         }

         next_permutation(perm.begin(), perm.end());
      }while(perm != initperm);

      cout << " " << bestans << endl;

   }
   return 0;
}
