///Team Heisenbug
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <cassert>
#include <vector>
#include <fstream>
#include <stack>
#include <cstring>
#include<sys/time.h>
/*****************************************************************************************************
					macros and typedefs for shortening length
******************************************************************************************************/
///Fast IO
//#define FASTIO
const int BUFFSIZE = 10240;
char BUFF[BUFFSIZE + 1], *p = BUFF;
int CHAR, SIGN, BYTES = 0;
#define GETCHAR(c) {								\
	if(p-BUFF==BYTES && (BYTES==0 || BYTES==BUFFSIZE)){BYTES=fread(BUFF,1,BUFFSIZE,stdin);p=BUFF;}	\
	if(p-BUFF==BYTES && (BYTES>0 && BYTES<BUFFSIZE)){BUFF[0]=0;p=BUFF;}					\
	c = *p++;										\
}
#define DIGIT(c) (((c) >= '0') && ((c) <= '9'))
#define LETTER(c)(((c) >= 'a' && (c) <= 'z') || ((c) >= 'A' && (c) <= 'Z'))
#define MINUS(c) ((c)== '-')
#define GETNUM(n) {								\
	n = 0;SIGN = 1; do{GETCHAR(CHAR);}while(!(DIGIT(CHAR)|| MINUS(CHAR)));	\
	if(MINUS(CHAR)){SIGN = -1; GETCHAR(CHAR);}		\
	while(DIGIT(CHAR)){n = 10*n + CHAR-'0'; GETCHAR(CHAR);}if(SIGN == -1){n = -n;}\
}
#define GETWORD(s,i) {								\
	i = 0;do{GETCHAR(s[i]);}while(!LETTER(s[i]));	\
	do{GETCHAR(s[++i]);}while(LETTER(s[i]));	\
	s[i]=0;													\
}

///Fast IO ends
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define SZ(c) (c).size()
#define ps(n) printf("%s\n",n)
#ifdef FASTIO
	#define s(n) GETNUM(n)
	#define sl(n) GETNUM(n)
	#define ss(n) int __l = 0;GETWORD(n,__l)
#else
	#define s(n) scanf("%d",&n)
	#define ss(n) scanf("%s",n)
	#define sl(n) scanf("%lld",&n)
#endif
typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

/*****************************************************************************************************
							Program starts here
******************************************************************************************************/
///macros for global constants
#define MAXN 100011
#define DEBUG 0
int O[105],R[105];
char seq[105];
int ocnt,rcnt;

int main()
{
	int T;
	s(T);
	for(int cases=1;cases<=T;cases++)
	{
		int N;
		s(N);
		ocnt=0;
		rcnt=0;
		REP(i,N)
		{
			int x;
			char c[2];
			scanf("%s %d",c,&x);
			if(c[0]=='O')O[ocnt++]=x;
			else R[rcnt++]=x;
			seq[i]=c[0];
		}
		
		int oind=0,rind=0,i=0;
		int x=1,y=1,T=0;
		
		while(i<N)
		{
			//printf("%d %d : %d %d %d %d->",T,i,x,y,rind,oind);
			if(seq[i]=='O')
			{
				if(x<O[oind])			//o moves forward
				x++;
				else if(x==O[oind])
				{
					i++;				//o pushes button
					oind++;
				}
				else if (x>O[oind])		//o moves back
				x--;
				
				if(rind<rcnt)
				{
					if(y<R[rind])		//r moves forward
					y++;
					else if(y>R[rind])	//r moves backward
					y--;
				}
			}
			else
			{
				if(oind<ocnt)
				{
					if(x<O[oind])		//o moves
					x++;
					else if(x>O[oind])
					x--;
				}
				
				if(y<R[rind])			//r moves
				y++;
				else if(y==R[rind])
				{
					i++;
					rind++;
				}
				else if(y>R[rind])
				y--;
			}
			T++;
			//printf(" %d %d %d %d\n",x,y,rind,oind);
		}
		printf("Case #%d: %d\n",cases,T);
	}
	return 0;
}
