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

int main()
{
#ifdef HOME_PC
	freopen ("A-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		int n;
		cin>>n;
		VS a(n);
		FOR(i,0,n)
			cin>>a[i];

		vector<double> rpi(n,0);

		FOR(i,0,n)
		{
			int total = 0;
			int wins = 0;
			FOR(j,0,n)
				if(a[i][j] != '.')
				{
					++total;
					wins += a[i][j] == '1';
				}
			if(total > 0)
				rpi[i] += 0.25 * (wins/(total+0.));
		}

		vector<double> owp(n,0);


		FOR(i,0,n)
		{
			double owpsum = 0;

			int opponents = 0;
			FOR(j,0,n)
				if(a[i][j] != '.')
				{
					++opponents;
					int total = 0;
					int win = 0;
					FOR(k,0,n)
						if(k != i && a[j][k] != '.')
						{
							++total;
							win += a[j][k] == '1';
						}
					if(total > 0)
						owpsum += win/(total+0.);
				}
			if(opponents > 0)
			owp[i] = owpsum/(opponents + 0.);
			rpi[i] += 0.5*owp[i];
		}


		//double owpsum = accumulate(ALL(owp),0);

		FOR(i,0,n)
		{
			int total = 0;
			double sum = 0;
			FOR(j,0,n)
				if(a[i][j] != '.')
				{
					++total;
					sum+=owp[j];
				}
			if(total > 0)
				rpi[i] += 0.25*sum/total;
		}

	
		printf("Case #%d:\n",cas);
		FOR(i,0,n)
			printf("%.12lf\n",rpi[i]);
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

