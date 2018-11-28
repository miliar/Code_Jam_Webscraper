
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
int it,N,M,A; 

int main()
{
  scanf("%d",&it); 

  FOR(nt,1,it){ 
	  bool sw=0,pos=1; 

      scanf("%d%d%d",&N,&M,&A); 
	  if(N<M){ swap(N,M); sw=1; } 
	  int a,b,c,d,Ap; 
  
      if(A>N*M) pos=0; 
	  else {
		 Ap=((A+N-1)/N)*N;  
		 a=N; 
		 d=Ap/N; 
		 b=1; 
         c=Ap-A;
//		printf("%d %d %d %d %d\n",Ap,a,b,c,d);  

       if(sw) { swap(a,b); swap(c,d); swap(N,M); } 
 	   if(abs(a*d-b*c)!=A)puts("kupa"); 
		  if( max(a,c)>N || max(b,d)>M) printf("dupa\n"); 
      } 
	 

	  printf("Case #%d: ",nt);
 

	  if(pos) printf("0 0 %d %d %d %d\n",a,b,c,d);
	  else puts("IMPOSSIBLE"); 
  } 

	return 0;
}

