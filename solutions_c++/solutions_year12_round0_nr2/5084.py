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
#define dif(a,b) (a>b?a-b:b-a)

using namespace std;
 
template< class T > T sq(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template< class T > T power(T N,T P){  return (P==0)?  1: N*power(N,P-1); }
struct node{
	int n1,n2,n3;
};
vector<node>v[100];
int fun(int i,int j)
{
	int n1=v[i][j].n1;
	int n2=v[i][j].n2;
	int n3=v[i][j].n3;
	if(dif(n1,n2)==2 || dif(n1,n3)==2 || dif(n3,n2)==2)	return 2;
	return 0;
}
int fun1(int i,int j)
{
	int n1=v[i][j].n1;
	int n2=v[i][j].n2;
	int n3=v[i][j].n3;
	return max(max(n1,n2),n3);
}
int main()
{
	int t,q,i,j,k,l,n,res,s,p;
	int b[100];
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(q=1;q<=t;q++)
	{
		scanf("%d%d%d",&n,&s,&p);
		node temp;
		rep(i,0,n)	SD(b[i]);
		rep(i,0,n)	v[i].clear();
		rep(i,0,n)
		{
			int num=b[i];
			for(j=0;j<=num;j++)
			{
				for(k=0;k<=num;k++)
				{
					if(dif(j,k)>2)	continue;
					for(l=0;l<=num;l++)
					{
						if(dif(j,l)>2 || dif(k,l)>2)	continue;
						if((j+k+l)==num)
						{
							//printf("%d ----> %d %d %d\n",i,j,k,l);
							temp.n1=j;
							temp.n2=k;
							temp.n3=l;
							v[i].pb(temp);
						}
					}
				}
			}
		}
		res=0;
		if(n==1)
		{
			rep(i,0,sz(v[0]))
			{
				int tot=0;
				if(fun(0,i)==2)	tot++;
				if(tot==s && fun1(0,i)>=p)
				{
					res=1;
					break;
				}
			}
		}
		else if(n==2)
		{
			rep(i,0,sz(v[0]))
			{
				int tot=0;
				if(fun(0,i)==2)	tot++;
				int total=0;
				if(fun1(0,i)>=p)	total++;
				rep(j,0,sz(v[1]))
				{
					if(fun(1,j)==2)	tot++;
					if(fun1(1,j)>=p)	total++;
					if(tot==s)
					{
						res=max(total,res);
					}
					if(fun1(1,j)>=p)	total--;
					if(fun(1,j)==2)	tot--;
				}
				if(fun1(0,i)>=p)	total--;
				if(fun(0,i)==2)	tot--;
			}
		}
		
		else if(n==3)
		{
			rep(i,0,sz(v[0]))
			{
				int tot=0;
				if(fun(0,i)==2)	tot++;
				int total=0;
				if(fun1(0,i)>=p)	total++;
				rep(j,0,sz(v[1]))
				{
					if(fun(1,j)==2)	tot++;
					if(fun1(1,j)>=p)	total++;
					rep(k,0,sz(v[2]))
					{
						if(fun(2,k)==2)	tot++;
						if(fun1(2,k)>=p)	total++;
						if(tot==s)
						{
							res=max(total,res);
						}
						if(fun1(2,k)>=p)	total--;
						if(fun(2,k)==2)	tot--;
					}
					if(fun1(1,j)>=p)	total--;
					if(fun(1,j)==2)	tot--;
				}
				if(fun1(0,i)>=p)	total--;
				if(fun(0,i)==2)	tot--;
			}
		}
		printf("Case #%d: %d\n",q,res);
	}
	return 0;
}
