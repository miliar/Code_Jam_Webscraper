#include <iostream>
#include <string>

using namespace std;

int main()
{
   int useCasesNumber;
   int N;
   int S;
   int p;
   int cnt = 0;
   int number;
   int tmp;
   cin>>useCasesNumber;
   for (int i = 0; i < useCasesNumber; ++i, cnt = 0)
   {
      cout<<"Case #"<<i+1<<": ";
      cin>>N>>S>>p;
      for (int j = 0; j < N; ++j)
      {
         cin>>number;
         if (number >= p && (number / 3) >= p)
         {
            cnt++;
            continue;
         }
         tmp = number - p;
         if (number >= p && (p - (tmp/2)) <= 1)
         {
            cnt++;
            continue;
         }
         if (S > 0 && (number >= p) && (p - (tmp / 2)) <= 2)
         {
            cnt++;
            S--;
         }
      }
      cout<<cnt<<endl;
   }
   return 0;
}
