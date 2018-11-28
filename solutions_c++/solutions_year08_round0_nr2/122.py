#include <cstdio>
#include <set>

using namespace std;

struct Event {
   int type, id;
   int t1, t2;

   Event( int Type, int Id, int T1, int T2 ) {
      type = Type;
      id = Id;
      t1 = T1;
      t2 = T2;
   }
};

bool operator < ( const Event &A, const Event &B ) {
   if( A.t1 != B.t1 ) return A.t1 < B.t1;
   if( A.type != B.type ) return A.type < B.type;
   return A.id < B.id;
}

int main( void ) {
   int T;
   scanf( "%d", &T );

   for( int tt = 1; tt <= T; ++tt ) {
      set<Event> E;

      int turn, nA, nB, hh1, mm1, hh2, mm2;
      scanf( "%d%d%d", &turn, &nA, &nB );
      for( int i = 0; i < nA; ++i ) {
         scanf( "%d:%d %d:%d", &hh1, &mm1, &hh2, &mm2 );
         E.insert( Event( 1, i, hh1*60+mm1, hh2*60+mm2 ) );
      }
      for( int i = 0; i < nB; ++i ) {
         scanf( "%d:%d %d:%d", &hh1, &mm1, &hh2, &mm2 );
         E.insert( Event( 2, i, hh1*60+mm1, hh2*60+mm2 ) );
      }

      int retA = 0, retB = 0;
      int A = 0, B = 0;

      while( !E.empty() ) {
         Event e = *E.begin(); 
         E.erase( E.begin() );

         if( e.type == -1 ) ++A;
         if( e.type == -2 ) ++B;
         if( e.type == 1 ) {
            if( A == 0 ) ++retA;
            else --A;
            E.insert( Event( -2, e.id, e.t2 + turn, -1 ) );
         }
         if( e.type == 2 ) {
            if( B == 0 ) ++retB;
            else --B;
            E.insert( Event( -1, e.id, e.t2 + turn, -1 ) );
         }
      }

      printf( "Case #%d: %d %d\n", tt, retA, retB );
   }
   return 0;
}
