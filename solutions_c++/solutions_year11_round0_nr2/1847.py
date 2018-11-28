#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main(void)
{
  
  int tc, cnt = 0;
  cin >> tc;  

  const int N = 'Z' + 1;
  char C[N][N];
  bool D[N][N];

  while( tc-- ){

    fill( &C[0][0], &C[N-1][N], '@' );
    fill( &D[0][0], &D[N-1][N], false );

    int c, d, n;

    cin >> c;    
    for(int i=0; i<c; ++i){
      char s, t, u;
      cin >> s >> t >> u;
      C[ s ][ t ] = C[ t ][ s ] = u;
    }

    cin >> d;
    for(int i=0; i<d; ++i){
      char s, t;
      cin >> s >> t;
      D[ s ][ t ] = D[ t ][ s ] = true;
    }
    
    cin >> n;
    vector<char> v;
    map<char, int> num;
    while( n-- ){
      char e;
      cin >> e;

      //for(int i=0; i<v.size(); ++i)cout << v[i] << ' '; cout << ": " << e << endl;

      while( v.size() ){
        char next = C[ v.back() ][ e ];
        //cout << v.back() << " + " << e << " = " << next << endl;
        if( next == '@' )break;
        --num[ v.back() ];
        v.pop_back();
        e = next;
      }

      bool init = false;
      for(char i='A'; i<='Z'; ++i){
        if( D[e][i] && num[i] ){
          init = true;
          break;
        }
      }
      if( init ){
        num = map<char, int>();
        v = vector<char>();
        continue;
      }

      v.push_back( e );
      ++num[ e ];
    }


    cout << "Case #" << ++cnt << ": " << "[" << flush;
    for(int i=0; i<v.size(); ++i){
      if(i)cout << ", ";
      cout << v[i];
    }
    cout << "]" << endl;        
  } 
  return 0;
}
