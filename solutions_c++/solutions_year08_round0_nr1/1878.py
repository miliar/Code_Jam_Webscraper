////////////////////////////////////////////////////////////////////////
/// Google Code.jam 2008 -- A. Saving the Universe
/// George Vafiadis [gvafiadis@gmail.com]
/// gcc version 4.2.1 [SUSE Linux]
/// Greece
////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include <map>
#include <vector>
using namespace std;

int readInt(ifstream &inp)
{
  char name[102];
  inp.getline( name, 100 );
 
  return atoi(name);
}

std::string readWord(ifstream &inp)
{
  char name[102];
  inp.getline( name, 100 );
  return std::string(name);
}

void solve(int id, vector<std::string> & e, vector<std::string> & q);

int main(int argc, char ** argv)
{
 if( argc != 2 ) 
 { cout << "Google Code.jam 2008 -- A. Saving the Universe" << endl << argv[0] << " [input file] " << endl;
   return 0;
 }
 
 ifstream inp(argv[1]);
 
 int N;   ///< Number of cases
 int S;   ///< Number of search engines
 int Q;   ///< Number of queries

 N = readInt(inp);

 for(int i = 0; i < N; ++i)
 {
   vector<std::string> engines;    ///< All search engines
   vector<std::string> queries;    ///< Queries

  S = readInt(inp);

  for(int j = 0; j < S; ++j)
  {
   char name[102];
   inp.getline( name, 100 );

   engines.push_back( name );  
  }

 Q = readInt(inp);

 for(int k = 0; k < Q; ++k)
  {
   char name[102];
   inp.getline( name, 100 );

   queries.push_back( name );  
  }

 solve( i+1, engines, queries );
 }

 inp.close(); 

 return 0;
}


void solve(int id, vector<std::string> & e, vector<std::string> & q)
{
 const int & S = e.size();
 const int & Q = q.size();

 map<std::string, bool> checked;
 
 for(int i = 0; i < S; ++i)
  checked[e[i]] = false;

 int changes = 0;
 int top = 0;
 int remain = S;

 while( top < Q )
 {
  std::string query = q[top];

  if( checked[query] == false )
   {
     if( remain == 1 )
       {
        for( map<std::string, bool>::iterator ii = checked.begin(); ii != checked.end(); ++ii)
          (*ii).second = false;

        remain = S-1;
        ++changes;
       }
     else
        --remain;

     checked[query] = true;
   }

  ++top;
 }

 cout << "Case #" << id << ": " << changes << endl;
}
