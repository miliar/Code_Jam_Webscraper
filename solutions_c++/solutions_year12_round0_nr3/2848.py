#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

int main(int, const char* []) {
   int T;
   cin>>T;
   for (int t = 0; t < T; ++t) {
      int A,B;
      cin>>A>>B;
      int factor = 1;
      int numdig = 0;
      int C = A;
      while (C != 0) {
         C /= 10;
         factor *= 10;
         ++numdig;
      }
      if (factor >= 10) {
         factor /= 10;
      }
      int res = 0;
      for (int k = A; k <= B; ++k) {
         int l = k;
         for (int a = 0; a < numdig; ++a) {
            l = l/10 + (l%10)*factor;
            if (k < l && l <= B) {
               ++res;
            }
         }
      }
      cout<<"Case #"<<t+1<<": "<<res<<endl;
   }
}