// Tic-Tac-Toe-Tomek
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cfloat>
#include <climits>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <utility>
#include <sys/time.h>

#define INF 1000000007
#define EPS (1e-8)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define mp make_pair
#define FOR(i,k) for(i=0;i<k;i++)
#define RFOR(i,k) for(i=k-1;i>=0;i--)
const long double PI = 3.1415926535897932384626433832795;
typedef long long LL;


using namespace std;

bool Xwon( vector<string>& board )
{
  int row,col;

  // checking for rows.
  for( row = 0 ; row < 4 ; row++ )
    {
      for( col = 0 ; col < 4 ; col++ )
	{
	  if( board[row][col] == 'X' || board[row][col] == 'T' )
	    {
	      if( col == 3 )
		{
		  return true;
		}
	      else
		{
		  continue;
		}
	    }
	  else
	    {
	      break;
	    }
	}
    }


  // checking for columns.
  for( col = 0 ; col < 4 ; col++ )
    {
      for( row = 0 ; row < 4 ; row++ )
	{
	  if( board[row][col] == 'X' || board[row][col] == 'T' )
	    {
	      if( row == 3 )
		{
		  return true;
		}
	      else
		{
		  continue;
		}
	    }
	  else
	    {
	      break;
	    }
	}
    }

  // checking for diagonals.
  for( int d = 0 ; d < 4 ; d++ )
    {
      if( board[d][d] == 'X' || board[d][d] == 'T' )
	{
	  if( d == 3 )
	    {
	      return true;
	    }
	  else
	    {
	      continue;
	    }
	}
      else
	{
	  break;
	}
    }


  for( int d = 0 ; d < 4 ; d++ )
    {
      if( board[d][3-d] == 'X' || board[d][3-d] == 'T' )
	{
	  if( d == 3 )
	    {
	      return true;
	    }
	  else
	    {
	      continue;
	    }
	}
      else
	{
	  break;
	}
    }

  return false;
}


bool Owon( vector<string>& board )
{
  int row,col;

  // checking for rows.
  for( row = 0 ; row < 4 ; row++ )
    {
      for( col = 0 ; col < 4 ; col++ )
	{
	  if( board[row][col] == 'O' || board[row][col] == 'T' )
	    {
	      if( col == 3 )
		{
		  return true;
		}
	      else
		{
		  continue;
		}
	    }
	  else
	    {
	      break;
	    }
	}
    }


  // checking for columns.
  for( col = 0 ; col < 4 ; col++ )
    {
      for( row = 0 ; row < 4 ; row++ )
	{
	  if( board[row][col] == 'O' || board[row][col] == 'T' )
	    {
	      if( row == 3 )
		{
		  return true;
		}
	      else
		{
		  continue;
		}
	    }
	  else
	    {
	      break;
	    }
	}
    }

  // checking for diagonals.
  for( int d = 0 ; d < 4 ; d++ )
    {
      if( board[d][d] == 'O' || board[d][d] == 'T' )
	{
	  if( d == 3 )
	    {
	      return true;
	    }
	  else
	    {
	      continue;
	    }
	}
      else
	{
	  break;
	}
    }


  for( int d = 0 ; d < 4 ; d++ )
    {
      if( board[d][3-d] == 'O' || board[d][3-d] == 'T' )
	{
	  if( d == 3 )
	    {
	      return true;
	    }
	  else
	    {
	      continue;
	    }
	}
      else
	{
	  break;
	}
    }

  return false;
}
  
bool gameIncomplete( vector<string>& board )
{
  int row,col;
  for( row = 0 ; row < 4 ; row++ )
    {
      for( col = 0 ; col < 4 ; col++ )
	{
	  if( board[row][col] == '.' )
	    {
	      return true;
	    }
	}
    }

  return false;
}
  
      

main()
{
  int tests;
  cin >> tests;
  
  for( int tc = 1 ; tc <= tests ; tc++ )
    {
      vector<string> board(4);
      
      for( int i = 0 ; i < 4 ; i++ )
	{
	  cin >> board[i];
	}
      
      if( Xwon( board ) ) 
	{
	  cout << "Case #" << tc << ": X won" << endl;
	}
      else if( Owon( board ) )
	{
	  cout << "Case #" << tc << ": O won" << endl;
	}
      else if( gameIncomplete( board ) )
	{
	  cout << "Case #" << tc << ": Game has not completed" << endl;
	}
      else
	{
	  cout << "Case #" << tc << ": Draw" << endl;
	}
    }
}



