#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const double EPS=1e-8;
double W,L,len;
int T,N;

struct CIC
{
	double r,x,y;
	int id;
	bool operator<(const CIC &rhs) const
	{
		return r>rhs.r;
	}
}C[1000];
double rx[1000],ry[1000];

void init()
{
	scanf("%d%lf%lf",&N,&W,&L);
	for(int i=0;i<N;i++)
	{
		scanf("%lf",&C[i].r);
		C[i].id=i;
	}
	sort(C,C+N);
	len=sqrt(W*W+L*L);
}
const double PI=acos(-1.0);
const double T_STEP=PI/100;
bool check(double x,double y,int id)
{
	for(int i=0;i<id;i++)
	{
		double rl=sqrt( (x-C[i].x)*(x-C[i].x) + (y-C[i].y)*(y-C[i].y) );
		if(rl<C[i].r+C[id].r+EPS)
			return false;
	}
	return true;
}
void work()
{
	double x,y;
	double RA,TH;
	
	for(int i=0;i<N;i++)
	{
		bool suc=false;
		for(RA=0;RA<len+EPS;RA+=C[i].r/2)
		{
			int yyy=1;
			for(TH=0;TH<0.5*PI+EPS;TH+=T_STEP)
			{
				x=RA*cos(TH);
				y=RA*sin(TH);
				if(x>W || y>L)
					continue;
				if(check(x,y,i))
				{
					rx[C[i].id]=C[i].x=x;
					ry[C[i].id]=C[i].y=y;
					suc=true;
					goto next;
				}
			}
		}
next:;
		if(!suc) cout<<"fuck"<<endl;
	}
}
void answer()
{
	for(int i=0;i<N;i++)
		printf(" %lf %lf",rx[i],ry[i]);
	puts("");
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int cnb=1;cnb<=T;cnb++)
	{
		init();
		work();
		printf("Case #%d:",cnb);
		answer();
	}
}