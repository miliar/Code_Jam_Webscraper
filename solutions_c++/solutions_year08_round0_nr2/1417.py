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

#define LN 105
#define RN 105

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

int ret(int h,int m)
{
	return h*60+m;
}

int main()
{
	int tn,qq=0;

	cin>>tn;
	while (tn--) {
		int tm,n,m;
		cin>>tm;

		cin>>n>>m;
		VPII da(n),db(m);
		REP(i,n) {
			int a,b,c,d;
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			da[i].ST=ret(a,b);
			da[i].ND=ret(c,d);
		}
		REP(i,m) {
			int a,b,c,d;
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			db[i].ST=ret(a,b);
			db[i].ND=ret(c,d);
		}

		Matching ma,mb;
		ma.ln=n;
		ma.rn=m;
		REP(i,n)
			REP(j,m)
				if (da[i].ND+tm<=db[j].ST)
					ma.alt[i].PB(j);
		mb.ln=m;
		mb.rn=n;
		REP(i,m)
			REP(j,n)
				if (db[i].ND+tm<=da[j].ST)
					mb.alt[i].PB(j);

		ma.match();
		mb.match();

		printf("Case #%d: %d %d\n",++qq,n-mb.cn,m-ma.cn);
	}
	return 0;
}
