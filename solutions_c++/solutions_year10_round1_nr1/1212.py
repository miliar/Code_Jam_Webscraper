#include<stdio.h>
#include<string>
#include<vector>
#include<iostream>
#include<utility>
#include<algorithm>
#include<set>
#include<stack>
#include<sstream>
#include<math.h>

using namespace std;

#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define VL vector<long long>
#define ll long long

int main(int argc, char** argv)
{
  ll cases;
  cin >> cases;
  for(ll caseNo = 0; caseNo < cases; ++caseNo)
    {
      ll N, K;
      cin >> N >> K;
      char board1[N][N], board2[N][N];
      for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    cin >> board1[i][j];
	}

      /*for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      cout << board1[i][j];
	    }
	  cout << endl;
	  }      

	  cout << "Rotate\n";*/

      ll row = 0, column = 0;
      for(ll i = N-1; i >= 0; i--)
	{
	  row = 0;
	  for(ll j = 0; j < N; j++)
	    {
	      board2[row][column] = board1[i][j];
	      //cout << board2[row][column];
	      row++;
	    }
	  column++;
	}
      
      for(ll i = N-1; i >= 0; i--)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      int inc = 1;
	      while((i+inc) < N && board2[i+inc][j] == '.')
		inc++;
	      
	      if(inc > 1)
		{
		  board2[i+inc - 1][j] = board2[i][j];
		  board2[i][j] = '.';
		}
	    }
	}

      /*
      for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      cout << board2[i][j];
	    }
	  cout << endl;
	  }      */

      ll count = 0;
      char prev = '.';
      bool red = false, blue = false;

      cout << "Case #" << caseNo + 1 << ": ";

      for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      if(board2[i][j] != '.' && board2[i][j] == prev)
		{
		  count++;
		  if(count == K-1)
		    {
		      if(prev == 'R')
			{
			  red = true;
			}
		      else
			{
			  blue = true;
			}
		    }
		}
	      else
		{
		  prev = board2[i][j];
		  count = 0;
		}
	    }
	  prev = '.';
	  count = 0;
	}

      if(red && blue)
	{
	  cout << "Both\n";
	  continue;
	}

      for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      if(board2[j][i] != '.' && board2[j][i] == prev)
		{
		  count++;
		  if(count == K-1)
		    {
		      if(prev == 'R')
			{
			  red = true;
			}
		      else if(prev == 'B')
			{
			  blue = true;
			}
		    }
		}
	      else
		{
		  count = 0;
		  prev = board2[j][i];
		}
	    }
	  prev = '.';
	  count = 0;
	}

      if(red && blue)
	{
	  cout << "Both\n";
	  continue;
	}

      for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      ll count = 0;
	      prev = board2[i][j];
	      ll rowInc = 01, colInc = 1;
	      while(count < K && (i+rowInc) < N && (j + colInc) < N)
		{
		  if(prev == board2[i+rowInc++][j + colInc++])
		    count++;
		  else
		    break;
		}
		if(count == K-1)
		  {
		    if(prev == 'R')
		      red = true;
		    else if(prev == 'B')
		      blue = true;
		  }
	    }
	}

        if(red && blue)
	{
	  cout << "Both\n";
	  continue;
	}

      for(ll i = 0; i < N; i++)
	{
	  for(ll j = 0; j < N; j++)
	    {
	      ll count = 0;
	      prev = board2[i][j];
	      ll rowInc = 1, colInc = 1;
	      while(count < K && (i+rowInc) >= 0 && (j + colInc) >= 0)
		{
		  if(prev == board2[i-rowInc++][j - colInc++])
		    count++;
		  else
		    break;
		}
		if(count == K-1)
		  {
		    if(prev == 'R')
		      red = true;
		    else if(prev == 'B')
		      blue = true;
		  }
	    }
	}

        if(red && blue)
	{
	  cout << "Both\n";
	  continue;
	}
	if(red)
	  cout << "Red\n";
	if(blue)
	  cout << "Blue\n";

	if(!red && !blue)
	  cout << "Neither\n";
	//cout << endl;
    }
}
