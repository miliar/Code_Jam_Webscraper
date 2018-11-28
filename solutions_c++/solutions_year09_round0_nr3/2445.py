//Author : Pankaj Kumar
#include <cassert>
#include <cctype>
#include <cfloat>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

#define Debug 0
#define INF 1e10
#define VAR(x,a) 	__typeof(a) x=(a)
#define FOREACH(it,c) 	for(VAR(it,(c).begin());it!=(c).end();++it)
#define FOR(i,a,b)  	for(int i=(int)(a),_b=(int)(b) ; i < _b;i++)
#define FORR(i,a,b) 	for(int i=(a),_b=(b);i>=_b;--i)
#define	REP(i,n)    	FOR(i,0,n)
#define ALL(c) 		(c).begin(),(c).end()
#define SZ		size()
#define PB		push_back
#define PF		push_front
#define V(x)    vector< x >
#define VI      V(int)
#define VII     V(VI)
#define VS      V(string)
#define LL      long long
#define LD      long double
#define PI      pair<int,int>
#define MP      make_pair


const double eps=1e-11;
const double pi=acos(-1.0);

/* Bitmasking Common Operator Follows */
#define two(X) (1<<(X))
#define twoL(X) (((ll)1)<<(X))
#define setBit(S,X) (S|=two(X))
#define setBitL(S,X) (S|=twoL(X))
#define contain(S,X) ((S&two(X))>0)
#define containL(S,X) ((S&twoL(X))>0)

/* Numeric Function */
template<class T> inline T gcd(T a,T b){if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}

template<class T> inline bool isPrime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}

/* Most Common Coversion */
template<class T> LL toInt(T n){stringstream ost;ost<<n;LL ret;ost>>ret;return ret;}
template<class T> string toString(T n){stringstream ost;ost<<n;ost.flush();return ost.str();}

//Don't Code Until You are sure of your Idea , God Bless You !
char msg[]="welcome to code jam";
int sz=strlen(msg);

//#define codegambler
int main()
{
    #ifdef codegambler
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    
    int T;
    cin>>T;
    getchar();
    int x=1;

    while(T--)
    {
        char s[35];
        gets(s);
        int res=0;
        //cout<<s<<" ";
        int len=strlen(s);
        FOR(a1,0,len)
        {
            if(s[a1]=='w')
            FOR(a2,a1+1,len)
            {
                if(s[a2]=='e')
                FOR(a3,a2+1,len)
                {
                    if(s[a3]=='l')
                    FOR(a4,a3+1,len)
                    {
                        if(s[a4]=='c')
                        FOR(a5,a4+1,len)
                        {
                            if(s[a5]=='o')
                            FOR(a6,a5+1,len)
                            {
                                if(s[a6]=='m')
                                FOR(a7,a6+1,len)
                                {
                                    if(s[a7]=='e')
                                    FOR(a8,a7+1,len)
                                    {
                                        if(s[a8]==' ')
            FOR(a9,a8+1,len)
            {
                if(s[a9]=='t')
                FOR(a10,a9+1,len)
                {
                    if(s[a10]=='o')
                    FOR(a11,a10+1,len)
                    {
                        if(s[a11]==' ')
                        FOR(a12,a11+1,len)
                        {
                            if(s[a12]=='c')
                            FOR(a13,a12+1,len)
                            {
                                if(s[a13]=='o')
                                FOR(a14,a13+1,len)
                                {
                                    if(s[a14]=='d')
                                    FOR(a15,a14+1,len)
                                    {
                                        if(s[a15]=='e')
            FOR(a16,a15+1,len)
            {
                if(s[a16]==' ')
                FOR(a17,a16+1,len)
                {
                    if(s[a17]=='j')
                    FOR(a18,a17+1,len)
                    {
                        if(s[a18]=='a')
                            FOR(a19,a18+1,len)
                            {
                                
                                if(s[a19]=='m')
                                res++;
                            }
                    }}}}}}}}}}}}}}}}}}
                            
       printf("Case #%d: %04d\n",x++,res);
    }
 	return 0;
}
