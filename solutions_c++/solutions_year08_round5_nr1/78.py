#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const int NIL = (-1);
const int N = 7010;
const int INF = 1000*1000*1000+10;
const long long LINF = (long long)(INF)*(long long)(INF)+10LL; 

typedef unsigned U;
typedef long long LL;
typedef long double LD;
typedef unsigned long long UL;

typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<long long> VL;
typedef pair<int,int> PI;
typedef VI::iterator VIT;
typedef VL::iterator VLT;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,b,e) for (int i=(b); i<=(e); i++)
#define FORD(i,b,e) for (int i=(b); i>=(e); i--)
#define FORALL(i,c) for (__typeof(c.begin()) i=(c.begin()); i!=c.end(); i++)
#define FOREACH FORALL
#define SIZE(c) ((int)(c.size()))
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

LL gcd(LL a, LL b) { return b ? gcd(b,a%b) : a; }
LL binpow(LL a, LL d, LL mod)
{
	if (!d) return 1;
	static LL tmp = binpow(a,d/2,mod);
	tmp = (tmp * tmp) % mod;
	return d&1 ? (tmp*a)%mod : tmp;
}
#define rev_prime(a,p) binpow(a,p-2,p)
#define coprimes(a,b) (gcd(a,b)==1)

int BC(UL x) { return x ? 1+BC(x^(x&((~x)+1))) : 0; }

vector<PI> V;
void load_data()
{
	V.clear();
	int x,y;
	int dir = 0;
	x=y=N/2;
	string tmp;
	int i;
	cin >> i;
	while (i--)
	{
		int j;
		cin >> tmp >> j;
		while (j--)
		{
			REP(k,tmp.length())
			{
				if (tmp[k]=='L') dir = (dir+3)%4;
				if (tmp[k]=='R') dir = (dir+1)%4;
				if (tmp[k]=='F')
				{
					if (dir==0) y++;
					if (dir==1) x++;
					if (dir==2) y--;
					if (dir==3) x--;
					V.PB(MP(x,y));
				}
			}
		}
	}
//	FOREACH(i,V)
//		cout << i->ST-N/2 <<  " " << i->ND-N/2 << endl;
}

inline int det(PI &a, PI &b)
{
	return (a.ST*b.ND-a.ND*b.ST);
}

inline int area()
{
	int aa = 0;
	FOR(i,1,SIZE(V)-1) aa+=det(V[i-1],V[i]);
	aa+=det(V[SIZE(V)-1],V[0]);
	if (aa<0) aa*=(-1);
	return aa/2;
}

inline int area2()
{
	int xlo[N],xhi[N],ylo[N],yhi[N];
	REP(i,N) {ylo[i]=xlo[i]=INF;yhi[i]=xhi[i]=0-INF;}
	FOREACH(i,V)
	{
		ylo[i->ND]=min(ylo[i->ND],i->ST);
		yhi[i->ND]=max(yhi[i->ND],i->ST);
		xlo[i->ST]=min(xlo[i->ST],i->ND);
		xhi[i->ST]=max(xhi[i->ST],i->ND);

	}
	
	int aa = 0;
/*	REP(i,N)
	{
		if (xlo[i]<INF) cout << "xlo[" << i-N/2 << "] " << xlo[i]-N/2 << endl;
		if (xhi[i]>-INF) cout << "xhi[" << i-N/2 << "] " << xhi[i]-N/2 << endl;
		if (ylo[i]<INF) cout << "ylo[" << i-N/2 << "] " << ylo[i]-N/2 << endl;
		if (yhi[i]>-INF) cout << "yhi[" << i-N/2 << "] " << yhi[i]-N/2 << endl;
	}//*/
	REP(x,N) REP(y,N)
	{
		if ( (ylo[y]<=x && yhi[y]>x && ylo[y+1]<=x&&yhi[y+1]>x) || (xlo[x]<=y && xhi[x]>y && xlo[x+1]<=y && xhi[x+1]>y)) 
		{

//			cout << x-N/2 << " " << y-N/2<<endl;
			aa++;
		}
	}

	return aa;
}


inline void single_case(int case_number)
{
	load_data();
	
	cout << "Case #" << case_number+1 <<": ";
	cout << area2()-area();
	cout << endl;



}

int main()
{
	int j = 1;
	scanf("%d",&j);//*/
	REP(i,j) single_case(i);
	return 0;
}

