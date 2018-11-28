
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
typedef vector<PII> VPI; 
map<string,int> M; 
int il; 
const int maxN=333; 
VPI v[maxN]; 
int T,N;  
const int inf=(1<<30); 

int number(string s){ 
   if(M.find(s)!=M.end()) return M[s]; 
   M[s]=il++; 
   return il-1;
} 

int main()
{
	scanf("%d",&T); 

	FOR(tc,1,T){ 
		scanf("%d",&N); 
		il=0; M.clear(); 
		REP(i,maxN)v[i].clear(); 

		int a,b; char s[2134]; 
		REP(i,N){ 			   
			scanf("%s%d%d",s,&a,&b); 
			string tmp=s; 
			v[number(tmp)].PB(MP(a,b)); 
		} 

		il=max(il,3); 
		int res=inf; 

		FOR(a,0,il-1)
			FOR(b,a+1,il-1)
			FOR(c,b+1,il-1){ 
				VPI u; 
				FORE(e,v[a])u.PB(*e); 
				FORE(e,v[b])u.PB(*e); 
				FORE(e,v[c])u.PB(*e); 
				sort(ALL(u)); 
				int pr=0,ok=1,up=0,cnt=0; 

				while(1){ 
					int g=-1,wh=-1; 

					while(u[pr].FI<=up+1 && pr<SIZE(u)){ 
						if(u[pr].SE>wh){ 
							wh=u[pr].SE; 
							g=pr; 
						} 
						++pr; 
					} 
					if(wh==-1) { ok=0; break; } 
					else { 
						up=wh; 
						++cnt; 
					}
				
					if(pr==SIZE(u) ||  up==10000)break; 
				} 
				if(ok && up==10000) res=min(res,cnt); 

			} 
		printf("Case #%d: ",tc); 
		if(res<inf) printf("%d\n",res); else puts("IMPOSSIBLE"); 

	} 



	return 0;
}

