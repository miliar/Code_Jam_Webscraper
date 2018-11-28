#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

int toInt(char * array)
{
    int result= 0;
    int length = 0;
    int mul = 1;
  while(array[length++] != '\0');
  length--;
  
  for(int k = length-1 ; k >= 0 ; k--)
  {
    result += mul*(array[k]-48);
    mul*= 10;
    
  }

  return result;
}

char * toStr(int num)
{
  char * list = new char[40];
  int number = 0 ;
  int index = 0;
  while (num != 0)
  {
    (number = num%10);
    list[index++]=number+48;
    num /= 10;
   }
   
  char * result = new char[40];
  
  for(int k = 0 ; k < index ; k++)
  result[index-k-1] = list[k];
   
   delete [] list;
   
  result[index] = '\0'; 
  return result;
}



bool isRe(int num, int num2)
{
  int result = 0;
  char * number1 = toStr(num);
  int length = 0;
  while(number1[length++] != '\0');
  length--;
  
  
  int index = 0 ;
  while(number1[index] != '\0')
  {
    char last = number1[length-1];
    
    for(int k = length-1 ; k > 0 ;k--)
    {
     number1[k] = number1[k-1];   
    }
    number1[length] = '\0' ;
    number1[0] = last ;
    
    int numnum =toInt(number1);
    if(numnum ==  num2)
    {
     // cout <<num<< "from" << numnum << "matched" <<num2 << endl;
      return true;
    }
    index++;
  }
  delete [] number1;
  return false;
}

int smart(int num , int min , int max)
{
   int result = 0;
  char * number1 = toStr(num);
  int * numberList = new int[max-min];
  int NumOfNumbers = 0 ;
  int length = 0;
  while(number1[length++] != '\0');
  length--;
  
  
  int index = 0 ;
  while(number1[index] != '\0')
  {
    char last = number1[length-1];
    
    for(int k = length-1 ; k > 0 ;k--)
    {
     number1[k] = number1[k-1];   
    }
    number1[length] = '\0' ;
    number1[0] = last ;
    
    int numnum =toInt(number1);
    
    bool isIn = false;
    
    for(int k = 0 ; k < NumOfNumbers ; k++)
      if( numberList[k] == numnum)
      {
	isIn= true;
	break;
      }
    
    
    if(!isIn)
    if(numnum >=  num+1 && numnum <= max)
    {
      numberList[NumOfNumbers++] = numnum;
      result++;
     // cout <<num<< "from" << numnum << "matched" <<num2 << endl;
    }
    index++;
  }
  delete [] numberList;
  delete [] number1;
  return result; 
  
}

int counter(int min , int max)
{
 int result = 0 ;
 /*
 for(int k = min ; k <= max ; k++)
   for(int l = k+1 ; l <=max; l++)
     if(isRe(k,l))
       result++;*/
     
     
    int result2 = 0; 
  for(int k = min ; k <= max ; k++)
    result2 += smart(k,min,max);
    
   //  cout << "equal = " << (result == result2) << endl;
     
     
  return result2;
  
}


int main()
{
  
  int cases;
  cin >> cases;
  for(int k = 0 ; k < cases ; k++)
  {
    int max =0;
    int min = 0;
    cin >> min >> max ;
   cout << "Case #" << k+1 << ": " << counter(min,max) << endl; 
    
  }
 return 0; 
}