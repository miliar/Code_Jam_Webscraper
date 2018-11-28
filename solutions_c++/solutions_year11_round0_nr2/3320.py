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

int C[300][300];
bool O[300][300];
char S[500];
char A[500];

int main()
{
	int T;
	s(T);
	for(int cases=1;cases<=T;cases++)
	{
		memset(C,0,sizeof C);
		memset(O,0,sizeof O);
		int c,d,n,alen=0;
		s(c);
		REP(i,c)
		{
			char tmp[100];
			ss(tmp);
			C[0][0]=0;
			C[tmp[0]][tmp[1]]=tmp[2];
			C[tmp[1]][tmp[0]]=tmp[2];
		}
		s(d);
		REP(i,d)
		{
			char tmp[100];
			ss(tmp);
			O[tmp[0]][tmp[1]]=1;
			O[tmp[1]][tmp[0]]=1;
		}
		s(n);
		ss(S);
		FOR(i,0,n)
		{
			//A[alen]=0;
			//cout<<A<<endl;
			if(alen==0)
			{
				A[alen++]=S[i];
				continue;
			}
			if(C[A[alen-1]][S[i]]!=0)
			{
				//printf("replacing at %d\n",i);
				A[alen-1]=C[A[alen-1]][S[i]];
			}
			else
			{
				REP(j,alen)
				{
					if(O[A[j]][S[i]])
					{
						alen=0;
						break;
					}
				}
				if(alen!=0)
				A[alen++]=S[i];
			}
		}
		printf("Case #%d: [",cases);
		if(alen>0)
		{
			printf("%c",A[0]);
			FOR(i,1,alen)
			printf(", %c",A[i]);
		}
		printf("]\n");
	}
	return 0;
}
