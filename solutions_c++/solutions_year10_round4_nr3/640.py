#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pi;

#define INF 1000000000
#define MAXN 105

int a[MAXN][MAXN];

int main()
{
  int t,r,x1,y1,x2,y2,left;
  scanf("%d",&t);
  for(int cas = 1 ; cas <= t ; cas++)
  {
     
     memset(a,0,sizeof(a));
     left = 0;
     cin>>r;
     for(int k = 1 ; k <= r ; k++)
     {
       cin>>x1>>y1>>x2>>y2;
     
 
     for(int i = x1 ; i <= x2 ; i++)
       for(int j = y1 ; j <= y2 ; j++)
       {
	 if( a[i][j] == 0 )
	 {
	  a[i][j] = 1;
	  left++;
	 }
       }
       
     }

    printf("Case #%d: ",cas);  
    int tim = 0;
    if( left == 0 )
    {
      cout<<tim<<endl;
      continue;
    }
    /*
    for(int i = 10 ; i >= 1 ; i--)
    {
      for(int j = 1 ; j <= 10 ; j++)
	cout<<a[i][j]<<" ";
      
      cout<<endl;
    }
    */
    while(1)
    {

      tim++; 
      for(int i = 1 ; i <= 100 ; i++)
	for(int j = 1 ; j <= 100 ; j++)
	{
	  if( a[i][j] == 0 )
	  {

	    if( (a[i][j-1] == 1 || a[i][j-1] == 3) && (a[i-1][j] == 1 || a[i-1][j] == 3 ) )
	    {
	      a[i][j] = 2;
	      left++;
	    }
	  }
	  else 
	  {
	    if( a[i][j-1] != 1 && a[i-1][j] != 1 && a[i][j-1]!= 3 && a[i-1][j] != 3 )
	    {
	      a[i][j] = 3;
	      left--;
	    }
	  }
	}
	
     for(int i = 1 ; i <= 100 ; i++)
	for(int j = 1 ; j <= 100 ; j++)
	{
	  if( a[i][j] == 2 )
	  {
	    a[i][j] = 1;
	  }
	  if( a[i][j] == 3 )
	    a[i][j] = 0;
	}
    
 /*   cout<<endl;
    for(int i = 10 ; i >= 1 ; i--)
    {
      for(int j = 1 ; j <= 10 ; j++)
	cout<<a[i][j]<<" ";
      cout<<endl;
      
    }
    */
      if( left == 0 )
      {
	cout<<tim<<endl;
	break;
      }
    }
       
  }
  return 0;  
}