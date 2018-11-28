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
using namespace std;

#pragma comment(linker,"/stack:16000000")

#define ALL(v) v.begin(),v.end()
#define SZ(v) v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=start;i<N;++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

VI x[3],v[3];

double f(double t)
{
	double X[3]={0,0,0};
	int N = x[0].size();

	FOR(i,0,3)
		FOR(j,0,N)
		X[i]+=x[i][j]+t*v[i][j];

	double sum = 0;
	FOR(i,0,3)
	{
		X[i]/=N;
		X[i]*=X[i];
		sum+=X[i];
	}

	return sqrt(max(sum,0.0));
}





int main()
{
//freopen ("input.txt","r",stdin);
//freopen ("in.txt","r",stdin);
freopen ("output.txt","w",stdout);

	int tt;
	cin>>tt;
	for(int cas = 1;cas<=tt;++cas)
	{
		int N;
		cin>>N;
		FOR(i,0,3)
		{
			v[i].resize(N);
			x[i].resize(N);
		}

		FOR(j,0,N)
		{
			FOR(i,0,3)
				cin>>x[i][j];
			FOR(i,0,3)
				cin>>v[i][j];
		}

		double a1 = f(0);
		double a2 = f(1);
		double a3 = f(2);

		if(fabs(a1-a2)<eps&&fabs(a2-a3)<eps)
		{
			printf("Case #%d: %.8lf %.8lf\n",cas,f(0),0);
			continue;
		}

		double l = 0, r = 1e12;

		int cnt = 0;

		while(fabs(l-r)>eps)
		{
			++cnt;
			if(cnt>2000) break;
			
			double t1 = (2*l+r)/3;
			double t2 = (l+2*r)/3;

			double a1 = f(t1);
			double a2 = f(t2);

			if(a1<a2)
				r = t2;
			else
				l = t1;
		}
		printf("Case #%d: %.8lf %.8lf\n",cas,f(l),l);
	}

	return 0;
}

