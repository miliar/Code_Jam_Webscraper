#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)
#define LN 1024
#define RN 1024

typedef struct Matching{
   // Required Header : vector, cstring
   // Setup before call match : ln, rn, alt

   int ln, rn, cn;      // # of left node, # of right node, Max Connection
   vector<int> alt[LN]; // adjacency list
   int c1[LN], c2[RN];  // Connection state
   int chk[RN], flag;   // Visit Check Array

   bool bpm( int p ){
      REP( i, SZ(alt[p]) ){
         int q = alt[p][i];
         if( chk[ q ] == flag ) continue;
         chk[ q ] = flag;

         if( c2[q] < 0 || bpm( c2[q] ) ){
            c2[q] = p;
            c1[p] = q;
            return 1;
         }
      }
      return 0;
   }

   void match(){
      memset(c1, -1, sizeof(c1));
      memset(c2, -1, sizeof(c2));
      memset(chk, 0, sizeof(chk));
      cn = flag = 0;
      REP( i, ln ) if( ++flag, bpm(i) ) cn++;
   }
}Matching;

typedef struct train{
	int a, b;
}train;


int main(){
	int tn;
	int cn = 1;
	cin >> tn;
	while(tn--){
		int t, na, nb, n;
		cin >> t >> na >> nb;
		n = na + nb;
		vector<train> d(n);

		REP( i, na ){
			int ha, hb, ma, mb;
			scanf("%d:%d %d:%d", &ha, &ma, &hb, &mb);
			d[i].a = ha * 60 + ma;
			d[i].b = hb * 60 + mb;
		}

		REP( i, nb ){
			int ha, hb, ma, mb;
			scanf("%d:%d %d:%d", &ha, &ma, &hb, &mb);
			d[na+i].a = ha * 60 + ma;
			d[na+i].b = hb * 60 + mb;
		}
		
		Matching mat;

		mat.ln = mat.rn = n;

		REP( i, na ){
			FOR( j, na, n ){
				// i -> j
				if( d[i].b + t <= d[j].a ) mat.alt[i].PB( j );
				// j -> i
				if( d[j].b + t <= d[i].a ) mat.alt[j].PB( i );
			}
		}	

		mat.match();

		int a, b;
		a = b = 0;
		REP( i, na ) if( mat.c2[i] == -1 ) a++;
		FOR( i, na, n ) if( mat.c2[i] == -1 ) b++;

		printf("Case #%d: %d %d\n", cn++, a, b);

	}
}
