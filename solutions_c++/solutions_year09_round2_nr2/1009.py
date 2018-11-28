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

/* Numeric Function */
template<class T> inline T gcd(T a,T b){if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline bool isPrime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}

/* Most Common Coversion */
template<class T> LL toInt(T n){stringstream ost;ost<<n;LL ret;ost>>ret;return ret;}
template<class T> string toString(T n){stringstream ost;ost<<n;ost.flush();return ost.str();}

//Don't Code Until You are sure of your Idea , God Bless You !
    
bool check(VI &x,VI &c)
{
    int i=0;
    int sz=x.SZ;
    int j=0;
    while(x[i]==c[i]&&i<sz){i++;}
    if(x[i]>c[i])return true;
    if(i==sz)return true;
    else return false;
}
    
#define codegambler
int main()
{
    #ifdef codegambler
        freopen("in.txt","r",stdin);
       freopen("out.txt","w",stdout);
    #endif
    int T;
    cin>>T;
    int i=1;
    getchar();
    while(T--)
    {
        VI x,c;
        char ch;
        while((ch=getchar())!='\n')x.PB(int(ch)-48);
            c=x;
            int sz=x.SZ;
            next_permutation(c.begin(),c.end());
            //cout<<x[0]<<" "<<c[0]<<" ";
            if(check(x,c)){
                x.insert(x.begin(),0);
                c=x;
                 next_permutation(c.begin(),c.end());
                }
        cout<<"Case #"<<i++<<": ";
        FOREACH(it,c)cout<<*it;cout<<endl;
    }
    
    
 	return 0;
}
