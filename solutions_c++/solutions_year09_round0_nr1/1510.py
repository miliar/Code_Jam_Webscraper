#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

char allwords[10000][20];
int L,D,N;
int main()
{
  
  scanf("%d %d %d",&L,&D,&N);
  
  

  for(int i=0;i<D;i++)
    {
      scanf("%s",&allwords[i]);
   
      
      
    }

  for(int i=0;i<N;i++)
    {
      char word[1000];
      scanf("%s",&word);
      int totcount=0;
      for(int j=0;j<D;j++)
	{
	  int pos=0;
	  int count=0;
	  int posword=0;
	  while(count<L)
	    {
	      bool there=0;
	      if(word[pos]=='(')
		{
		  while(word[pos]!=')')
		    {
		      pos++;
		      if(word[pos]==allwords[j][count])
			{
			  there=1;
			}
			 
		    }
		}
	      else
		{
		  if(word[pos]==allwords[j][count])
		    there=1;
		  
		}
	      if(!there)
		break;
	      pos++;
	      count++;
	      
	    }  
	  if(count==L)
	    {
	      totcount++;
	    }
	}
      printf("Case #%d: %d\n",i+1,totcount);
    }
    



}
