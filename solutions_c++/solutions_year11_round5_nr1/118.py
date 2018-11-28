#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 

struct P
{
	double x,y;
	P(double _x=0, double _y=0)
	{
		x = _x; y=_y;
	}
	void scan()
	{
		scanf("%lf%lf",&x,&y);
	}
};
struct Line
{
	double A,B,C;
	Line()
	{
	}
	Line(P a, P b)
	{
		A = a.y - b.y;
		B = b.x - a.x;
		C = -(A*a.x+B*a.y);
	}
	P Inter(Line x)
	{
		P res;
		res.x = -(C*x.B - B*x.C);
		res.y = -(A*x.C - C*x.A);
		res.x /= (A*x.B - B*x.A);
		res.y /= (A*x.B - B*x.A);
		return res;
	}
};
int W,Lo,Up,G;
vector<P> lo,up;
double Vect(P a, P b,P c)
{
	a.x-=c.x;
	a.y-=c.y;
	b.x-=c.x;
	b.y-=c.y;
	return a.x*b.y-a.y*b.x;
}
double Search(double x)
{
	double L = 0,R=W+1e-10,m;
	while(R-L> 1e-8)
	{
		m = (L+R)/2;
		double S=0;
		P lastL=lo.back();
		P lastU=up.back();
		for (int i=0;i+1<Lo;i++)
		{
			P t = lo[i+1];
			bool br = 0;
			if (t.x > m)
			{
				lastL = t = Line(lo[i],lo[i+1]).Inter(Line(P(m,0),P(m,1)));
				br = 1;
			}
			S+=Vect(lo[i],t,lo[0]);
			if (br)
				break;
		}
		for (int i=0;i+1<Up;i++)
		{
			P t = up[i+1];
			bool br = 0;
			if (t.x > m)
			{
				lastU = t = Line(up[i],up[i+1]).Inter(Line(P(m,0),P(m,1)));
				br = 1;
			}
			S-=Vect(up[i],t,lo[0]);
			if (br)
				break;
		}
		S+=Vect(lastL,lastU,lo[0]);
		S = fabs(S);
		if (S > x)
			R = m;
		else
			L = m;
	}
	return L;
}
void Solve()
{
	scanf("%d%d%d%d",&W,&Lo,&Up,&G);
	lo.clear();
	up.clear();
	for (int i=0;i<Lo;i++)
	{
		lo.push_back(P());
		lo.back().scan();
	}
	for (int i=0;i<Up;i++)
	{
		up.push_back(P());
		up.back().scan();
	}
	double S=0;
	for (int i=1;i+1<Lo;i++)
	{
		S+=Vect(lo[i],lo[i+1],lo[0]);
	}
	S+=Vect(lo.back(),up.back(),lo[0]);
	for (int i=Up-1;i-1>=0;i--)
	{
		S+=Vect(up[i],up[i-1],lo[0]);
	}
	for (int i=1;i<=G-1;i++)
	{
		double res = Search((i)*S/G);
		printf("%.7lf\n",res);
	}
}
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		printf("Case #%d:\n",test);
		Solve();
	}
	return 0; 
}