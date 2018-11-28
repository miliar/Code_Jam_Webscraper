
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
const LL P=1000000009; 
const int maxN=555; 
int T,n,c;  
VI v[maxN]; 
int o[maxN]; 
bool vis[maxN]; 
int a,b; 

LL odw(LL a){ 
  REP(i,a+1) if( (P*(LL)i+1)%a==0) return (P*(LL)i+1)/a; 
 return 0; 
} 

LL binom(LL n,LL k){
  // printf("%lld %lld\n",n,k); 	
	if(k>n || k<0 || n<0) return 0; 
   LL ret=1; 
   REP(i,k) ret=(ret*(n-i))%P; 
//   REP(i,k) ret=(ret*odw(i+1))%P; 
  return ret;  
} 

LL result; 

void dfs(int w){
//   printf("w: %d size: %d \n",w,SIZE(v[w])-1); 	
    if(o[w]==0) (result*=binom(c,SIZE(v[w])))%=P; 
	else (result*=binom(c-SIZE(v[o[w]]),SIZE(v[w])-1))%=P;  	     	        
	vis[w]=1;
  // printf("%d %lld\n",w,result); 	
	FORE(e,v[w]) if(!vis[*e]){
	 o[*e]=w; 	dfs(*e); 	
	} 
} 


int main()
{
   scanf("%d",&T); 

   FOR(tc,1,T){ 
	   scanf("%d%d",&n,&c);
	   REP(i,maxN)v[i].clear(); 
	   REP(i,n-1) { 
           scanf("%d%d",&a,&b); 
		   v[a].PB(b); v[b].PB(a); 
	   } 
	   result=1;
//	    FOR(p,1,n) printf("size: %d\n",SIZE(v[p]));  
	   CLR(vis,0);CLR(o,0); 
	   dfs(1); 
	   printf("Case #%d: %lld\n",tc,result); 	  
   } 

	return 0;
}

