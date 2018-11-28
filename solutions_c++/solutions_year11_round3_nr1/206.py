#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      int R,C,i,j;
      cin>>R>>C;
      char grid[60][60];
      for(i=0;i<R;i++)
	for(j=0;j<C;j++)
	  cin>>grid[i][j];
      for(i=0;i<R;i++)
	{
	  for(j=0;j<C;j++)
	    {
	      if(grid[i][j]=='#')
		{
		  if((i+1==R)||(j+1==C))
		    break;
		  if((grid[i+1][j]!='#')||(grid[i][j+1]!='#')||(grid[i+1][j+1]!='#'))
		    break;
		  grid[i][j]=grid[i+1][j+1]='/';
		  grid[i+1][j]=grid[i][j+1]='\\';
		}
	    }
	  if(j<C)
	    break;
	}
      cout<<"Case #"<<t<<": "<<"\n";
      if(i<R)
	cout<<"Impossible\n";
      else
	for(i=0;i<R;i++)
	  {
	    for(j=0;j<C;j++)
	      cout<<grid[i][j];
	    cout<<"\n";
	  }
    }
  return 0;
}
