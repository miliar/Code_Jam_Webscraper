#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

vector <long> recycledNumbers;

bool rn(long n, long m)
{
  //Finding number of digits
  int numberOFDigits = 0;
  int temp = n;
  while(temp != 0)
  {
    numberOFDigits++;
    temp /= 10;
  }
  long power = (long)pow(10, numberOFDigits-1);
  long a=10, b = power;
    for(int j = 1; j<numberOFDigits; j++)
    {
      long rotate = ((n%a)*b) + (n/a);
      if(rotate == m) return true;
       a *=10;
       b /=10;
    }
    return false;
  
}
long FindRecycle(long ll, long ul)
{
  long count = 0;
  if(ul < 9) return 0;
  
  
      for(long i = ll; i<ul;i++)
      {
	for(long j = i+1; j<=ul; j++)
	{
	  if(rn(i,j)) count +=1;
	}
      }
  return count;
}


int main()
{
  int T;
  scanf("%d", &T);
  int cas = 1;
  while(T--)
  {
    long lLimit, uLimit;
    scanf("%ld %ld", &lLimit, &uLimit);
    long answer = FindRecycle(lLimit, uLimit);
    printf("Case #%d: %ld\n", cas, answer);
    cas++;
  }
  return 0;
}
