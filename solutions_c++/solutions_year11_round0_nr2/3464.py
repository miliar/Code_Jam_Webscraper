#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <utility>
#include <deque>
using namespace std;

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "out", "w", stdout );
     
    int T;
    cin >> T;
    for( int i = 1; i <= T; ++i ){
         string out;
         map<pair<char,char>, char> cmp;
         map<pair<char,char>, char> dmp;
         cmp.clear();        
         dmp.clear();
         
         int n; 
         cin >> n;
         for( int p = 0 ; p < n; ++p ){
              char c[2], c3;
              cin >> c[0] >> c[1] >> c3;
              sort( c, c + 2 );
              cmp[make_pair( c[0], c[1] )] = c3;
         }
         
         cin >> n ;
         for( int p = 0; p < n; ++p ){
              char c[2];
              cin >> c[0] >> c[1];
              sort( c, c + 2 );
              dmp[make_pair( c[0], c[1] )] = 'a';
         }
         
         cin >> n;
         for( int p = 0; p < n; ++p ){
              char c;
              cin >> c;
              bool b = false;
              
            
              if( out.size() > 0 && ! cmp.empty() ){
                  char cc[2]; 
                  cc[0] = c; 
                  cc[1] = out[ out.size() -1 ];
                  sort( cc, cc + 2 );
                  if( cmp.find( make_pair( cc[0], cc[1] ) ) != cmp.end() ) {
                      char ctmp = cmp[ make_pair( cc[0], cc[1] ) ];                      
                      out[out.size()-1] = ctmp;
                      continue;
                  }
              }
              
              if( out.size() > 0 && !dmp.empty() ){
                  for( int i = 0; i < out.size(); ++i ){
                       char cc[2];
                       cc[0] = c;
                       cc[1] = out[i];
                       sort( cc, cc + 2 );
                       if( dmp.find( make_pair( cc[0], cc[1] ) ) != dmp.end() ){
                           out = "";
                           b = true;
                           break;
                       }
                  } 
              }
              if( !b ) out += c;
              //cout << out << endl;
         }
         
         cout << "Case #" << i << ": [" ;
         if( out.size() > 0 ){ 
                  for( int p = 0; p < out.size() - 1; ++p ){
                       cout << out[p] << ", ";
                  }
                       cout << out[out.size() -1];
         }
         cout << ']' << endl;
          
    }    
}
