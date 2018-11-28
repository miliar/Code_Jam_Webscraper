/**

  Author: Zafar Ahmad
  Reg.No: 2008331028
        SUST

**/

#include <iostream>
#include <string>
#include <cmath>
#include <complex>
#include <utility>
#include <cstdio>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <list>
#include <set>
#include <sstream>
#include <iterator>
#include <numeric>
#include <functional>
#include <climits>
#include <cstddef>
#include <bitset>
#include <ctime>
#include <memory.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#ifdef __GNUC__
typedef long long ll;typedef unsigned long long ull;
#else
typedef __int64 ll;  typedef unsigned __int64 ull;
#endif

#define REP(i,n)    for(i=0;i<n;i++)
#define REV(i,n)    for(i=n;i>=0;i--)
#define FOR(i,x,y)  for(i=x;i<=y;i++)

#define all(x)      (x).begin(), (x).end()
#define Sort(x)     sort(x.begin(),x.end())
#define Reverse(x)  reverse(x.begin(),x.end())
#define mem(x,with) memset(x,(with),sizeof(x))
#define bug(x)      cout<< "->" <<#x<<": "<<x<<endl
#define UN(v)       sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acu(x)      accumulate(x.begin(),x.end(),0)
#define bits(x)     __builtin_popcount( x )
#define SZ(x)       (int)x.size()
#define tr(c, i)    for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define iter(c)     __typeof((c).begin())
#define CLR(x)      x.clear()
#define min(a,b)    (a<b?a:b)
#define max(a,b)    (a>b?a:b)
#define oo          (1<<28)
#define PB          push_back
#define PF          push_front
#define fs          first
#define sc          second
#define pi          2*acos()
#define two(x)      (1<<x)
#define twoL(X)     (((ll)(1))<<(X))
#define sqr(x)      (x*x)
#define ERR         1e-7
#define MARK(n)     printf("MARK %d  LINE: %d\n",n,__LINE__);
#define CROSS(a,b,c,d)  ((b.x-a.x)*(d.y-c.y) - (d.x-c.x)*(b.y-a.y))
#define DOT(a,b,c,d)    ((b.x-a.x)*(b.y-a.y) - (d.x-c.x)*(d.y-c.y))
#define SIZE        1000000
const double PI=acos(-1.0);

template<class T> void out(const vector<T> &a) { cout<<"array: "; for (int i=0;i<SZ(a);i++) cout<<a[i]<<" "; cout<<endl; cout.flush(); }
template<class T> T gcd(T a,T b) { return (b==0)?a:gcd(b,a%b); }
template<class T> T Abs(T x) {return x > 0 ? x : -x;}
template<class T> inline bool isPrime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> T lcm(T a,T b) { return a*(b/gcd(a,b)); }
template<typename T> static T mod(T a, T b) { a %= b; if (a < 0) a += b; return a; }
template<class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template<typename T> static void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
ll toLl(string s){ll r=0;istringstream sin(s); sin>>r; return r;}
bool IsVowel(char ch){ch=tolower(ch);if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')return true;return false;}
//compute b^p%m
int BigMod(ll B,ll P,ll M){	ll R=1;	while(P>0)	{if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;}	return (int)R;}
/*calculates (a*b)%c taking into account that a*b might overflow */
ll mulmod(ll a,ll b,ll c){ ll x = 0,y=a%c; while(b>0){ if(b%2 == 1){x=(x+y)%c;} y=(y*2)%c;b/= 2;}return x%c;}
//print a number in binary format with n length
void binprint(int mask,int n){int i;string s="";do{s+=(mask%2+'0');mask/=2;}while(mask);Reverse(s);s=string(max(n-SZ(s),0),'0')+s;for(i=SZ(s)-n;i<SZ(s);i++) printf("%c",s[i]);printf("\n");}
ll mpow(ll x,ll k) { if( k==0) return 1; ll r=mpow(x,k/2); return k%2?(r*r*x):(r*r); }                 // Power Calculation function

//struct pq{    int cost,node;bool operator<(const pq &b)const{return cost>b.cost;}};// Min Priority Queue
//typedef struct{int x,y;}P;P pvt;
//typedef struct{int x,y;}man;man PArray[1000];
//bool com(man a,man b){ if(a.x==b.x) return a.y<b.y; return a.x<b.x;}

typedef pair<int,int>   pii;
typedef pair<double,double> pdd;
typedef vector<int>     vi;
typedef vector<double>  vd;
typedef vector<ll>      vll;
typedef vector<string>  vs;
typedef vector<vi>      vii;
typedef vector<vll>     vvll;
typedef vector<vd>      vvd;
typedef vector<pii>     vpii;
typedef map<string,int> msi;
typedef map<int,int>    mii;
typedef map<pii,int>    mpi;
typedef list<int>       li;
typedef istringstream   iss;

//int month[]={31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={2,1,-1,-2,-1,1};int dy[]={0,1,1,0,-1,-1}; //Hexagonal Direction

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test,cas=0,d,g,x,y;
    ll n;

    cin>>test;
    while(test--)
    {
        cin>>n>>d>>g;
        x=gcd(100,d);
        y=100/x;
        if(n<y)
           printf("Case #%d: Broken\n",++cas);
        else if((d>0 && g==0) || (d<100 && g==100))
            printf("Case #%d: Broken\n",++cas);
        else
            printf("Case #%d: Possible\n",++cas);
    }

    return 0;
}

