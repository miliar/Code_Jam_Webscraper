#include <cstdio>
#include <cstring>
#include <queue>
#include <string>
#include <vector>
using namespace std;
const int NULA = 0;

class trie {
public:
  struct node {
    node *next[27];
    node( void ) { memset( next, 0, sizeof( next ) ); } 
  };

  typedef node* node_ptr;

  void insert( node_ptr& gdje, char *S ) {
    if( gdje == 0 ) gdje = new node;
    if( S[0] == 0 ) { gdje->next[26] = root; return; }

    insert( gdje->next[ S[0] - 'a' ], S+1 );
  }
  
  node *root;

  trie( void ) : root( 0 ), spaces( 0 ) {}
  void insert( char *S ) { insert( root, S ); }
  
  int spaces;
  void write( node *gdje ) {
    if( gdje == 0 ) return;

    for( int i = 0; i < 26; ++i ) {
      if( gdje->next[i] == 0 ) continue;
      for( int j = 0; j < spaces; ++j ) printf( " " );
      ++spaces;
      printf( "%c\n", 'a'+i );
      write( gdje->next[i] );
      --spaces;
    }
  }
};

int l, d, n;
char buff[ 3000 ];
trie T;
inline void input( void ) {
  scanf( "%d%d%d", &l, &d, &n );
  for( int i = 0; i < d; ++i ) {
    scanf( " %s", buff );
    T.insert( buff );
  }
//  T.write( T.root );
}

struct stanje {
  trie::node_ptr P;
  int depth;
//  string S;

  stanje( void ) : P( 0 ), depth( -1 ) {}
  stanje( trie::node_ptr _P, int _depth ) : P( _P ), depth( _depth ) {}
//  stanje( trie::node_ptr _P, int _depth, string _S ) : P( _P ), depth( _depth ), S( _S ) {}

  const trie::node_ptr& operator[]( int x ) { return P->next[x]; }
};

queue< stanje > Q;
vector< string > A;

inline void parse( char *S, vector< string > &A ) {
  A = vector< string >();
  for( int i = 0; S[i]; ++i )
    if( S[i] == '(' ) {
      A.push_back( "" );
      for( ++i; S[i] != ')'; ++i )
        A.back() += S[i];
    }
    else
      A.push_back( string( 1, S[i] ) );
}

inline int solve( char *S ) {
  int sol = 0;
  parse( S, A );
  Q = queue< stanje >();

  for( Q.push( stanje( T.root, 0 ) ); !Q.empty(); Q.pop() ) {
    stanje sad = Q.front();
//    printf( "%d\n", sad.depth );
    
    if( sad[26] ) { ++sol; continue; }
    for( int i = 0; i < (int)A[sad.depth].size(); ++i )
      if( sad[ A[sad.depth][i] - 'a' ] != 0 ) {
//        printf( "postoji za %c\n", A[sad.depth][i] );
        Q.push( stanje( sad[ A[sad.depth][i] - 'a' ], sad.depth+1 ) );
      }
  }

  return sol;
}

int main( void ) {
  input();
  for( int i = 0; i < n; ++i ) {
    scanf( " %s", buff );
    printf( "Case #%d: %d\n", i+1, solve( buff ) );
  }

  return NULA;
}


