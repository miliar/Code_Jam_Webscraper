#include <iostream>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <vector>

using namespace std;

int A,B;
vector<int> re;

bool inside(int n)
{
   for(int i = 0; i < re.size(); i++)
   {
      if(re[i] == n) return 1;
   }
   return 0;

}

int make_pair(int a)
{

   int b,c,d,f, cnt=0;
   re.clear();
   re.push_back(a);

   for(int i = 1; i <= log10(a); i++)
   {

      b = a % (int)pow(10,i);
      c = a / pow(10,i);
      d = log10(a);
      f = b*pow(10,d-i+1)+c;
      if(inside(f)) {
         //cout << "COPY!!!!\n\n";
         continue;
      }
      re.push_back(f);
      //cout << b << " : " << c << " : " << d << "\n";

      if(A <= a && a < f && f <= B)
      {
         //cout << "(" << a << ", " << f << ")" << endl;

         cnt++;
      }
      else
      {
         //cout << f << "\ttoo big" << endl;
      }
   }

   return cnt;
}

int main() 
{
   int n, sum = 0;

   cin >> n;
  
   for(int t = 1; t <= n; t++)
   {
      cin >> A >> B;

      for(int i = 0; i <= B; i++)
      {

         sum += make_pair(i);

      }

      cout << "Case #" << t << ": " << sum << endl;
      sum = 0;
   }
return 0;
}
