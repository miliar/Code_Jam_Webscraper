#include <iostream>
#include <stdio.h>
#include <string>
#include <iomanip>

using namespace std;

string line ;

int list[10] ;

int findnext(int current)
{

    do
    {
    if(list[current] >0 )
    {
	list[current]-- ;
	return current ;
    }
    current++;
    }while(true) ;
      
}

int main()
{
  int n ;

  scanf("%d", &n) ;
  getline(cin, line) ;

  for(int i=1;i<=n;i++)
  {
      getline(cin, line) ;
      int num[line.size()+1] ;
      num[0] = 0 ;
      int numbers[10] = {} ;
      for(int j=1;j<=line.size();j++)
      {
	  num[j] = (int)line[j-1] - 48 ;
	  numbers[num[j]]++ ;
      }
      
      for(int j=line.size();j>0;j--)
	  if(num[j-1] < num[j])
	  {
	      for(int k=0;k<10;k++)
		    list[k] = 0 ;
	      for(int k=j-1;k<=line.size();k++)
		list[num[k]]++ ;
	      int change = num[j-1] ;

	      num[j-1] = findnext(change+1) ;
	      for(int k=j;k<=line.size();k++)
		  num[k] = findnext(0) ;
	      
	      break ;
	  }

      cout << "Case #" << i << ": " ;
      if(num[0] != 0)
	  cout << num[0] ;
      for(int k=1;k<=line.size();k++)
	  cout << num[k]  ;
      cout << endl ;

  }

  return 0;
}