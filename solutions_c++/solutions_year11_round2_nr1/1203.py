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

inline st itoa(i64 a){st ret;for(i64 i=a; i>0; i=i/10) ret+=((i%10)+48);rev(all(ret));return ret;}
inline int toi(st s){int r=0;istringstream sin(s);sin>>r;return r;}
inline i64 toi64(st s){i64 r=0;istringstream sin(s);sin>>r;return r;}
inline double tod(st s){double r=0;istringstream sin(s);sin>>r;return r;}
inline vs token(st a, st b) {const char *q = a.c_str();while(count(all(b),*q)) q++;vs oot;while(*q){const char *e=q;while(*e&&!count(all(b), *e ) ) e++;oot.push_back( string( q, e ) );q = e;while(count(all(b), *q))q++;}return oot;}


template<class T> inline T gcd(T a,T b) {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T power(T x,T p){if(!p) return 1;return x*power(x,p-1);}

const int mx=110;

int main()
{
	read("in"); rite("out");
	double cl = clock();
	
	int test;
	cin>>test;
	rep(loop,test)
	{
		int n;
		vector<double> wp,owp,oowp,rpi;
		st game[mx];
		cin>>n;
		rep(i,n) cin>>game[i];
		
		rep(i,n)
		{
			int tot=0, cnt=0;
			rep(j,n)
			{
				if(game[i][j]!='.')
				{
					tot++;
					if(game[i][j]=='1') cnt++;
				}
			}
			double temp=(double)cnt/(double)tot;
			//cout<<"wp "<<temp<<endl;
			wp.pb(temp);
		}
		
		
		rep(k,n)
		{
			double oo=0, ccnt=0;
			rep(i,n) if(i!=k) if(game[i][k]!='.')
			{
				ccnt++;
				int tot=0, cnt=0;
				rep(j,n) if(j!=k)
				{
					if(game[i][j]!='.')
					{
						tot++;
						if(game[i][j]=='1') cnt++;
					}
				}
				double temp=(double)cnt/(double)tot;
				oo+=temp;
				//cout<<"   "<<temp<<endl;
			}
			
			//cout<<oo<<endl;
			oo=oo/(double)ccnt;
			
			//cout<<k<<" owp "<<oo<<endl;
			owp.pb(oo);
		}
		
		rep(i,n)
		{
			double tot=0,cnt=0;
			rep(j,n) if(j!=i && game[j][i]!='.')
			{
				tot+=owp[j];
				cnt++;
			}
			double tt=tot/(double)cnt;
			oowp.pb(tt);
		}
		
		printf("Case #%d:\n",loop+1);
		rep(i,n)
		{
			double temp=0;
			//cout<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;
			temp= (0.25 * wp[i]) + (0.50 * owp[i]) + (0.25 * oowp[i]);
			cout<<temp<<endl;

		}
		
		
	}
	
	
	cl = clock() - cl;
	fprintf(stderr, "Total Execution Time = %lf seconds\n", cl / CLOCKS_PER_SEC);
	return 0;
}
