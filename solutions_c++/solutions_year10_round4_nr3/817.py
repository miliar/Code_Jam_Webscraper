#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
bool bact[250][250];


int main()
{
  int c = 1;
  scanf("%d", &c);
  for(int C = 1; C <= c; C++)
    {
      int ans = 0;
      int R;
      for(int i = 0 ; i < 250; i++)
	for(int j = 0 ; j < 250; j++)
	  bact[i][j] = false;
      scanf("%d", &R);
      int x1, x2, y1, y2;
      for(int r = 0 ; r < R; r++){
	scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
	for(int i = y1; i <= y2; i++)
	  for(int j = x1; j <= x2; j++)
	    bact[i][j] = true;
      }
      while(true)
	{
	  bool allDead = true;
	  bool nbact[250][250];
	  for(int i = 0 ; i < 250; i++)
	    for(int j = 0; j < 250; j++){
	      nbact[i][j] = false;
	      if( bact[i][j] )
		allDead = false;
	    }
	  
	  if( allDead )
	    break;
	  for(int i = 1; i < 250; i++)
	    for(int j = 1 ; j < 250; j++)
	      {
		if( !bact[i][j])
		  nbact[i][j] =  bact[i-1][j] && bact[i][j-1];
		else
		  nbact[i][j] = bact[i-1][j] || bact[i][j-1];
	      }
	  for(int i = 1; i < 250; i++)
	    for(int j = 1; j < 250; j++)
	      bact[i][j] = nbact[i][j];
	  ans++;

	}
      
      printf("Case #%d: %d\n", C, ans);
    }
}

