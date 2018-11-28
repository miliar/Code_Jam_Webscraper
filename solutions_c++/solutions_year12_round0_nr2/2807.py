#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;

int main(int, const char* []) {
   int T;
   cin>>T;
   for (int t = 0; t < T; ++t) {
      int N, S, p;
      cin>>N>>S>>p;
      int res = 0;
      for (int n = 0; n < N; ++n) {
         int k;
         cin>>k;
         if (k>=3*p-2 && k >= p) {
            ++res;
         }
         else if (k>=3*p-4 && S && k >= p) {
            ++res;
            --S;
         }
      }  
      cout<<"Case #"<<t+1<<": "<<res<<endl;
   }
}