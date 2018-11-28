#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

bool win(int a, int b)
{
// std::cout << "w?" << a << " " << b << std::endl;
  
				   // if (a<=0)
//    return true;
  
  if (a<b)
    {
      int c=a;
      a=b;
      b=c;
    }


  if (a==b)
    return false;

  if (a%b==0)
    return true;

  int maxk=a/b;

  bool w=win(a-maxk*b,b);

  if (maxk==1)
        return !w;
  else
//    if (!w)
      return true;


  
  
  
    for (int k=1;k<=maxk;++k)
    if (!win(a-k*b,b))
      return true;

  
  return false;
  
}


int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int c=0;c<cases;++c)
    {
      int A1,A2,B1,B2;
      in >> A1 >> A2 >> B1 >> B2;

      int wins=0;
      for (int a=A1;a<=A2;++a)
	for (int b=B1;b<=B2;++b)
	  {
	    if (win(a,b))
	      ++wins;
	  }

      

      std::cout << "Case #" << c+1 << ": ";

      std::cout << wins;
      
      std::cout << std::endl;

    }
  return 0;
}
