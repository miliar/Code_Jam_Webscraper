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

//#define codegambler
int main()
{
    #ifdef codegambler
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int L,D,N;
    cin>>L>>D>>N;
    V(string) dic,tdic;
    REP(i,D)
    {
        string tmp;
        cin>>tmp;
        tdic.PB(tmp);
    }
    
    REP(i,N)
    {
        dic=tdic;
        V(string)vs1,vs2;
        string word,s[L];
        cin>>word;
        int sz=word.SZ;
        int k=0;
        REP(x,L)
        {
            if(word[k]!='(')
            s[x]+=word[k];
            if(word[k]=='(')
            {
                k++;
                while(word[k]!=')')
                s[x]+=word[k++];
            }
            k++;
        }
        //REP(i,L)cout<<s[i]<<" ";cout<<endl;
        int count=0;
        int res=0;
        REP(j,L)
        {
            V(string)temp;
            count=0;
            REP(i,dic.SZ)
            {
                    if((s[j].find(dic[i][j]))!=string::npos)
                    {    
                        temp.PB(dic[i]);
                        count++;
                    }   
            }
            dic=temp;
            if(res=0)
                res=count;
            else 
            res=gcd(res,count);
            // FOREACH(it,dic)cout<<*it<<endl;cout<<"\n";
            //res*=count;
        }
                
        //REP(it,L)cout<<s[it]<<" ";
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }            
 	return 0;
}
