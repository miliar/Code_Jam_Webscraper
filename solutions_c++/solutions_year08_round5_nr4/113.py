
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

vector<PII > V; 
int H,W,R,T; 
const int P=10007; 
int odw[P]; 
LL war[P];


LL binom(int n,int k){ 
   if( n/P > (n-k)/P +k/P) return 0; 

   return (war[n%P] * odw[war[(n-k)%P]] * odw[war[k%P]])%P; 
   
   /*   LL ret=1; 
   REP(i,k) {ret*=(n-i); ret/=(i+1); }
   return ret%P; 
   */
} 

LL ways(int a,int b){ 
   if( (a+b)%3!=0) return 0; 
   if( a<0 || b<0) return 0; 
   int u=(a+b)/3; 
   if( a<u || b<u) return 0; 
   a-=u; 
   b-=u; 
   return binom(a+b,b); 
} 

int main()
{
	FOR(p,1,P-1) FOR(k,1,P-1) if( (p*k)%P==1) odw[p]=k; 
	war[0]=war[1]=1; 
	FOR(p,1,P-2) war[p+1]=(war[p]*(p+1))%P; 

   scanf("%d",&T); 

   FOR(tc,1,T){
	   scanf("%d%d%d",&H,&W,&R); 

	   V.clear();
	  int x,y;  
	   REP(i,R){scanf("%d%d",&x,&y); V.PB(MP(x,y)); } 
       sort(ALL(V)); 

	   LL ret=0; 

       REP(mask,(1<<SIZE(V))){ 
            vector<PII > tmp; 
             tmp.PB(MP(1,1));
			   LL cnt=1;  
              REP(i,R) if( (mask&(1<<i))){ tmp.PB(V[i]); cnt*=(-1); } 
             tmp.PB(MP(H,W)); 
			  
            REP(i,SIZE(tmp)-1) 
                  cnt=(cnt*ways(tmp[i+1].FI-tmp[i].FI,tmp[i+1].SE-tmp[i].SE))%P; 
           ret+=cnt; 			
	   } 
     printf("Case #%d: %lld\n",tc,(ret%P+P)%P); 
   } 



	return 0;
}

