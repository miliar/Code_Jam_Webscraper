#include <iostream>
#include <math.h>
using namespace std;

//long int Array[30];
//ol boolArray[30];

long int Power(int p)
{
  long int pow = 1;
  for(int i=0;i<p;i++)
    {
      pow *=2;
    }
  return pow;
}

int main()
{
  /*Array[0] = 0;
    Array[1] = 2;
    Array[2] = 4;
    for(int i=1;i<30; i++)
    {
    Array[i] = 
    }*/
  int nTestCases;
  //cout << Power(2);
  cin >> nTestCases;
  for(int i=1;i<= nTestCases; i++)
    {
      int iCsnappers = 0;
      cin >> iCsnappers; 
      int iCFingersSnapped = 0;
      cin >> iCFingersSnapped;
      long int power = Power(iCsnappers);
      if(((iCFingersSnapped + 1 ) % power) == 0)
	{
	  cout << "Case #"<< i << ": " << "ON"<<"\n";
	}
      else
	{
	  cout << "Case #"<< i << ": " << "OFF"<<"\n";
	}
    }
}
