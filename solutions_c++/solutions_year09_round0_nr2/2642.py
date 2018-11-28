#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAPITR(a,b)	map<a,b>::iterator
#define LISTITR(a)	list<a>::iterator

#define ITER(itr,a)	for( itr = (a).begin(); itr != (a).end(); ++itr )
#define ITERNI(itr,a)	for( itr = (a).begin(); itr != (a).end();  )
#define FORI(i,a,b)	for( int i(a), _b(b); i < _b; ++i )
#define FORD(i,a,b)	for( int i(a), _b(b); i > _b; --i )
#define FORLE(i,a,b)	for( int i(a), _b(b); i <= _b; ++i )
#define FORGE(i,a,b)	for( int i(a), _b(b); i >= _b; --i )

typedef list<char> lc;
typedef list<int> li;
typedef list<double> ld;
typedef list<string> ls;

typedef vector<char> vc;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

typedef struct Node
{
   bool visited;
   char basin;
   int elev;
   vector< struct Node* > nbors;
} Node;

vector< vector< Node* > > grid;

void visit( Node *n )
{
   if( n->visited )
      return;

   n->visited = true;

   FORI( i, 0, n->nbors.size() )
   {
      n->nbors[i]->basin = n->basin;
      visit( n->nbors[i] );
   }
}

int main()
{
   char bas;
   int nCases, elv, height, width;
   Node * nd;

   cin >> nCases;

   FORLE( i, 1, nCases )
   {
      cout << "Case #" << i << ":";
      cout << endl;

      grid.clear();
      bas = 'a';

      cin >> height; cin >> width;

      FORI( y, 0, height )
      {
         vector< Node* > v;

         FORI( x, 0, width )
         {
            cin >> elv;

            nd = new Node;
            nd->elev = elv;
            nd->visited = false;

            v.push_back( nd );
         }

         grid.push_back( v );
      }

    //  build_graph
      FORI( y, 0, height )
      {
         FORI( x, 0, width )
         {
            nd = NULL;
            //south
            if( y + 1 < height && grid[y+1][x]->elev < grid[y][x]->elev )
            {
               nd = grid[y+1][x];
            }
            //east
            if( x + 1 < width && grid[y][x+1]->elev < grid[y][x]->elev )
            {
               if( !nd || grid[y][x+1]->elev <= nd->elev )
               {
                  nd = grid[y][x+1];
               }
            }
            //west
            if( x > 0 && grid[y][x-1]->elev < grid[y][x]->elev )
            {
               if( !nd || grid[y][x-1]->elev <= nd->elev )
               {
                  nd = grid[y][x-1];
               }
            }
            //north
            if( y > 0 && grid[y-1][x]->elev < grid[y][x]->elev )
            {
               if( !nd || grid[y-1][x]->elev <= nd->elev )
               {
                  nd = grid[y-1][x];
               }
            }

            if( nd )
            {
               grid[y][x]->nbors.push_back( nd );
               nd->nbors.push_back( grid[y][x] );
            }
         }
      }

      FORI( y, 0, height )
      {
         FORI( x, 0, width )
         {
            if( !grid[y][x]->visited )
            {
               grid[y][x]->basin = bas;
               visit( grid[y][x] );

               ++bas;
            }

            if( x == 0 )
               printf( "%c", grid[y][x]->basin );
            else
               printf( "%2c", grid[y][x]->basin );
         }

         cout << endl;
      }

      FORI( y, 0, height )
      {
         FORI( x, 0, width )
         {
            delete grid[y][x];
         }

         grid[y].clear();
      }
   }

   return 0;
}  
