#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <list>
#include <queue>
#include <algorithm>
#define max(a,b) a>b?a:b
#define min(a,b) a>b?b:a

using namespace std;

struct guy{

  int free ; 
  int engaged;

};

int stable(int *menpref , int* womenpref, int n )
{  for(int i=0;i<n;i++)
	{
	  for(int j =0;j<n;j++)
	    {
	      printf("%d",(*(womenpref+i)+j));
	    }
	}
     
  int proposed[n][n];
  struct guy  men[n];
  struct guy women[n];
  for(int i =0;i<n;i++)
    {
      men[i].free =  0 ; 
      women[i].free = 0 ;
      men[i].engaged = 0 ; 
      women[i].engaged  = 0 ; 
    }
  for(int i =0;i<n;i++)
    {
      if(men[i].engaged == 0)
	{
	  for(int j =0;j<n;j++)
	    {
	      if(proposed[i][j] == 0 )
		{
		  if(women[j].engaged ==0)
		    {
		      // she is free 
		      women[i].engaged = i ; 
		      men[i].engaged = j; 
		    }
		  else 
		    {
		      // she is already engaged 
		      //		      int curr  = 
		      
		    }
		  proposed[i][j] = 1; 
		}
	    }
	}
    }
  
}


int main()
{
  int t; 
  cin>>t;
  while(t--)
    {
      int n;
      cin>>n;
      int men[n][n];
      int women[n][n];
      for(int i=0;i<n;i++)
	{
	  for(int j =0;j<n;j++)
	    {
	      scanf("%d",&men[i][j]);
	    }
	}
       for(int i=0;i<n;i++)
	{
	  for(int j =0;j<n;j++)
	    {
	      scanf("%d",&women[i][j]);
	    }
	}
      stable(&men[0][0],&women[0][0],n);
    }


  return 0;
}
