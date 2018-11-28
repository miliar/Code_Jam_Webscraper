// _/\_ //

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<cerrno>
#include<sstream>
#include<iomanip>
#include<streambuf>
#include<valarray>
#include<typeinfo>
#include<new>

#include<set>
#include<list>
#include<vector>
#include<bitset>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<list>
#include<algorithm>
#include<functional>
#include<utility>
#include<iterator>


#define SZ( c )                          ( ( int )  ( ( c ).size()  ) )
#define LN( str )                        ( ( int )  (  ( str ).length() ) )
#define ALL(c)                           ( c ).begin( ) , ( c ).end() 
#define TR(c,i)                          for( typeof( ( c ).begin( ) )  i  = ( c ).begin() ;  i != ( c ).end() ; i++) 
#define PRESENT(c,x)                     ( ( c ).find( x ) != ( c ).end() ) 
#define CPRESENT(c,x)                    ( find( all( c ) , x ) != ( c ).end( ) ) 
#define PB                               push_back
#define MP                               make_pair
#define MOD                              1000000007

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector < int > VI;
typedef vector < VI > VVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef pair< int , int > pii;

const long double PI = 3.141592653589793L;

vector < pair < char , char > > Translation;

int main()
{
    // first of all we make a table of all translations of the form < G , E > where G - Googlereese , E - English
    
    Translation.PB( MP( 'y' , 'a' ) );
    Translation.PB( MP( 'n' , 'b' ) );
    Translation.PB( MP( 'f' , 'c' ) );
    Translation.PB( MP( 'i' , 'd' ) );
    Translation.PB( MP( 'c' , 'e' ) );
    Translation.PB( MP( 'w' , 'f' ) );
    Translation.PB( MP( 'l' , 'g' ) );
    Translation.PB( MP( 'b' , 'h' ) );
    Translation.PB( MP( 'k' , 'i' ) );
    Translation.PB( MP( 'u' , 'j' ) );
    Translation.PB( MP( 'o' , 'k' ) );
    Translation.PB( MP( 'm' , 'l' ) );
    Translation.PB( MP( 'x' , 'm' ) );
    Translation.PB( MP( 's' , 'n' ) );
    Translation.PB( MP( 'e' , 'o' ) );
    Translation.PB( MP( 'v' , 'p' ) );
    Translation.PB( MP( 'z' , 'q' ) );
    Translation.PB( MP( 'p' , 'r' ) );
    Translation.PB( MP( 'd' , 's' ) );
    Translation.PB( MP( 'r' , 't' ) );
    Translation.PB( MP( 'j' , 'u' ) );
    Translation.PB( MP( 'g' , 'v' ) );
    Translation.PB( MP( 't' , 'w' ) );
    Translation.PB( MP( 'h' , 'x' ) );
    Translation.PB( MP( 'a' , 'y' ) );
    Translation.PB( MP( 'q' , 'z' ) );
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T; // the number of test cases
    cin >> T;
    
    int t_cases = 0;
    
    cin.ignore();
    
    while( T-- )
    {
           ++t_cases;
           
           string str;
           getline( cin , str );
           
           for(int i = 0 ; i < LN( str ) ; ++i)
           {
                   char c = str.at( i );
                   
                   for(int j = 0 ; j < SZ( Translation ) ; ++j)
                   {
                      if( Translation[ j ].first == c )
                          str.at( i ) = Translation[ j ].second ;
                      
                   }
           }
           
           cout <<"Case #"<<t_cases<<": " << str << endl;
    }
    
    getchar();
    getchar();
    
    return 0;
}
