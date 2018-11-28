#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

#define FOR( i, n ) for( int (i) = 0; (i) < (n); ++(i) ) 
#define FORR( i, n, m ) for(int (i) = (n); (i) <= (m); ++(i) ) 
#define FOREACH(_it,_l) for(__typeof((_l).begin()) _it=((_l).begin());(_it)!=(_l).end();(_it)++) 
#define ALL(x) (x).begin(),(x).end() 
#define eatDel( ifs, del ) while( ifs.peek() == del ) ifs.ignore(); 
#define isMaped( m, element ) ((m).find( (element) ) != (m).end()) 

using namespace std;

void emptyMap( map<string,int> & m )
{
     FOREACH( p, m )
     {
              p->second = 0;
              }
 }

int main()
{
    ifstream ifs( "A-small-attempt4.in" );
    ofstream ofs( "a.out" );
    
    int n;
    ifs>>n;
    for( int case_num = 1; case_num <= n; ++case_num )
    {
         int num_engines;
         ifs>>num_engines;
         map<string,int> freq_table;
         for( int engine = 0; engine < num_engines; ++engine )
         {
              eatDel( ifs, '\n' );
              string engine_str;
              getline( ifs, engine_str );
              freq_table[ engine_str ] = 0;    
         }
         int min_freq = 0;
         
         int num_searches;
         ifs>>num_searches;
         int z = num_engines;
         for( int searches = 0; searches < num_searches; ++searches )
         {
              eatDel( ifs, '\n' );
              string search;
              getline( ifs, search );
              if( isMaped( freq_table, search ) && freq_table[search] == 0 )
              {
                  cout<<search<<endl;
                  freq_table[search] = 1;
                  z--;
                  cout<<z<<endl;
              }
              if( z == 0 )
              {
                  z = num_engines-1;
                  min_freq++;
                  emptyMap( freq_table );
                  freq_table[search] = 1;
              }
                
              
         }
        
         ofs<<"Case #"<<case_num<<": "<<min_freq<<endl;
    }
    ifs.close();
    ofs.close();
    
    system( "pause" );
}
