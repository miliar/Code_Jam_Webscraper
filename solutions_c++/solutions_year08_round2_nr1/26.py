
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

LL il[3][3],tmp[3][3]; 
int it,n,M; 
LL A,B,C,D,x,y; 

LL binom(int n,int k){ 
   LL res=1; 
   REP(i,k) res=res*(LL)(n-i); 
   REP(i,k) res/=(i+1);
  return res;  
} 

int main()
{
    scanf("%d",&it); 

	REP(nt,it){ 
       scanf("%d%lld%lld%lld%lld%lld%lld%d",&n,&A,&B,&C,&D,&x,&y,&M); 

	   CLR(il,0); 

	   REP(i,n){ 
           ++il[x%3][y%3]; 
		   x=(A*x+B)%M;  y=(C*y+D)%M; 
	   } 
      
	   LL ret=0; 

	  FOR(a,0,8)
		  FOR(b,a,8)
		     FOR(c,b,8)
			   if( (a/3+b/3+c/3)%3==0 && (a%3+b%3+c%3)%3==0){
				     CLR(tmp,0); 
						  ++tmp[a/3][a%3]; ++tmp[b/3][b%3];++tmp[c/3][c%3]; 
                          LL w=1; 
						  REP(i,3) REP(j,3) w*=binom(il[i][j],tmp[i][j]); 

				    ret+=w;			  
			   } 

	    printf("Case #%d: %lld\n",nt+1,ret); 
	} 

	return 0;
}

