#include <iostream>
#include <string>
using namespace std;

long long ans = 0;
bool isUgly(long long a)
{
   if(a%2 == 0 || a%3 ==0 || a%5 == 0 || a%7 ==0)return true;
   return false;
}
void calc(string str)
{
   long long sum = 0, t = 0;
   int flag = 1;
   for(int i = 0; i < str.size(); i++)
   {
      if(str[i] == '+')
      {
         sum += flag*t;
         flag = 1;
         t = 0;
      }
      else if(str[i] == '-')
      {
         sum += flag*t;
         flag = -1;
         t = 0;
      }
      else
         t = t* 10 + (str[i] - '0');
   }
   sum += flag*t;
   if(isUgly(sum)){  ans++;}
}
void solve(int k, string str)
{
   if( k >= str.size())
   {
      calc(str);
      return;
   }
   string newstr = str;
   if(k+1 < str.size())solve (k+2, newstr.insert(k+1,"+"));
   newstr = str;
   if(k+1 < str.size())solve (k+2, newstr.insert(k+1,"-"));
   solve (k+1, str);
}
int main()
{
   freopen("B-small-attempt3.in","r",stdin);
   freopen("B-small-attempt3.out","w",stdout);
   int t;
   cin >> t;
   for(int i = 1; i <= t; i++)
   {
      ans = 0;
      string str;
      cin >> str;
      solve (0, str);
      cout << "Case #" << i << ": " << ans << endl;
   }
   return 0;
}
