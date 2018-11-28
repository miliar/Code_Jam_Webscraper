#include <iostream>
#include <stdio.h>
#include <string>


using namespace std;

string line ;


int main()
{
  int n ;

  scanf("%d\n", &n) ;
  

  for(int i=1;i<=n;i++)
  {
      getline(cin, line) ;
      int numbers[(int)'z' + 1] ;
      int s[line.size()] ;
      for(int j=0;j<line.size();j++)
	  s[j] = j ;
      s[0] = 1 ;
      s[1] = 0 ;
      for(int j=0;j<(int)'z' + 1;j++)
	numbers[j] = -1 ;
      int count = 0 ;
      for(int j=0;j<line.size();j++)
      {
	  if(numbers[(int)line[j]] == -1)
	  {
	    numbers[(int)line[j]] = s[count] ;
	    count++ ;
	  }
      }
      if(count ==1 ) count =2 ;
      int result = 0 ;
      int power = 1 ;
      for(int j=line.size()-1;j>=0;j--)
      {
	      result += power*numbers[(int)line[j]] ;
	      power *= count ;
      }
      cout << "Case #" << i << ": " << result << endl ;


      
  }

  return 0;
}