#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) (int)v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

struct Interval
{
	int b,e,w;
	Interval() {}
	Interval(int b,int e,int w):b(b),e(e),w(w) {}
	bool operator<(const Interval& X) const
	{
	//	return b < X.b;
		return w < X.w;
	}
	double length() const 
	{
		return e-b;
	}
};

int main()
{
#ifdef HOME_PC
	freopen ("A-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("A-large.out","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		int X,S,R,N;
		double T;
		cin>>X>>S>>R>>T>>N;

		vector<Interval> intervals;
		intervals.push_back(Interval(0,0,0));
		FOR(i,0,N)
		{
			int b,e,w;
			cin>>b>>e>>w;
			intervals.push_back(Interval(b,e,w));
		}	
		intervals.push_back(Interval(X,X,0));

	//	sort(ALL(intervals));

		vector<Interval> x(1,intervals[0]);

		FORSZ(i,1,intervals)
		{
			x.push_back(Interval(intervals[i-1].e,intervals[i].b,0));
			x.push_back(intervals[i]);
		}
		
		intervals = x;

		sort(ALL(intervals));

		double passed = 0;
		REPSZ(i,intervals)
		{	
			double runTime = intervals[i].length() / (R + intervals[i].w);
			runTime = min(runTime,T);		
			passed += runTime;
			T -= runTime;
			double gone = (R + intervals[i].w)*runTime;
			passed += (intervals[i].length() - gone)/(S + intervals[i].w);
		}	

		printf("Case #%d: %.10lf\n",cas,passed);
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

