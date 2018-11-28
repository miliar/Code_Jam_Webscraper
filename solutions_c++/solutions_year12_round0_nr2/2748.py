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
#include <map>
#include <set>

#define INF 1000000007
#define EPS (1e-8)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
typedef long long LL;

using namespace std;


void setBits( int i , int score , vector< vector< vector<int> > > & table , int best , vector< vector<int> >& posstable )
{
  // first triplet.
  bool surprise;
  bool better;
  int index;
  
  if( (table[score][0][2] - table[score][0][0]) == 2 )
    {
      surprise = true;
    }
  else
    {
      surprise = false;
    }
  
  if( table[score][0][2] >= best )
    {
      better = true;
    }
  else
    {
      better = false;
    }

  index = surprise*2 + better;
  posstable[i][index] = 1;



  if( (table[score][1][2] - table[score][1][0]) == 2 )
    {
      surprise = true;
    }
  else
    {
      surprise = false;
    }
  
  if( table[score][1][2] >= best )
    {
      better = true;
    }
  else
    {
      better = false;
    }

  index = surprise*2 + better;
  posstable[i][index] = 1;
}
  
  

void checkAllAndSet( int num_googlers , int surprises, vector< vector<int> >& posstable , int curr_index , int curr_surprises, int curr_best_googlers , int& max_best_googlers )
{
  if( curr_index == num_googlers )
    {
      if( curr_surprises == surprises )
	{
	  max_best_googlers = max ( max_best_googlers, curr_best_googlers );
	}
      return;
    }
  else
    {
      for( int i = 0 ; i < 4 ; i++ )
	{
	  if( posstable[curr_index][i]  == 1 )
	    {
	      
	      if( i == 0 )
		{
		  checkAllAndSet( num_googlers, surprises, posstable , curr_index+1 , curr_surprises , curr_best_googlers , max_best_googlers);
		  
		}
	      else if( i == 1 )
		{
		  checkAllAndSet( num_googlers, surprises, posstable , curr_index+1 , curr_surprises , curr_best_googlers+1 , max_best_googlers);
		}
	      else if( i == 2 )
		{
		  checkAllAndSet( num_googlers, surprises, posstable , curr_index+1 , curr_surprises+1 , curr_best_googlers , max_best_googlers);
		}
	      else if( i == 3 )
		{
		  checkAllAndSet( num_googlers, surprises, posstable , curr_index+1 , curr_surprises+1 , curr_best_googlers+1 , max_best_googlers);

		}
	    }
	}
    }
}
	      

main()
{
  vector<int> v3(3);
  vector< vector<int> > tbl(2, v3);
  vector< vector < vector <int> > > table(31, tbl);

  int number;
  
  number = 0;
  table[number][0][0] = 0;
  table[number][0][1] = 0;
  table[number][0][2] = 0;
  table[number][1][0] = 0;
  table[number][1][1] = 0;
  table[number][1][2] = 0;

  number = 1;
  table[number][0][0] = 0;
  table[number][0][1] = 0;
  table[number][0][2] = 1;
  table[number][1][0] = 0;
  table[number][1][1] = 0;
  table[number][1][2] = 1;

  number = 2;
  table[number][0][0] = 0;
  table[number][0][1] = 0;
  table[number][0][2] = 2;
  table[number][1][0] = 0;
  table[number][1][1] = 1;
  table[number][1][2] = 1;

  number = 3;
  table[number][0][0] = 0;
  table[number][0][1] = 1;
  table[number][0][2] = 2;
  table[number][1][0] = 1;
  table[number][1][1] = 1;
  table[number][1][2] = 1;

  number = 4;
  table[number][0][0] = 0;
  table[number][0][1] = 2;
  table[number][0][2] = 2;
  table[number][1][0] = 1;
  table[number][1][1] = 1;
  table[number][1][2] = 2;

  number = 5;
  table[number][0][0] = 1;
  table[number][0][1] = 1;
  table[number][0][2] = 3;
  table[number][1][0] = 1;
  table[number][1][1] = 2;
  table[number][1][2] = 2;

  number = 6;
  table[number][0][0] = 1;
  table[number][0][1] = 2;
  table[number][0][2] = 3;
  table[number][1][0] = 2;
  table[number][1][1] = 2;
  table[number][1][2] = 2;

  number = 7;
  table[number][0][0] = 1;
  table[number][0][1] = 3;
  table[number][0][2] = 3;
  table[number][1][0] = 2;
  table[number][1][1] = 2;
  table[number][1][2] = 3;

  number = 8;
  table[number][0][0] = 2;
  table[number][0][1] = 2;
  table[number][0][2] = 4;
  table[number][1][0] = 2;
  table[number][1][1] = 3;
  table[number][1][2] = 3;

  number = 9;
  table[number][0][0] = 2;
  table[number][0][1] = 3;
  table[number][0][2] = 4;
  table[number][1][0] = 3;
  table[number][1][1] = 3;
  table[number][1][2] = 3;

  number = 10;
  table[number][0][0] = 2;
  table[number][0][1] = 4;
  table[number][0][2] = 4;
  table[number][1][0] = 3;
  table[number][1][1] = 3;
  table[number][1][2] = 4;

  number = 11;
  table[number][0][0] = 3;
  table[number][0][1] = 3;
  table[number][0][2] = 5;
  table[number][1][0] = 3;
  table[number][1][1] = 4;
  table[number][1][2] = 4;

  number = 12;
  table[number][0][0] = 3;
  table[number][0][1] = 4;
  table[number][0][2] = 5;
  table[number][1][0] = 4;
  table[number][1][1] = 4;
  table[number][1][2] = 4;

  number = 13;
  table[number][0][0] = 3;
  table[number][0][1] = 5;
  table[number][0][2] = 5;
  table[number][1][0] = 4;
  table[number][1][1] = 4;
  table[number][1][2] = 5;

  number = 14;
  table[number][0][0] = 4;
  table[number][0][1] = 4;
  table[number][0][2] = 6;
  table[number][1][0] = 4;
  table[number][1][1] = 5;
  table[number][1][2] = 5;

  number = 15;
  table[number][0][0] = 4;
  table[number][0][1] = 5;
  table[number][0][2] = 6;
  table[number][1][0] = 5;
  table[number][1][1] = 5;
  table[number][1][2] = 5;

  number = 16;
  table[number][0][0] = 4;
  table[number][0][1] = 6;
  table[number][0][2] = 6;
  table[number][1][0] = 5;
  table[number][1][1] = 5;
  table[number][1][2] = 6;

  number = 17;
  table[number][0][0] = 5;
  table[number][0][1] = 5;
  table[number][0][2] = 7;
  table[number][1][0] = 5;
  table[number][1][1] = 6;
  table[number][1][2] = 6;

  number = 18;
  table[number][0][0] = 5;
  table[number][0][1] = 6;
  table[number][0][2] = 7;
  table[number][1][0] = 6;
  table[number][1][1] = 6;
  table[number][1][2] = 6;

  number = 19;
  table[number][0][0] = 5;
  table[number][0][1] = 7;
  table[number][0][2] = 7;
  table[number][1][0] = 6;
  table[number][1][1] = 6;
  table[number][1][2] = 7;

  number = 20;
  table[number][0][0] = 6;
  table[number][0][1] = 6;
  table[number][0][2] = 8;
  table[number][1][0] = 6;
  table[number][1][1] = 7;
  table[number][1][2] = 7;

  number = 21;
  table[number][0][0] = 6;
  table[number][0][1] = 7;
  table[number][0][2] = 8;
  table[number][1][0] = 7;
  table[number][1][1] = 7;
  table[number][1][2] = 7;

  number = 22;
  table[number][0][0] = 6;
  table[number][0][1] = 8;
  table[number][0][2] = 8;
  table[number][1][0] = 7;
  table[number][1][1] = 7;
  table[number][1][2] = 8;

  number = 23;
  table[number][0][0] = 7;
  table[number][0][1] = 7;
  table[number][0][2] = 9;
  table[number][1][0] = 7;
  table[number][1][1] = 8;
  table[number][1][2] = 8;

  number = 24;
  table[number][0][0] = 7;
  table[number][0][1] = 8;
  table[number][0][2] = 9;
  table[number][1][0] = 8;
  table[number][1][1] = 8;
  table[number][1][2] = 8;

  number = 25;
  table[number][0][0] = 7;
  table[number][0][1] = 9;
  table[number][0][2] = 9;
  table[number][1][0] = 8;
  table[number][1][1] = 8;
  table[number][1][2] = 9;

  number = 26;
  table[number][0][0] = 8;
  table[number][0][1] = 8;
  table[number][0][2] = 9;
  table[number][1][0] = 8;
  table[number][1][1] = 8;
  table[number][1][2] = 10;

  number = 27;
  table[number][0][0] = 8;
  table[number][0][1] = 9;
  table[number][0][2] = 10;
  table[number][1][0] = 9;
  table[number][1][1] = 9;
  table[number][1][2] = 9;

  number = 28;
  table[number][0][0] = 8;
  table[number][0][1] = 10;
  table[number][0][2] = 10;
  table[number][1][0] = 9;
  table[number][1][1] = 9;
  table[number][1][2] = 10;

  number = 29;
  table[number][0][0] = 9;
  table[number][0][1] = 10;
  table[number][0][2] = 10;
  table[number][1][0] = 9;
  table[number][1][1] = 10;
  table[number][1][2] = 10;

  number = 30;
  table[number][0][0] = 10;
  table[number][0][1] = 10;
  table[number][0][2] = 10;
  table[number][1][0] = 10;
  table[number][1][1] = 10;
  table[number][1][2] = 10;
  

  int tests;
  scanf("%d",&tests);
  
  int num_googlers , surprises , best , tmp;
  for( int tc = 1 ; tc <= tests ; tc++ )
    {
      scanf("%d%d%d", &num_googlers , &surprises , &best );
      
      vector<int> scores(num_googlers);
      vector< vector<int> > posstable(num_googlers , vector<int>(4));
      
      for( int i = 0 ; i < num_googlers ; i++ )
	{
	  scanf("%d",&scores[i] );
	  setBits( i, scores[i] , table , best , posstable);
	}
      
      int max_best_googlers = 0;
      checkAllAndSet( num_googlers , surprises, posstable , 0 ,0 ,0, max_best_googlers );

      
      printf("Case #%d: %d\n", tc ,max_best_googlers );
    }      
  
}


