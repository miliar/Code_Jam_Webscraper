
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

char S[1111],tmp[1111]; 
int T,k,pr[5];  

int main()
{
    scanf("%d",&T); 

	FOR(nt,1,T){ 
        scanf("%d",&k); 
		scanf("%s",S); 

		REP(i,k) pr[i]=i; 

		int d=strlen(S),ret=1111; 

		do{ 
		    REP(i,d) tmp[(i/k)*k+pr[i%k]]=S[i]; 
			int cnt=1; 
			REP(i,d-1) if(tmp[i]!=tmp[i+1])++cnt; 
			if(cnt<ret)ret=cnt; 
		} while(next_permutation(pr,pr+k)); 

      printf("Case #%d: %d\n",nt,ret); 


	} 



	return 0;
}

