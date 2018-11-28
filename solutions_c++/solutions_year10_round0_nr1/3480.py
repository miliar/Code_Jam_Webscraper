#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
   unsigned int T, N, K;

   cin >> T;
   for(unsigned int i=0; i<T;i++)
   {
      cin >> N;
      cin >> K;
      if((K+1)%(1<<N))
         cout << "Case #" << i+1 << ": OFF" << endl;
      else
         cout << "Case #" << i+1 << ": ON" << endl;
   }
}
