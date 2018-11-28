
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

const int ogr=1111000; 
int f[ogr],r[ogr]; 

int father(int a){ if(f[a]!=a) f[a]=father(f[a]); return f[a]; } 

void join(int a,int b){ 
   int x=father(a),y=father(b); 
   if(x==y)return ; 
       if(r[x]<r[y]) { 
         f[x]=y; 
	   } 
	   else { 
           f[y]=x; 
		   if(r[x]==r[y])++r[x]; 
	   } 
}

bool prime(int a){ 
  if(a<2) return 0; 
   if(a<4) return 1; 

  int b=2; 
  while(b*b<a && a%b!=0) ++b; 
  return a%b!=0; 
} 

bool pr[ogr]; 
int it; 
LL A,B,P; 
int main()
{
   REP(i,ogr) pr[i]=prime(i); 

	scanf("%d",&it); 

	REP(nt,it){ 
         scanf("%lld%lld%lld",&A,&B,&P); 
		 int df=B-A; 

		 FOR(p,0,df) {f[p]=p; r[p]=0; } 

		 LL l=P;

		 while(l<=df){ 
             LL fs=((A-1)/l+1)*l; 
			if(pr[l])  while(fs+l<=B){ join(fs-A, fs+l-A); fs+=l; } 
			 ++l; 
		 } 

		 int res=0; 
		 FOR(p,0,df) if(f[p]==p)++res; 
		printf("Case #%d: %d\n",nt+1,res); 
	} 



	return 0;
}

