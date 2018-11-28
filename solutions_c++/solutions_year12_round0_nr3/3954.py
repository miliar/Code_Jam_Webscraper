#include <iostream>
using namespace std;

int countRecycle(int a, int b);
int count(int num, int up, int nd);
int numDigits(int num);
int moveFront(int num, int digits);

const int powers[]= {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

#define pow10(X) powers[(X)]

int main()
{
  int T;

  cin >> T;

  for(int test = 0; test < T; ++test)
    {
      int a, b;
      cin >> a >> b;
      cout << "Case #" << (test+1) << ": " << countRecycle(a, b) << endl;
    }

  return 0;
}

int countRecycle(int a, int b)
{
  int total = 0;
  int nd = numDigits(a);

  for(int i = a; i <= b; ++i)
    total += count(i, b, nd);

  return total;
}

int count(int num, int up, int nd)
{
  int counter = 0;
  int bo = moveFront(num, nd);
 
 while( bo != num )
    {
      if ( (bo > num) && (bo <= up)) counter++;
      bo = moveFront(bo, nd);
    }

  return counter;
}

int numDigits(int num)
{
  int digits = 0;
  if(num == 0) return 1;

  while( num != 0 )
  {
   num = num / 10; 
   digits++;
  }

  return digits;
}

int moveFront(int num, int digits)
{
  int last = num % 10;
  int rv = (last * pow10(digits-1)) + (num / 10); 
  return rv;
}
