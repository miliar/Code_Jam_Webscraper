
// Headers {{{
#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define CLR(A,v) memset((A),v,sizeof((A)))
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SIZE(x) (int)(x.size())
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD; 
typedef vector<string> VS;
// }}}
int T,na,nb,tt; 
char a[111],b[111]; 
vector<PII > A,B; 

int val(char a){ return a-'0'; } 
int recycling(multiset<int> outc,VI inc){ 
	sort(ALL(inc)); 

    int ret=0; 

	FORE(e,inc)
		if( outc.lower_bound(*e) != outc.end()) { 
           ++ret; 
		   outc.erase( outc.lower_bound(*e) ); 
		} 
   return ret; 
} 

int parse(char a[]){ 
   return val(a[0])*600+val(a[1])*60+val(a[3])*10+val(a[4]); 
} 

void wypisz(vector<PII >  v){ FORE(e,v) printf("%d %d\n",e->FI,e->SE); } 
	multiset<int> outc; VI inc; 

int main()
{
    scanf("%d",&T); 

	REP(nt,T){ 
		A.clear(); B.clear(); 
        scanf("%d%d%d",&tt,&na,&nb); 

		REP(i,na){ 		scanf("%s%s",a,b); A.PB(MP(parse(a),parse(b)+tt)); } 
    	REP(i,nb){ 		scanf("%s%s",a,b); B.PB(MP(parse(a),parse(b)+tt)); } 
  
		int resA,resB; 

		outc.clear(); inc.clear(); 
		FORE(e,A) outc.insert(e->FI); 
		FORE(e,B) inc.PB(e-> SE); 
		resA=SIZE(A)-recycling(outc,inc); 

			outc.clear(); inc.clear();
		FORE(e,B) outc.insert(e->FI); 
		FORE(e,A) inc.PB(e-> SE); 
		resB=SIZE(B)-recycling(outc,inc); 

		printf("Case #%d: %d %d\n",nt+1,resA,resB); 
	} 



	return 0;
}

