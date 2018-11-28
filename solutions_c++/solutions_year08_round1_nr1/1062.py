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

std::vector<std::string> expand( const std::string & input, char delimiter )
{
     std::vector<std::string> out;
     int begin = 0;
     int i;
     for( i = 0; i < input.length( ); i++ )
     {
          if( i > 0 && input[i] == delimiter && input[i-1] != delimiter ) 
          { 
              out.push_back( input.substr( begin, i - begin ) ); 
              begin = i+1 ;
          }
          else
          {
              if( input[i] == delimiter ){ begin = i+1; }
          }
     }
     if( begin < i )
     {
         out.push_back( input.substr( begin ) );
     }
     return out;
}

long long INF = 1<<29;

int find_largest( vector<int> & b, vector<bool> & done )
{
    for( int i = done.size() - 1; i >= 0; --i )
    {
         if( !done[i] ) return i;
     }
     return -1;
}

int findLargest( vector<int> & a, vector< bool > & done )
{    
    int max_i = INF * -1;
    int max_p = -1;
    for( int i = 0; i < a.size(); ++i )
    {
         if( max_i < a[i] && !done[i])
         {
             max_i = a[i];
             max_p = i;
         }
     }
     return max_p;
}

int findSmallest( vector<int> & a, vector< bool > & done )
{    
    int min_i = INF;
    int min_p = -1;
    for( int i = 0; i < a.size(); ++i )
    {
         if( min_i > a[i] && !done[i])
         {
             min_i = a[i];
             min_p = i;
         }
     }
     return min_p;
}

long long solve( vector< int > & a, vector< int > & b )
{
     long long ret = 0;
     vector< bool > a_done( a.size(), false );
     vector< bool > b_done( b.size(), false );
     FOR( i, a.size() )
     {
          int s_a = findSmallest( a, a_done );
          int s_b = findLargest( b, b_done );
          ret += a[s_a] * b[s_b];
          a_done[s_a] = true;
          b_done[s_b] = true;
      }
      return ret;
     
}


int count_neg( vector<int> & a )
{
    int ret = 0;
    FOREACH( el, a )
    {
             if( *el <= 0 ) ret++;
             }
             return ret;
}


int main()
{
    ifstream ifs( "A-small-attempt1.in" );
    ofstream ofs( "a.out" );
    
    int n;
    ifs>>n;
    cout<<n<<endl;
    for( int case_num = 1; case_num <= n; ++case_num )
    {
         eatDel( ifs, '\n' );
         int vec_n;
         ifs>>vec_n;
         eatDel( ifs, '\n' );
         string line1, line2;
         getline( ifs, line1 );
         getline( ifs, line2 );
         //cout<<line1<<endl;
         //cout<<line2<<endl;
         
         vector<int> a, b;
         vector< string > as, bs;
         as = expand( line1, ' ' );
         bs = expand( line2, ' ' );
         FOREACH( el, as ) a.push_back( atoi( el->c_str() ) );
         FOREACH( el, bs ) b.push_back( atoi( el->c_str() ) );
         
         FOREACH( el, a ) cout<<*el<<" ";
         cout<<endl;
         FOREACH( el, b ) cout<<*el<<" ";
         cout<<endl;
         sort( ALL( a ) );
         sort( ALL( b ) );
         ofs<<"Case #"<<case_num<<": "<<solve( a, b )<<endl;
          
    }
    system("pause");
}
