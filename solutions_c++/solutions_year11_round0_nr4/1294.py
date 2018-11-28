#include <iostream>
#include <cstring>
using namespace std;
int countsum(int T[], int l) {
   int A[20000];
   memcpy(A,T,l*sizeof(int));
   int q = 0 ;
   for (int i = 0; i < l; i++)
     if (A[i]>=0) {
       int len = 0 , st = i;
       while (A[st]>=0) {
         len++; A[st] = -1; st = T[st];
       }
       if (len>1)
       q += len;
     }
     return q;
}
int T[10000];
int main() {
   int TT;
   cin >> TT;
   for (int t = 1; t<= TT; t++)
   {
     cout <<"Case #"<<t<<": ";
     int l;
     cin >> l;
     for (int i = 0 ; i < l ; i++)
       { cin >> T[i];  T[i]--; }
     
     cout << countsum(T,l) <<".000000"<<endl;
     
   }
}
