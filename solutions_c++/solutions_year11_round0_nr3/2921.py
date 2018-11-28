#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define clr clear()
#define all(x) x.begin(),x.end()
#define sz(x) (int)x.size()
#define rev reverse
#define mem(x,val) memset((x),(val),sizeof(x));

#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

#define on(bit,pos) (bit)|1<<(pos-1)
#define off(bit,pos) (bit)& ~(1<<(pos-1))
#define check(bit,pos) ((bit)==((bit)|1<<(pos-1)))

using namespace std;

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;

st itoa(i64 a){st ret;for(i64 i=a; i>0; i=i/10) ret+=((i%10)+48);rev(all(ret));return ret;}
int toi(st s){int r=0;istringstream sin(s);sin>>r;return r;}
i64 toi64(st s){i64 r=0;istringstream sin(s);sin>>r;return r;}
double tod(st s){double r=0;istringstream sin(s);sin>>r;return r;}
vs token(st a, st b) {const char *q = a.c_str();while(count(all(b),*q)) q++;vs oot;while(*q){const char *e=q;while(*e&&!count(all(b), *e ) ) e++;oot.push_back( string( q, e ) );q = e;while(count(all(b), *q))q++;}return oot;}


template<class T> inline T gcd(T a,T b) {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T power(T x,T p){if(!p) return 1;return x*power(x,p-1);}

int main()
{
	read("in"); rite("out");
	int test,n,ans,tt,kas=0; i64 sum=0;
	cin>>test;
	while(test--)
	{
		vi num; sum=0;
		cin>>n;
		rep(i,n){
			cin>>tt;
			if(!i) ans=tt;
			else ans=ans^tt;
			num.pb(tt);
			sum+=tt;
		}
		
		printf("Case #%d: ",++kas);
		if(!ans){
			sort(all(num));
			cout<<sum-num[0]<<endl;
		}
		else cout<<"NO"<<endl;
	}
	return 0;
}
