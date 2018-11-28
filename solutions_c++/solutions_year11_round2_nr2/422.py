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
#define INF 1e15
#define EPS 1e-7

int C,_D,cnt,N;
double D;
int A[1000011];
double tA[1000011];


bool inline f(double t)
{
        //check if in time t, we can achieve min separation
        REP(i,N)
        tA[i] = A[i];

        tA[0] = tA[0] - t;//push him back

        FOR(i,1,N)
        {
                //maintain D from tA[i-1]
                double tpos = tA[i-1] + D;
                double tpos2 = tA[i] - t;
                double tpos3 = tA[i] + t;
                //tpos2,tpos,tpos3
                if(tpos < tpos3 || fabs(tpos - tpos3) < EPS)
                {
                        //assign greedy best
                        if(tpos2 > tpos || fabs(tpos2 - tpos) < EPS)
                        tA[i] = tpos2;
                        else if(tpos > tpos2 && tpos < tpos3)
                        tA[i] = tpos;
                        else
                        tA[i] = tpos3;
                }
                else
                return false;
        }
        return true;
}

bool inline f1(double d)
{
    //printf("f called with %lf\n",d);
    double st=A[0]-d;
    FOR(i,1,cnt+1)
    {
        if((st+D)>A[i])
        {
            if((st+D)<(A[i]+d))
            st=st+D;
            else return false;
        }
        else
        st=max(st+D,A[i]-d);
    }
    return true;
}

double solve()
{
    double low=0,high=INF;
    double mid;
    int itr=400;
    while(itr--)
    {
        mid = (low+high)/2.0;
        if(f(mid))
        high = mid;
        else low = mid;
        if(fabs(low-high) < EPS)
        break;
    }
    if(f(low))return low;
    if(f(mid))return mid;
    if(f(high))return high;
    assert(-1 > 0);
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T;
    s(T);
    FOR(cases,1,T+1)
    {
        s(C),s(_D);
        D=_D;
        cnt=0;
        REP(i,C)
        {
            int v,p;
            s(p);s(v);
            REP(j,v)A[cnt++]=p;
        }
        N=cnt;
        printf("Case #%d: %.9lf\n",cases,solve());
    }
	return 0;
}
