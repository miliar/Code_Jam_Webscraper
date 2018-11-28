#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <functional>
#include <math.h>

using namespace std;

#define in cin
#define out cout
#define pf printf

#define g(name) 	in >> name
#define gi(name)	int name;		   g(name)
#define gl(name)	long name;		   g(name)
#define gll(name) long long name;   g(name)
#define gd(name)	double name; 	   g(name)
#define gc(name)	char name;		   g(name)
#define gb(name)	bool name;		   g(name)
#define gs(name)  string name;      g(name)

#define fri(var, a, b)		for( int var = a; var < b; var++ )
#define frd(var, a, b) 	   for( int var = a; var > b; var-- )
#define frv(var, vec)      for( unsigned int var = 0; var < vec.size(); var++ )
#define frvi(it, vec)      for( typeof(vec.begin()) it = vec.begin(); it != vec.end(); it++ )

#define pb push_back
#define mp make_pair

char matrix[55][55];
bool visited[55][55];
int rows, cols;
bool solved = false;

void solve(int row, int col)
{
   if(solved)
      return;

   if(col >= cols - 1)
   {
      solve(row + 1, 0);
      return;
   }

   if(row >= rows - 1)
   {
      bool valid = true;
      fri(i, 0, rows)
      {
         fri(j, 0, cols)
         {
            if(matrix[i][j] == '#')
            {
               valid = false;
               break;
            }
         }
      }

      if(valid)
      {
         fri(i, 0, rows)
         {
            fri(j, 0, cols)
               cout << matrix[i][j];
            cout << '\n';
         }
         solved = true;
      }
      return;
   }

   if(matrix[row][col] == '#' && matrix[row + 1][col] == '#' && matrix[row][col + 1] == '#'
         && matrix[row + 1][col + 1] == '#')
   {
      matrix[row][col] = matrix[row + 1][col + 1] = '/';
      matrix[row + 1][col] = matrix[row][col + 1] = '\\';

      solve(row, col + 1);

      matrix[row][col] = matrix[row + 1][col + 1] = '#';
      matrix[row + 1][col] = matrix[row][col + 1] = '#';
   }
   else
      solve(row, col + 1);
}

void runTrial(int trial)
{
   g(rows);
   g(cols);

   printf("Case #%d: \n", trial);
   solved = false;

   fri(i, 0, rows)
   {
      fri(j, 0, cols)
      {
         gc(ch);
         matrix[i][j] = ch;
      }
   }

   if(rows < 2 || cols < 2)
   {
      bool valid = true;
      fri(i, 0, rows)
      {
         fri(j, 0, cols)
         {
            if(matrix[i][j] == '#')
            {
               valid = false;
               break;
            }
         }
      }

      if(valid)
      {
         fri(i, 0, rows)
         {
            fri(j, 0, cols)
               cout << matrix[i][j];
            cout << '\n';
         }
         solved = true;
      }
   }
   else
      solve(0, 0);

   if(!solved)
      printf("Impossible\n");
}

int main()
{
   gi(numTrials);

   fri(t, 0, numTrials)
      runTrial(t + 1);

   return 0;
}

