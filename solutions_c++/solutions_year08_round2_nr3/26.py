
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

const int ogr=1000100; 
int w[ogr]; 

class tree{ 
	public: 
	   int t[ogr]; 

	   void init(){ 
         CLR(t,0); 
	   } 

	   void add(int a){ 
          int pt=1;

		  while(a<ogr){
              ++t[a];   
			   while( (a&pt)!=pt)  pt*=2;	
			   a+=pt; 
		  }
	   } 

	   int sum(int b){ // returns number of free cells among 1,2,...,b
         int pt=1,sm=0,a=b; 
		 while(a){ 
            sm+=t[a]; 
			   while( (a^pt)!=a-pt) pt*=2; 
			  a-=pt;  
		 } 
         return b-sm; 
	   }      
}D ; 

int main()
{
   int T,K; 
   scanf("%d",&T); 

   FOR(nt,1,T){ 
        scanf("%d",&K); 

         D.init(); CLR(w,0); 
		 int st=1,lf=K-1,r; 

		 D.add(1); w[1]=1; 
		 
		FOR(p,2,K){ 
             r=(p-1)%lf+1; 
              
              int d=D.sum(K) - D.sum(st-1),i; 
			  if(r<=d) i=D.sum(st-1)+r; 
			  else i=r-d; 

			 int x=1,y=0,z=K; 

			  while(z-x){
				//  printf("%d %d %d\n",x,y,z);  
                y=(x+z)/2; 
				if(D.sum(y)<i) x=y+1; else z=y; 
			  }  

			  w[x]=p; D.add(x); st=x;  
                    
			--lf; 
		}
		int il; 
	   scanf("%d",&il); 	
	   int tb[111]; 
	   REP(i,il) scanf("%d",&tb[i]); 
	   printf("Case #%d: ",nt); 
	   REP(i,il) printf("%d ",w[tb[i]]); 
	   puts(""); 

//		FOR(p,1,K) printf("%d ",w[p]); puts(""); 
   } 

	return 0;
}

