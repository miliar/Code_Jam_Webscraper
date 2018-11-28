
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

const int maxN=10010; 
const int INF=(1<<29); 

bool change[maxN],kind[maxN]; 
int res[maxN][2]; 
int N,V,it; 

int main()
{
   scanf("%d",&it);

  FOR(nt,1,it){ 
      scanf("%d%d",&N,&V); 

	  int nh=N/2,a,b;  

	  FOR(p,1,nh){
		  scanf("%d%d",&a,&b); 
		  kind[p]=a; change[p]=b; 
	  } 

	  FOR(p,nh+1,N){ 
          scanf("%d",&a); 
		  res[p][0]=res[p][1]=INF; 
		  res[p][a]=0; 		  
	  } 

      FORD(p,nh,1){ 
     	  res[p][0]=res[p][1]=INF; 
		  a=2*p; b=2*p+1; 

		  if(kind[p]){ 
		     res[p][1]=min(res[p][1],res[a][1]+res[b][1]); 	  

			 if(change[p])
				 REP(i,2) REP(j,2) if(i+j)
				  res[p][1]=min(res[p][1],res[a][i]+res[b][j]+1); 	  

			 REP(i,2)REP(j,2) if( i*j==0)
			 res[p][0]=min(res[p][0],res[a][i]+res[b][j]); 
		  } 
          else { 
             REP(i,2)REP(j,2) if( i || j )
			 res[p][1]=min(res[p][1],res[a][i]+res[b][j]); 
    
			 res[p][0]=min(res[p][0],res[a][0]+res[b][0]); 

			 if(change[p])
				 REP(i,2)REP(j,2) if( !i || !j) 
				 res[p][0]=min(res[p][0],res[a][i]+res[b][j]+1);		 
		  } 
	  } 

	  printf("Case #%d: ",nt); 
	  if(res[1][V]<INF) printf("%d\n",res[1][V]); else puts("IMPOSSIBLE");
  } 



	return 0;
}

