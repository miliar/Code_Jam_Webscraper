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
#define MAXN 16
int A[MAXN];

int add(int x,int y)
{
	//perform patrick's add
	int res = 0;
	//printf("%d + %d = ",x,y);
	for(int i=0;i<32;i++)
	{
		int bit = (x&1) + (y&1);
		bit &= 1;
		
		if(bit)
		res |= (1<<i);
		
		x >>= 1;
		y >>= 1;
	}
	//printf("%d\n",res);
	return res;
}	
int main()
{
	/*
	add(5,4);
	add(7,9);
	add(50,10);
	*/
	
	int T;
	s(T);
	FOR(cases,1,T+1)
	{
		int N;
		s(N);
		REP(i,N)
		s(A[i]);
		
		//brute force
		int res = -1;
		FOR(msk,0,(1<<N))
		{
			//0's as for SEAN
			int osum = 0;
			int zsum = 0;
			
			int s0 = 0;
			int s1 = 0;
			
			FOR(i,0,N)
			{
				if(msk&(1<<i))
				{
					osum = add(osum,A[i]);
					s1 += A[i];
				}
				else
				{
					zsum = add(zsum,A[i]);
					s0 += A[i];
				}
			}
			
			if(osum == zsum && s1>0 && s0>0)
			{
				//printf("MASK:%d %d %d %d %d\n",msk,osum,zsum,s0,s1);
				res = max(res,s0);
			}
		}
		printf("Case #%d: ",cases);
		if(res == -1)
		printf("NO\n");
		else
		printf("%d\n",res);
	}
	return 0;
}
