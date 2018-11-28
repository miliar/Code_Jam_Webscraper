#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std ;

int gcd( int a, int b)
{
  if(a*b == 0 )
    return a+b;
  if(a<b) 
    return gcd(b,a);
  return gcd(b,a%b);
}

bool algo()
{
  int pg,pd ;
  long long n;
  scanf("%lld %d %d",&n,&pd,&pg);
  if( pg == 0 ||pg == 100 )
    return pg==pd;
  return n >= 100/(gcd(100,pd));
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int i = 1 ; i <= t ; i++ )
    {
      printf("Case #%d: ",i);
      printf("%s",algo()?"Possible":"Broken");
      printf("\n");
    }
  return 0;
}
