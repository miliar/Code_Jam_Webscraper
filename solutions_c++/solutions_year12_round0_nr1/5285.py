//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:0x800000")
 
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#define maxim 2010
#define LLD long long int
#define LLU long long unsigned
#define pi acos(-1.0)
#define inf (1<<29)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define sz(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define eps 1e-9
#define rep(i,init,n) for(i=init;i<n;i++)
#define rem(i,init,n) for(i=init;i>n;i--)
#define area(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define sqr(x) ((x)*(x))
#define distSqr(x1,y1,x2,y2) ( sqr(x1-x2) + sqr(y1-y2) )
#define spDist(lat1,long1,lat2,long2,r) ( r * acos( sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1-long2) ) )
#define isEq(a,b) (fabs(a-b)<eps)
#define STR string
#define LF double
#define IT iterator
#define VI vector<int>
#define VLLD vector<LLD>
#define VS vector<STR>
#define VLF vector<LF>
#define MII map<int,int>
#define MIB map<int,bool>
#define MSI map<STR,int>
#define MSB map<STR,bool>
#define MSS map<STR,STR>
#define M2dII map<int,map<int,int> >
#define QI queue<int>
#define SI stack<int>
#define PII pair< int, int >
#define PPI pair< PII, int >
#define ff first
#define ss second
#define VPII vector<PII>
#define MP make_pair
 
#define chkB(a,k) (bool)(a[k>>5] & (1<<(k&31)))
#define setB0(a,k) (a[k>>5] &= ~(1<<(k&31)))
#define setB1(a,k) (a[k>>5] |= (1<<(k&31)))
 
#define SD(a) scanf("%d",&a)
#define SHD(a) scanf("%hd",&a)
#define SLLD(a) scanf("%lld",&a)
#define SLLU(a) scanf("%llu",&a)
#define SF(a) scanf("%f",&a)
#define SLF(a) scanf("%lf",&a)
#define SC(a) scanf("%c",&a)
#define SS(a) scanf("%s",a)
 
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
 
int diru[] = {-1,-1,-1,0,0,1,1,1};
int dirv[] = {-1,0,1,-1,1,-1,0,1};
 
using namespace std;
 
template< class T > T sq(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template< class T > T power(T N,T P){  return (P==0)?  1: N*power(N,P-1); }
char a[100000];
int main()
{
	int t,q,i;
	char b[1000],dummy;
	b['a'] = 'y';
	b['b'] = 'h';
	b['c'] = 'e';
	b['d'] = 's';
	b['e'] = 'o';
	b['f'] = 'c';
	b['g'] = 'v';
	b['h'] = 'x';
	b['i'] = 'd';
	b['j'] = 'u';
	b['k'] = 'i';
	b['l'] = 'g';
	b['m'] = 'l';
	b['n'] = 'b';
	b['o'] = 'k';
	b['p'] = 'r';
	b['q'] = 'z';
	b['r'] = 't';
	b['s'] = 'n';
	b['t'] = 'w';
	b['u'] = 'j';
	b['v'] = 'p';
	b['w'] = 'f';
	b['x'] = 'm';
	b['y'] = 'a';
	b['z'] = 'q';
	b[' '] = ' ';
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%c",&t,&dummy);
	for(q=1;q<=t;q++)
	{
		gets(a);
		int len = strlen(a);
		printf("Case #%d: ",q);
		rep(i,0,len)	printf("%c",b[(int)a[i]]);
		printf("\n");
	}
	return 0;
}
