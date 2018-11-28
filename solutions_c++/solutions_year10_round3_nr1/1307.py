#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;


int A[1000];
int B[1000];

int main(int argc, char *argv[])
{
   int T, N, ret;
   cin >> T;
   for(int c =0; c<T;c++)
   {
      cin >> N;
      for(int i=0; i<N; i++)
         cin >> A[i] >> B[i];

      for(int j = 0; j<N; j++)
         for(int k = j; k<N; k++)
            if((A[j]-A[k])*(B[j]-B[k])<0)
               ret ++;

      cout << "Case #"<< c+1 << ": " << ret << endl;
      ret = 0;
   }

   return 0;
}
