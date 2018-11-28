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
#define MAXC 256
int combine[MAXC][MAXC];
int oppose[MAXC][MAXC];
char str[MAXC];
char res[MAXC];

int main()
{
	int T;
	s(T);
	FOR(cases,1,T+1)
	{
		memset(combine,-1,sizeof combine);
		memset(oppose,0,sizeof oppose);
		
		int C,D;
		s(C);
		REP(i,C)
		{
			scanf("%s",str);
			combine[str[0]][str[1]] = str[2];
			combine[str[1]][str[0]] = str[2];
		}
		s(D);
		REP(i,D)
		{
			scanf("%s",str);
			oppose[str[0]][str[1]] = 1;
			oppose[str[1]][str[0]] = 1;
		}
		int N;
		s(N);
		scanf("%s",str);
		int l = 0;
		res[l] = 0;
		
		REP(i,N)
		{
			if(l == 0)
			res[l++] = str[i];
			else
			{
				res[l++] = str[i];
				//now check combine
				if(combine[res[l-1]][res[l-2]] != -1)
				{
					char x = combine[res[l-1]][res[l-2]];
					res[l-2] = x;
					l -= 1;
				}
				else
				{
					//check oppose
					bool f = 0;
					for(int j=0;j<l && !f;j++)
					{
						for(int k=j+1;k<l && !f;k++)
						{
							if(oppose[res[j]][res[k]])
							f = true;
						}
					}
					if(f)
					l = 0;
				}
			}
		}
		res[l] = 0;
		printf("Case #%d: [",cases);
		REP(i,l)
		{
			if(i > 0)
			printf(", ");
			printf("%c",res[i]);
		}
		printf("]\n");
	}
	return 0;
}
