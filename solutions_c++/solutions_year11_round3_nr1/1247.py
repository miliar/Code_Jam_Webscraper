#include <iostream>
#include <string>
#include <fstream>
using namespace std;

char g[55][55];

int main()
{
    ifstream iff;
    ofstream of;
    iff.open("a.in");
    of.open("a.out");
    int p;
    iff>>p;

    for(int t=0; t<p; t++)	
    {
	int n,m;
	iff>>n>>m;
	for(int i=0; i<n; i++)
	  for(int j=0; j<m; j++)
	  {
	      iff>>g[i][j];
	  }
	  int ans = 0;
	  for(int i=0; i<n; i++)
	  for(int j=0; j<m; j++)
	  {
	      if(g[i][j] == '#')
	      {
		 g[i][j] = '/';
		 if(j +1 < m && g[i][j+1] == '#')g[i][j+1] = '\\';
		 else ans = 1;
		 if(i + 1 <n && j +1 < m && g[i +1][j+1] == '#')g[i +1][j+1] = '/';
		 else ans = 1;
		 
		 if(i +1 < n && g[i + 1][j] == '#')g[i +1 ][j] = '\\';
		 else ans = 1;
		 
	      }
	  }
	  
	  if(ans == 0)
	  { 
	     of<<"Case #"<<t+1<<":"<<endl;
	     for(int i=0; i<n; i++)
	     {
	       for(int j=0; j<m-1; j++)of<<g[i][j];
	       of<<g[i][m-1]<<endl;
		 
	     }
	  }
	  else
	  {
	      of<<"Case #"<<t+1<<":"<<endl;
	      of<<"Impossible"<<endl;
	  }
    }
    return 0;
}