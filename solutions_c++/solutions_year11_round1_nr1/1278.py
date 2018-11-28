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
#include <functional>
#include <math.h>

using namespace std;

ifstream fin( "a-small.in" );
ofstream fout( "answer.out" );

#define in fin
#define cout fout
#define pf printf

#define g(name) 	in >> name
#define gi(name)	int name;		g(name)
#define gl(name)	long name;		g(name)
#define gd(name)	double name; 	g(name)
#define gc(name)	char name;		g(name)
#define gb(name)	bool name;		g(name)

#define fri(var, a, b)		for( int var = a; var < b; var++ )
#define frd(var, a, b) 	   for( int var = a; var > b; var-- )

int main()
{
   gi(numTrials);

   fri(i, 0, numTrials)
   {
      gi(n);
      gi(pd);
      gi(pg);

      bool works = false;
      for( int j = n; j > 0; j-- ) {
         if( ( pd * j ) % 100 == 0 )
            works = true;
      }

      bool possible = works;
      if( pg == 0 && pd != 0 )
         possible = false;

      if( pg == 100 && pd != 100 )
         possible = false;

      cout << "Case #" << i + 1 << ": ";
      if( possible )
         cout << "Possible\n";
      else
         cout << "Broken\n";
   }

   return 0;
}

