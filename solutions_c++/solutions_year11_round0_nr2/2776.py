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

const int mx=0;

int main()
{
	read("in"); rite("out");
	int test,kas=0;
	st temp;
	
	scanf("%d",&test);
	rep(loop,test)
	{
		int bas; scanf("%d",&bas);
		map<st,char> base_element;
		rep(i,bas)
		{
			cin>>temp;
			if(temp[0]>temp[1]) swap(temp[0],temp[1]);
			base_element[temp.substr(0,2)]=temp[2];
			//cout<<temp.substr(0,2)<<" "<<temp[2]<<endl;
		}
		
		map<char,char> oppose; int d;
		scanf("%d",&d);
		rep(i,d)
		{
			cin>>temp;
			oppose[temp[0]]=temp[1];
			oppose[temp[1]]=temp[0];
		}
		
		int N;
		st ele,ans="";
		cin>>N>>ele;
		rep(i,sz(ele))
		{
			ans+=ele[i];
			if(sz(ans)>1)//checking pairs
			{
				st cut="";
				cut+=ans[sz(ans)-1];
				cut+=ans[sz(ans)-2];
				sort(all(cut));
				
				if(base_element.find(cut)!=base_element.end())
				{
					//cout<<"pair found "<<cut<<" "<<base_element[cut]<<endl;
					ans=ans.substr(0,sz(ans)-2);
					ans+=base_element[cut];
				}
			}
			
			bool found=false;
			rep(ii,sz(ans)-1)
			{
				if(oppose[ans[sz(ans)-1]]==ans[ii]) { /*cout<<"Oppose found "<<ans[sz(ans)-1]<<" "<<ans[ii]<<endl;*/ found=true; break; }
			}
			
			if(found) ans="";
			//cout<<"____"<<ans<<endl;
		}
		
		printf("Case #%d: [",++kas);
		rep(i,sz(ans)) { if(i) printf(", "); printf("%c",ans[i]); } printf("]\n");
	}
	return 0;
}
