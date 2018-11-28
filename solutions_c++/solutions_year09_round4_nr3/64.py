#include <vector>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>

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
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end();++it)

#define LN 128
#define RN 128

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

VI dt[101];
VI da[101];
int n,m;

bool comp(VI& a,VI& b)
{
	REP(i,m) if (a[i]>=b[i]) return false;
	return true;
}

int main()
{
	int tn;

	cin>>tn;
	FOR(qq,1,tn+1) {
		cin>>n>>m;
		REP(i,n) dt[i].clear();

		REP(i,n) REP(j,m) {
			int ka;
			cin>>ka;
			dt[i].PB(ka);
		}

		Matching mt;
		mt.ln=mt.rn=n;
		REP(i,n) REP(j,n) if (comp(dt[i],dt[j]))
			mt.alt[i].PB(j);
		
		mt.match();

		printf("Case #%d: %d\n",qq,n-mt.cn);
	}
	return 0;
}
