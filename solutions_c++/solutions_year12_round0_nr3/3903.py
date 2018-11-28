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
const long sz = 2000001;

vector < pair < long , long > > Rotations;

string convertLong(long number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main()
{
    for(long i = 0 ; i < sz ; ++i)
    {
            string s = convertLong( i );
            
            if( LN( s ) == 1 )
                continue;
            
            else
            {
                set < long > S;
                
                for(long j = 0 ; j < LN( s ) - 1 ; ++j)
                {
                        string temp = "";// this is a temporary string used for finding the rotation
                        
                        for(long k = LN( s ) - j - 1 ; k < LN( s ) ; ++k)
                        temp = temp + s[ k ];
                        
                        for(long k = 0 ; k < LN( s ) - j - 1 ; ++k)
                        temp = temp + s[ k ];
                        
                        if( temp[ 0 ] == '0')
                            continue;
                        
                        else                   
                        S.insert( atol (temp.c_str() ) );
                        
                }
                
                set < long > :: iterator it;
                
                for(it = S.begin() ; it != S.end() ; ++it) 
                       if (i > *it) 
                       {
                       //cout << s << " " << *it << endl;
                       Rotations.PB( MP( atoi ( s.c_str() )  , *it ) );
                       }
            }
    }
    
    //cout << SZ( Rotations ) << endl;
    
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T; // the number of test cases
    cin >> T;
    
    int t_case = 0; // this indicates the test case number
    
    while( T-- )
    {
           ++t_case;
           
           long A , B;
           cin >> A >> B;
           
           long count = 0;       
           
           for(long i = 0 ; i < SZ( Rotations ) ; ++i)
           {
           if( Rotations[ i ].first <= B && Rotations[ i ].second >= A )
           ++count;
           }
           
           cout << "Case #" << t_case <<": " << count << endl;
    }
    
    getchar();
    getchar();
    
    return 0;
}
