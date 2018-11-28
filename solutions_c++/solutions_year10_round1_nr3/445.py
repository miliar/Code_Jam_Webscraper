#include<iostream>

using namespace std;
long long gcd(long long a,long long b)
{
  if(b == 0)
    return a;
  else
    return gcd(b,a%b);
}
int win(long long x,long long y)
{
  long long val = gcd(x,y);
  if(x == y)
    return -1;
  else if(y%x == 0 || x%y == 0)
    return 1;
  else if(val == x-y || val == y-x)
    {
      return -1;
    }
  else if(x>y && x<2*y || y>x &&y<2*x)
    {
      if(y>x)
	return -win(x,y-x);
      else
	return -win(x-y,y);
    }
  else
    return 1;
}
int main()
{
  long long t,a1,a2,b1,b2,a,b,i,j,count;
  cin>>t;
  i = 1;
  while(i<=t)
    {
      count = 0;
      cin>>a1>>a2>>b1>>b2;
      for(a=a1;a<=a2;a++)
	for(b=b1;b<=b2;b++)
	  {
	    if(win(a,b)==1)
	      {
		//cout<<"\na="<<a<<"  b="<<b;
		count++;
	      }
	  }
      cout<<"\nCase #"<<i<<": "<<count;
      i++;
    }
  return 0;
}
	  
