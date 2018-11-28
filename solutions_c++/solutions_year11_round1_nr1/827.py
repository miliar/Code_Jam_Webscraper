#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#define beginT int _T; cin>>_T; for(int _t=1;_t<=_T;_t++)
#define printT(_ans) cout<<"Case #"<<_t<<": "<<_ans<<endl
using namespace std;

long long gcd(int a, int b)
{
         if(b==0) return a;
         return gcd(b, a%b);
}

int main()
{
   beginT
   {
         int Pd,Pg;
         long long N;
         cin>>N>>Pd>>Pg;
         int D = 100/gcd(100,Pd);
         if(Pg == 0)
         {
               if(Pd == 0) printT("Possible");
               else printT("Broken");
         }
         else if(Pg == 100)
         {
              if(Pd == 100) printT("Possible");
              else printT("Broken");
         }
         else if(D>N) printT("Broken");
         else printT("Possible");
   }
   return 0;
}
