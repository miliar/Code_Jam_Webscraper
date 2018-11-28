/*
Snapper Chain
*/

#include <iostream>
#include <fstream>

   using namespace std;

    int main()
   {
   // the first N bits of the binary representation of K must all be 1
      ifstream in ("snap.in");
      ofstream out ("snap.out");
   
      int T, N, K;
      in >> T;
      for(int i = 0; i < T; i++)
      {
         in >> N >> K;
         if((K % (1 << N)) == ((1 << N) - 1))
            out << "Case #" << (i + 1) << ": ON" << endl;
         else
            out << "Case #" << (i + 1) << ": OFF" << endl;
      }
   
      return 0;
   }
