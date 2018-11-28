#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
int ways[30][1000];
string message;
string curr;
int findit(int mpos,int cpos)
{
  if(mpos==message.size())
    return 1;
  if(cpos==curr.size())
    return 0;
  if(ways[mpos][cpos]!=-1)
    return ways[mpos][cpos];

  int retval=0;
  if(message[mpos]==curr[cpos])
    {
      retval=(retval+findit(mpos+1,cpos+1))%1000;
    }
  
  retval=(retval+findit(mpos,cpos+1))%1000;

  ways[mpos][cpos]=retval;
  return retval;



}


int main()
{
  int N;
  scanf("%d",&N);
  

  message="welcome to code jam";
   
  char c;
   scanf("%c",&c);

  for(int t=1;t<=N;t++)
    {
     
      curr="";
      
      do
	{
	  scanf("%c",&c);
	  curr.push_back(c);
	}while(c!='\n');
      curr.resize(curr.size()-1);
      //cout << curr << endl;

      for(int i=0;i<30;i++)
	for(int j=0;j<500;j++)
	  ways[i][j]=-1;

      int retval=findit(0,0);

      printf("Case #%d: %04d\n",t,retval);


      
    }

}
