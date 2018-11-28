
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

char s[1111]; 
VS names; 
set<string> remain; 

void newRemain(){ 
  FORE(e,names)remain.insert(*e); 
} 

int main()
{
	int T; 
   scanf("%d",&T); 

   REP(nt,T){ 
	   names.clear();
	   remain.clear();  

	   int n,m,res=0;
      scanf("%d\n",&n);  

        REP(i,n){ 
            gets(s); 
			int d=strlen(s); 
		    string nm=""; 
			REP(j,d)nm+=s[j];
			//printf("%s\n",nm.c_str()); 
			names.PB(nm); 
		} 

		newRemain(); 

	      scanf("%d\n",&m); 
	        REP(i,m){ 
               gets(s); 
      			int d=strlen(s); 
        		    string nm=""; 
		     	REP(j,d)nm+=s[j]; 		
				remain.erase(nm); //			printf("%s\n",nm.c_str()); 
				if(SIZE(remain)==0){++res; newRemain();remain.erase(nm);  } 			
			} 		

			printf("Case #%d: %d\n",nt+1,res); 		
   } 
	return 0;
}

